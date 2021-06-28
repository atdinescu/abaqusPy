'''
Author: Ashwin Kumar
Email: ashwin.kumar@vanderbilt.edu
Description: Compute reaction force from output database (.odb).
Code adapted from extractRF_CT01M_01I_R15_PT50_SUB_PR.py.
Calculate Guinea Pig Medial and Lateral sections
'''

from abaqus import *
from abaqusConstants import *
from odbAccess import *
import visualization
import os


'''
Input: Directory containing odb file
Output: odb file name
Description: Get full odb path
'''
def odb_file_retrieval(dirPath):
    for abqFile in os.listdir(dirPath):
        if abqFile.endswith('.odb'):
            return dirPath + '\\' + abqFile

'''
Input: odb full path
Description: Compute reaction force using odb. Adapted from extractRF_CT01M_01I_R15_PT50_SUB_PR.py.
'''
def odb_session_analysis(odbPath):
    o1 = session.openOdb(name=odbPath)
    session.viewports['Viewport: 1'].setValues(displayedObject=o1)
    session.linkedViewportCommands.setValues(_highlightLinkedViewports=False)
    odb = session.odbs[odbPath]
    session.xyDataListFromField(odb=odb, outputPosition=NODAL, variable=(('RF', NODAL, ((COMPONENT, 'RF3'),)),), nodeSets=("PART-1-1.TOP_Z",))
    keyname = 'RF:RF3 PI: PART-1-1 N:'
    RF = [o for o in session.xyDataObjects.values() if o.description.find(keyname) == 0]
    RF = session.xyDataObjects.values()
    xytotal = sum(RF)
    session.writeXYReport(fileName=odbPath.replace('odb', 'rpt'), xyData=xytotal)


for filename in os.listdir(os.getcwd()):
    dirPath = os.getcwd() + '\\\\' + filename
    if os.path.isdir(dirPath) and str(filename).isdigit():
        #opens a new session for each analysis to avoid session reuse
        odb_session_analysis(odb_file_retrieval(dirPath + '\Lateral'))
        odb_session_analysis(odb_file_retrieval(dirPath + '\Medial'))
