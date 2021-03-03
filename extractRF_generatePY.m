 clear all; close all; clc;

dirName = 'G:\Projects-Main\Trab Simulation';
files = dir( fullfile(dirName, '*.odb'));
%%
for i = 1:length(files)
    
    fileName = files(i).name;
    
    fileSave = ['extractRF_',[fileName(1:25)],'.py'];

    fid = fopen(fileSave,'wt');
    
    fprintf(fid,'\n%s','from abaqus import *');
    fprintf(fid,'\n%s','from abaqusConstants import *');
    fprintf(fid,'\n%s','from odbAccess import *');
    fprintf(fid,'\n%s','import visualization');
    fprintf(fid,'\n%s',' ');
    fprintf(fid,'\n%s','o1 = session.openOdb(name=''E:\Projects-Main\Trab Simulation\Jenny_new_subregions\Simulated\Abaqus_ToDo\',fileName(1:25),'.odb)');
    fprintf(fid,'\n%s','session.viewports[''Viewport: 1''].setValues(displayedObject=o1)');
    fprintf(fid,'\n%s','session.linkedViewportCommands.setValues(_highlightLinkedViewports=False)');
    fprintf(fid,'\n%s',' ');
    fprintf(fid,'\n%s','odb = session.odbs[''E:\Projects-Main\Trab Simulation\Jenny_new_subregions\Simulated\Abaqus_ToDo\',fileName(1:25),'.odb]');
    fprintf(fid,'\n%s','session.xyDataListFromField(odb=odb, outputPosition=NODAL, variable=((''RF''');
    fprintf(fid,'\n%s','	NODAL, ((COMPONENT, ''RF3''), ), ),');
    fprintf(fid,'\n%s','nodeSets=("PART-1-1.TOP_Z", )');
    fprintf(fid,'\n%s',' ');
    fprintf(fid,'\n%s','keyname = ''RF:RF3 PI: PART-1-1 N:''');
    fprintf(fid,'\n%s',' ');
    fprintf(fid,'\n%s','RF = [o for o in session.xyDataObjects.values() if');
    fprintf(fid,'\n%s','	o.description.find(keyname)==0]');
    fprintf(fid,'\n%s',' ');
    fprintf(fid,'\n%s','RF=session.xyDataObjects.values()');
    fprintf(fid,'\n%s',' ');
    fprintf(fid,'\n%s','xytotal = sum(RF)');
    fprintf(fid,'\n%s',' ');
    fprintf(fid,'\n%s','session.writeXYReport(fileName=''E:\Projects-Main\Trab Simulation\Jenny_new_subregions\Simulated\Abaqus_ToDo\', ...
      [fileName(1:25)],'.rpt'', xyData=xytotal)');
      
    fclose(fid);
end


