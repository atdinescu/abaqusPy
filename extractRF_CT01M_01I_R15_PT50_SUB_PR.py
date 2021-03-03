
from abaqus import *
from abaqusConstants import *
from odbAccess import *
import visualization
 
o1 = session.openOdb(name='G:\Projects-Main\Trab Simulation\Jenny_new_subregions\Simulated\Abaqus_ToDo\CT01M_01I_R15_PT50_SUB_PR.odb')
session.viewports['Viewport: 1'].setValues(displayedObject=o1)
session.linkedViewportCommands.setValues(_highlightLinkedViewports=False)
 
odb = session.odbs['G:\Projects-Main\Trab Simulation\Jenny_new_subregions\Simulated\Abaqus_ToDo\CT01M_01I_R15_PT50_SUB_PR.odb']
session.xyDataListFromField(odb=odb, outputPosition=NODAL, variable=(('RF', 
	NODAL, ((COMPONENT, 'RF3'), )), ), 
	nodeSets=("PART-1-1.TOP_Z", )
 
keyname = 'RF:RF3 PI: PART-1-1 N:'
 
RF = [o for o in session.xyDataObjects.values() if
	o.description.find(keyname)==0]
 
RF=session.xyDataObjects.values()
 
xytotal = sum(RF)
 
session.writeXYReport(fileName='G:\Projects-Main\Trab Simulation\Jenny_new_subregions\Simulated\Abaqus_ToDo\CT01M_01I_R15_PT50_SUB_PR.rpt', xyData=xytotal)