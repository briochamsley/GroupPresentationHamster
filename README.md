# GroupPresentationHamster
To use the provided scripts with the test-data, you first need to run the CreateRules.bat-File. Afterwards you need to change the data-directory in both PyScripts (first line) and run the BufferQGisPyScript.py ind QGIS and the AnalysisPyScript.py in Grass GIS. In QGIS, once you started the script, it will ask you for different output names. Just ignore these pop-ups and hit execute, the results will be saved in your data directory nevertheless as there is a storing command in the script.

The PreProcessing.bat can be used instead of the CreateRules.bat, it donwloads the data, unzips it, reproject and patch/extract it and creates the rules as well. You need to have wget installed though.
