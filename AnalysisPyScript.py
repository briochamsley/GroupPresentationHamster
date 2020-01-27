#!/usr/bin/env python
import grass.script as gscript


def main():
    #Set Workspace, so you need to change only this path if you're changing folders 
    data_dir=r'D:\Dokumente\Uni\Master\MSc-Sem1\FOSS\Projekt\Data\\'


    ## This Section will import the Study Area and set the Region according to this file
    #-----------------------------------------------------------------------------------
    #Set path for region-File
    region_file=data_dir+'StudyArea.gpkg'

    #Import region file
    gscript.run_command('v.in.ogr', overwrite=True, input=region_file, output='StudyArea', flags='t')

    #Set Region according to the vectorfile
    gscript.run_command('g.region',vector='StudyArea@PERMANENT')

    #Show region
    gscript.run_command('g.region', flags='p')

    
    #In this Section, all paths for the files will be set
    #----------------------------------------------------    
    #Set path for buffered Roads-File
    roads_file=data_dir+'RoadsBuffered.gpkg'

    #Set path for buffered Rail-File
    rail_file=data_dir+'RailBuffered.gpkg'
    
    #Set path for buffered Buildings-File
    buildings_file=data_dir+'BuildingsBuffered.gpkg'
    
    #Set path for Landuse-File
    land_file=data_dir+'Landuse.gpkg'
    
    #Set path for Soilmap-File
    soil_file=data_dir+'soilmap.gpkg'
    
    #Set path for DEM-File
    DEM_file=data_dir+'dem.tif'
    
    #Set path for Reserve-File
    Reserve_file=data_dir+'Reserves.gpkg'
    
    #Set path for the DEM reclass rules
    DEM_rules=data_dir+'DEM_rules.txt'
    
    #Set path for the Soil reclass rules
    Soil_rules=data_dir+'Soil_rules.txt'
    
    #Set path for the landuse reclass rules
    Landuse_rules=data_dir+'Landuse_rules.txt'
    
    #Set path for the size reclass rules
    Size_rules=data_dir+'Size_rules.txt'
    
    
    #In this Section, all needed data will be imported
    #-------------------------------------------------
    #Import buffered Roads-file
    gscript.run_command('v.in.ogr', flags='r', overwrite=True, input=roads_file, output='Roads')

    #Import buffered Rail-file
    gscript.run_command('v.in.ogr', flags='r', overwrite=True, input=rail_file, output='Rail')

    #Import buffered Buildings-file
    gscript.run_command('v.in.ogr', flags='r', overwrite=True, input=buildings_file, output='Buildings')

    #Import Landuse-File
    gscript.run_command('v.in.ogr', flags='r', overwrite=True, input=land_file, output='Landuse')

    #Import Soilmap-file
    gscript.run_command('v.in.ogr', flags='r', overwrite=True, input=soil_file, output='Soilmap')
    
    #Import DEM-file
    gscript.run_command('r.in.gdal', flags='r', overwrite=True, input=DEM_file, output='DEM')
    
    #Import Reserve-File
    gscript.run_command('v.in.ogr', flags='r', overwrite=True, input=Reserve_file, output='Reserves')


    #In this Section, all areas which need to be excluded from the rating will be preprocessed, so it is ready to be cliped out of the study area
    #--------------------------------------------------------------------------------------------------------------------------------------------
    #Extract unsuitable Landuse
    gscript.run_command('v.extract', overwrite=True, flags='d', input='Landuse@PERMANENT', where="(landuse = 'airport') or (landuse = 'allotments') or (landuse = 'aquaculture') or (landuse = 'basin') or (landuse = 'basin;meadow') or (landuse = 'cemetery') or (landuse = 'churchyard') or (landuse = 'civic_admin') or (landuse = 'commercial') or (landuse = 'concrete') or (landuse = 'construction') or (landuse = 'construction1') or (landuse = 'cottage') or (landuse = 'craft') or (landuse = 'depot') or (landuse = 'education') or (landuse = 'events') or (landuse = 'fairgound') or (landuse = 'fairground') or (landuse = 'fishfarm') or (landuse = 'garage') or (landuse = 'garages') or (landuse = 'grave_yard') or (landuse = 'greenhouse_horticulture') or (landuse = 'harbour') or (landuse = 'highway') or (landuse = 'industrial') or (landuse = 'industrial;retail') or (landuse = 'infrastructure') or (landuse = 'institutional') or (landuse = 'kindergarten') or (landuse = 'landfill') or (landuse = 'logistics') or (landuse = 'military') or (landuse = 'nature_reserve') or (landuse = 'nursery') or (landuse = 'observatory') or (landuse = 'offices') or (landuse = 'open_air_warehouse') or (landuse = 'pipelinearea') or (landuse = 'place') or (landuse = 'plaza') or (landuse = 'pond') or (landuse = 'port') or (landuse = 'power') or (landuse = 'public') or (landuse = 'railway') or (landuse = 'railway; highway') or (landuse = 'religious') or (landuse = 'research') or (landuse = 'reservoir') or (landuse = 'residential') or (landuse = 'retail') or (landuse = 'road') or (landuse = 'school') or (landuse = 'sandpit') or (landuse = 'sport') or (landuse = 'Sport') or (landuse = 'storage') or (landuse = 'tourism') or (landuse = 'traffic_calming') or (landuse = 'traffic_islands') or (landuse = 'water') or (landuse = 'water_storage') or (landuse = 'water_well') or (landuse = 'water_wellfield') or (landuse = 'water_works')", output='UnsuitableLanduse')

    #Extract unsuitable Soils
    gscript.run_command('v.extract', overwrite=True, flags='d', input='Soilmap@PERMANENT', where="(NRKART = '0') or (NRKART = '4') or (NRKART = '5') or (NRKART = '6') or (NRKART = '7') or (NRKART = '8') or (NRKART = '9') or (NRKART = '10') or (NRKART = '11') or (NRKART = '12') or (NRKART = '13') or (NRKART = '14') or (NRKART = '30') or (NRKART = '31') or (NRKART = '33') or (NRKART = '34') or (NRKART = '35') or (NRKART = '36') or (NRKART = '73') or (NRKART = '86') or (NRKART = '87') or (NRKART = '91') or (NRKART = '92') or (NRKART = '97')", output='UnsuitableSoils')

    #Reclass the DEM and resample it
    gscript.run_command('r.reclass', overwrite=True, input='DEM@PERMANENT', output='DEMreclass', rules=DEM_rules)
    gscript.run_command('r.resample', overwrite=True, input='DEMreclass@PERMANENT', output='DEMclassified')
    
    #convert the reclassified DEM to vector
    gscript.run_command('r.to.vect', overwrite=True, input='DEMclassified@PERMANENT', output='DEMvector', type='area')
    
    #Extract the unsuitable heights and create an attribute table for the new layer
    gscript.run_command('v.extract', overwrite=True, flags='d', input='DEMvector@PERMANENT', where="(value = '0')", output='UnsuitableHeights')
    gscript.run_command('v.db.addtable', map='UnsuitableHeights@PERMANENT')


    #In this section, all areas which need to be excluded from the rating will be cliped out of the study area
    #---------------------------------------------------------------------------------------------------------
    #check if there are features in the Roadbuffer layer. if yes, Clip the Roadbuffer out of the StudyArea. If not copy the input file and name it like the output file
    featurecount=gscript.parse_command('v.category', input='Roads@PERMANENT', option='report', flags='g')
    if len(featurecount.keys())==0:
        gscript.run_command('g.copy', overwrite=True, vector='StudyArea@PERMANENT,SAS1')
    else :
        gscript.run_command('v.overlay', overwrite=True, ainput='StudyArea@PERMANENT', binput='Roads@PERMANENT', operator='not', output='SAS1')

    #check if there are features in the Railbuffer layer. if yes, Clip the Railbuffer out of the StudyArea. If not copy the input file and name it like the output file
    featurecount=gscript.parse_command('v.category', input='Rail@PERMANENT', option='report', flags='g')
    if len(featurecount.keys())==0:
        gscript.run_command('g.copy', overwrite=True, vector='SAS1@PERMANENT,SAS2')
    else :
        gscript.run_command('v.overlay', overwrite=True, ainput='SAS1@PERMANENT', binput='Rail@PERMANENT', operator='not', output='SAS2')
    
    #check if there are features in the buildings-buffer layer. if yes, Clip the Buildingsbuffer out of the StudyArea. If not copy the input file and name it like the output file
    featurecount=gscript.parse_command('v.category', input='Buildings@PERMANENT', option='report', flags='g')
    if len(featurecount.keys())==0:
        gscript.run_command('g.copy', overwrite=True, vector='SAS2@PERMANENT,SAS3')
    else :
        gscript.run_command('v.overlay', overwrite=True, ainput='SAS2@PERMANENT', binput='Buildings@PERMANENT', operator='not', output='SAS3')

    #check if there are features in the unsuitable landuse layer. if yes, Clip unsuitable Landuse out of the StudyArea. If not copy the input file and name it like the output file
    featurecount=gscript.parse_command('v.category', input='UnsuitableLanduse@PERMANENT', option='report', flags='g')
    if len(featurecount.keys())==0:
        gscript.run_command('g.copy', overwrite=True, vector='SAS3@PERMANENT,SAS4')
    else :
        gscript.run_command('v.overlay', overwrite=True, ainput='SAS3@PERMANENT', binput='UnsuitableLanduse@PERMANENT', operator='not', output='SAS4')

    #check if there are features in the unsuitable Soils layer. if yes, Clip unsuitable Soils out of the StudyArea. If not copy the input file and name it like the output file
    featurecount=gscript.parse_command('v.category', input='UnsuitableSoils@PERMANENT', option='report', flags='g')
    if len(featurecount.keys())==0:
        gscript.run_command('g.copy', overwrite=True, vector='SAS4@PERMANENT,SAS5')
    else :
        gscript.run_command('v.overlay', overwrite=True, ainput='SAS4@PERMANENT', binput='UnsuitableSoils@PERMANENT', operator='not', output='SAS5')
    
    #check if there are features in the unsuitable heights layer. if yes, clip the unsuitable heights out of the StudyArea. If not copy the input file and name it like the output file
    featurecount=gscript.parse_command('v.category', input='UnsuitableHeights@PERMANENT', option='report', flags='g')
    if len(featurecount.keys())==0:
        gscript.run_command('g.copy', overwrite=True, vector='SAS5@PERMANENT,SAS6')
    else :
        gscript.run_command('v.overlay', overwrite=True, ainput='SAS5@PERMANENT', binput='UnsuitableHeights@PERMANENT', operator='not', output='SAS6')

    #check if there are features in the reserves layer. if yes, Clip Reserves out of the StudyArea. If not copy the input file and name it like the output file
    featurecount=gscript.parse_command('v.category', input='Reserves@PERMANENT', option='report', flags='g')
    if len(featurecount.keys())==0:
        gscript.run_command('g.copy', overwrite=True, vector='SAS6@PERMANENT,FeasibleAreas')
    else :
        gscript.run_command('v.overlay', overwrite=True, ainput='SAS6@PERMANENT', binput='Reserves@PERMANENT', operator='not', output='FeasibleAreas')


    #In this section, the size of the potential areas will be calculated
    #-------------------------------------------------------------
    #delete attribute-table of the areas to rate and create a new one in order to loose unneccesary information
    gscript.run_command('v.db.droptable', map='FeasibleAreas@PERMANENT', flags='f')
    gscript.run_command('v.db.addtable', map='FeasibleAreas@PERMANENT')
    
    #calculate size of all areas
    gscript.run_command('v.to.db', map='FeasibleAreas@PERMANENT', option='area', columns='AreaSize', units='meters')
    

    #In this section, all information for the rating will be reclassed (except the DEM, which needed to be reclassed before to extract unsuitable heights)
    #-----------------------------------------------------------------------------------------------------------------------------------------------------
    #Reclass the Landuse, create an attribute table and dissolve common boundaries
    gscript.run_command('v.reclass', overwrite=True, input='Landuse@PERMANENT', output='Landusereclass', rules=Landuse_rules)
    gscript.run_command('v.db.addtable', map='Landusereclass@PERMANENT')
    gscript.run_command('v.dissolve', overwrite=True, input='Landusereclass@PERMANENT', column='cat', output='LanduseClassified')
    gscript.run_command('v.db.addtable', map='LanduseClassified@PERMANENT')

    #minus every value of the classified Landuse Raster by one to get classes out of the category number
    gscript.run_command('r.mapcalc', overwrite=True, expression="LanduseClassRast = LanduseClassRastModified@PERMANENT - 1")
           
    #Reclass the Soil and dissolve common boundaries
    gscript.run_command('v.reclass', overwrite=True, input='Soilmap@PERMANENT', output='Soilreclass', rules=Soil_rules)
    gscript.run_command('v.db.addtable', map='Soilreclass@PERMANENT')
    gscript.run_command('v.dissolve', overwrite=True, input='Soilreclass@PERMANENT', column='cat', output='SoilClassified')
    gscript.run_command('v.db.addtable', map='SoilClassified@PERMANENT')

    #reclass the size of the study areas
    gscript.run_command('v.reclass', overwrite=True, input='FeasibleAreas@PERMANENT', output='SizeReclass', rules=Size_rules)
    gscript.run_command('v.db.addtable', map='SizeReclass@PERMANENT')


    #In this section, the reclassed files will be converted to raster format
    #----------------------------------------------------------------------
    #Convert classified Landuse to Raster
    gscript.run_command('v.to.rast', overwrite=True, input='LanduseClassified@PERMANENT', output='LanduseClassRastModified', use='cat')

    #Convert classified Soils to Raster
    gscript.run_command('v.to.rast', overwrite=True, input='SoilClassified@PERMANENT', output='SoilClassRast', use='cat')
    
    #convert SizeReclass to Raster
    gscript.run_command('v.to.rast', overwrite=True, input='SizeReclass@PERMANENT', output='SizeClassRaster', use='cat')
    

    #In this section, the Rating for each suited polygon will be calculated
    #----------------------------------------------------------------------
    #do a weighted overlay with the Size- (x2), Soil- (x3), Landuse- (x6) and heights-classes (x1)
    gscript.run_command('r.mapcalc', overwrite=True, expression="RatingRaster = DEMclassified@PERMANENT + 2 * SizeClassRaster@PERMANENT +3 * SoilClassRast@PERMANENT + 6 * LanduseClassRast@PERMANENT")

    #extract the polygons which are big enough out of the feasable Areas
    gscript.run_command('v.extract', overwrite=True, input='SizeReclass@PERMANENT', where="cat !=99", output='AreasToRateClassified')
    gscript.run_command('v.overlay', overwrite=True, ainput='FeasibleAreas@PERMANENT', binput='AreasToRateClassified@PERMANENT', operator='and', output='PossibleAreas')

    #Calculate the average Rating value per polygon
    gscript.run_command('v.rast.stats', flags='c', map='PossibleAreas@PERMANENT', raster='RatingRaster@PERMANENT', column_prefix='Rating', method='average', percentile=100)
    
    #set colortable, so the best areas are colored in green, the worst in red
    gscript.run_command('v.colors', map='PossibleAreas@PERMANENT', use='attr', column='Rating_average', color='ryg')
    
    #display result in active graphics frame
    gscript.run_command('d.vect', map='PossibleAreas@PERMANENT')


    

if __name__ == '__main__':
    main()
