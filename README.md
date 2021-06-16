# abaqusPy
* Python scripts to run input files and extract reaction force or displacement results from output database (.odb)

Can run Abaqus input file via command line using
```
call abq2021 job="nameofinputfile" interactive
```

Can extract reaction force using python script (make sure to change file name and directory)
```
abaqus cae noGUI=extractRF_filename.py
```

https://info.simuleon.com/blog/submitting-abaqus-commands-through-the-command-window
