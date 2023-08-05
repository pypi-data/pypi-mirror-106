"""
.. module:: procedure_rig
   :synopsis: helper module for procedures used with any rig

"""

import numpy as np

from . import kine, kine_or, ligaments as liga

import os
from mpl_toolkits.mplot3d import Axes3D
import matplotlib
from .pyver import __pyver
if __pyver == 3:
    matplotlib.use('Qt5Agg')
else:
    matplotlib.use('Qt4Agg')
import matplotlib.pyplot as plt


def performAnalysis(
        markers,
        params,
        resultsDir
        ):
    
    results = {}

    side = params['side']
    
    mkrsLoc = {m: np.array(params['mkrsLoc'][m]['pos']) for m in params['mkrsLoc']}
    
    mkrsSegs = {}
    for m in params['mkrsLoc']:
        if 'fixedTo' in params['mkrsLoc'][m]:
            mkrsSegs[m] = params['mkrsLoc'][m]['fixedTo']
            
    ALs = {m: np.array(params['mkrsLoc'][m]['pos']) for m in params['mkrsLoc']}

    mkrs = markers
    N = markers[list(markers.keys())[0]].shape[0]
    
    t = np.arange(N)
    
    args = {}
    args['mkrsLoc'] = mkrsLoc
    args['verbose'] = False

    RTs = {}

    allALs = {}
    
    defSegPoses = params['defSegPoses']
    
    segList = params['calcSegPoses']['selected']

    poses = {}

    for segName in segList:

        defSegPose = [s for s in defSegPoses if s['name'] == segName][0]

        type = defSegPose['type']
        mkrList = defSegPose['markers'].split(',')
        funName = defSegPose['defFun']

        if type == 'markers_fitting':

            R, T, info = kine.rigidBodySVDFun(mkrs, mkrList, args)
            RT = kine.composeRotoTranslMatrix(R, T)
            RTs[segName] = RT
            pose = {}
            pose['matrix'] = RT
            pose['RMSE'] = info['RMSE']
            pose['err_max'] = info['eMax']
            pose['err_max_marker'] = info['eMaxMarker']
            poses[segName] = pose
            
            plt.subplot(3,2,1)
            plt.plot(t, pose['RMSE'], label=segName)
            plt.legend(loc='upper right', fontsize=7)
            plt.title('Markers fitting RMSE (mm)')
            plt.subplot(3,2,2)
            plt.plot(t, pose['err_max'], label=segName)
            plt.legend(loc='upper right', fontsize=7)
            plt.title('Markers fitting error max (mm)')

        elif type == 'define_from_markers':

            RTseg = RTs[mkrsSegs[mkrList[0]]]
            usedALs = {m: ALs[m] for m in mkrList}
            allALs.update(kine.changeMarkersReferenceFrame(usedALs, RTseg))
            R, T = kine_or.register[funName](allALs, s=side)
            RT = kine.composeRotoTranslMatrix(R, T)
            RTs[segName] = RT
            pose = {}
            pose['matrix'] = RT
            pose['RMSE'] = [0] * N
            pose['err_max'] = [0] * N
            pose['err_max_marker'] = [''] * N
            poses[segName] = pose
            
    results['poses'] = poses
        
    results['landmarks'] = {m: allALs[m] for m in allALs}
    
    defJoints = params['defJoints']
    
    jointsList = params['calcJoints']['selected']
    
    results['joint_angles'] = {}
    results['joint_transl'] = {}
    results['joint_outputs'] = {}

    for jointName in jointsList:

        defJoint = [j for j in defJoints if j['name'] == jointName][0]
        segName1 = defJoint['seg1']
        segName2 = defJoint['seg2']
        invertJointRotMatrix = defJoint['invertJointRotMatrix']
        defAngles = defJoint['R2AnglesFun']
        outputs = defJoint['outputs']

        RT1 = RTs[segName1]
        RT2 = RTs[segName2]

        Ra1, Oa1 = RT1[:,:3,:3], RT1[:,:3,3]
        Ra2, Oa2 = RT2[:,:3,:3], RT2[:,:3,3]

        if defAngles == 'ges':
            R2anglesFun = kine_or.gesOR
            funInput = 'segmentsR'
        else:
            R2anglesFun = defAngles
            funInput = 'jointRMatrix'
        if invertJointRotMatrix:
            Ra1, Ra2 = Ra2, Ra1
        angles = kine.getJointAngles(Ra1, Ra2, R2anglesFun=R2anglesFun, funInput=funInput, s=side)
        transl = kine.getJointTransl(Ra1, Ra2, Oa1, Oa2, T2translFun=kine_or.gesTranslOR)

        results['joint_angles'][jointName] = angles
        results['joint_transl'][jointName] = transl
        
        outputNames = outputs.split(',')
        angleName1 = '%s_%s' % (jointName, outputNames[0])
        angleName2 = '%s_%s' % (jointName, outputNames[1])
        angleName3 = '%s_%s' % (jointName, outputNames[2])
        translName1 = '%s_%s' % (jointName, outputNames[3])
        translName2 = '%s_%s' % (jointName, outputNames[4])
        translName3 = '%s_%s' % (jointName, outputNames[5])
        results['joint_outputs'][angleName1] = angles[:,0]
        results['joint_outputs'][angleName2] = angles[:,1]
        results['joint_outputs'][angleName3] = angles[:,2]
        results['joint_outputs'][translName1] = transl[:,0]
        results['joint_outputs'][translName2] = transl[:,1]
        results['joint_outputs'][translName3] = transl[:,2]
        
        plt.subplot(3,2,3)
        plt.plot(t, angles[:,0], label=angleName1)
        plt.plot(t, angles[:,1], label=angleName2)
        plt.plot(t, angles[:,2], label=angleName3)
        plt.legend(loc='upper right', fontsize=7)
        plt.title('Joint angles (deg)')
        plt.subplot(3,2,4)
        plt.plot(t, transl[:,0], label=translName1)
        plt.plot(t, transl[:,1], label=translName2)
        plt.plot(t, transl[:,2], label=translName3)
        plt.legend(loc='upper right', fontsize=7)
        plt.title('Joint translations (mm)') 
        
    splinesLoc = {s: np.array(params['splines'][s]['pos']) for s in params['splines']}

    splinesSegs = {s: params['splines'][s]['fixedTo'] for s in params['splines']}

    splinesLocParams = {}
    for s in params['splines']:
        splinesLocParams[s] = liga.createParamSpline(splinesLoc[s])
        
    ligaPaths = {}
    ligaLengths = {}
    ligaStrains = {}
    
    defLigas = params['defLigas']
    
    ligasList = params['calcLigas']['selected']
    
    outputSnapshots = params['outputSnapshots']

    for ligaName in ligasList:

        defLiga = [l for l in defLigas if l['name'] == ligaName][0]
        name = defLiga['name']
        ins1 = defLiga['ins1']
        method = defLiga['method']
        spline = defLiga['edge']
        ins2 = defLiga['ins2']

        segIns1 = mkrsSegs[ins1]
        segIns2 = mkrsSegs[ins2]
        if spline != '':
            segSpline = splinesSegs[spline]

        RT1 = RTs[segIns1]
        RT2 = RTs[segIns2]
        if segSpline is not None:
            RTs = RTs[segSpline]

        p1Loc = {ins1: mkrsLoc[ins1]}
        p1 = kine.changeMarkersReferenceFrame(p1Loc, RT1)[ins1]

        p2Loc = {ins2: mkrsLoc[ins2]}
        p2 = kine.changeMarkersReferenceFrame(p2Loc, RT2)[ins2]
        
        ligaPaths[name] = [[]] * N
        ligaLengths[name] = np.nan * np.zeros((N,))
        ligaStrains[name] = np.nan * np.zeros((N,))
        
        ligaSnapshots = [l for l in outputSnapshots if l['output'] == '%s_length' % name]
        ligaLengthRef = None
        if len(ligaSnapshots) > 0:
            ligaSnapshot = ligaSnapshots[0]
            ligaLengthRef = ligaSnapshot['value']
        
        for i in range(N):

            ligaPath = np.array((p1[i,:], p2[i,:]))
    
            if method == 'shortest_via_edge':
    
                splineParams = liga.reposeSpline(splinesLocParams[spline], RTs[i,...])
                dummy, ligaPath = liga.ligamentPathBlankevoort1991(ligaPath, splineParams)
    
            ligaLength = np.linalg.norm(np.diff(ligaPath, axis=0), axis=1).sum()
            
            if ligaLengthRef is not None:
                ligaStrain = 100. * (1.*ligaLength - ligaLengthRef) / ligaLengthRef
            else:
                ligaStrain = np.nan

            ligaPaths[name][i] = ligaPath
            ligaLengths[name][i] = ligaLength
            ligaStrains[name][i] = ligaStrain
        
        plt.subplot(3,2,5)
        plt.plot(t, ligaLengths[name], label=name)
        plt.legend(loc='upper right', fontsize=7)
        plt.title('Ligament lengths (mm)')
        plt.subplot(3,2,6)
        plt.plot(t, ligaStrains[name], label=name)
        plt.legend(loc='upper right', fontsize=7)
        plt.title('Ligament strains (%)') 

    results['paths'] = ligaPaths
    results['lengths'] = ligaLengths
    results['strains'] = ligaStrains
    
    plt.tight_layout()
    
    if not os.path.exists(resultsDir):
        os.mkdir(resultsDir)
    
    manager = plt.get_current_fig_manager()
    manager.window.showMaximized()
    plt.savefig(os.path.join(resultsDir, 'summary.png'), format='png', orientation='landscape')
    
    plt.show()
    
    return results
