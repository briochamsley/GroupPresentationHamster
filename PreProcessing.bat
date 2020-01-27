:: download the data for the study area
wget https://biogeo.ucdavis.edu/data/gadm3.6/gpkg/gadm36_DEU_gpkg.zip 
:: unzip the downloaded data
tar -xf gadm36_DEU_gpkg.zip
:: reproject the unzipped data
ogr2ogr -t_srs EPSG:32632 gadm36_DEUReprojected.gpkg gadm36_DEU.gpkg
:: create a new file with the named regions only
ogr2ogr -sql "SELECT * FROM gadm36_DEU_2 WHERE GID_2 in ('DEU.7.1_1','DEU.1.26_1','DEU.1.15_1','DEU.1.35_1')" RegionenSelect.gpkg gadm36_DEUReprojected.gpkg
:: merge the regions into the study area
ogr2ogr StudyArea.gpkg RegionenSelect.gpkg -dialect sqlite -sql "SELECT ST_Union(geom) AS geometry FROM 'SELECT'"
:: Write the query for the overpass download
@echo [out:xml][maxsize:2000000000];(way["building"](48.803,7.3333,50.087,9.61215););(._;^>;);out; >queryBuildings.txt
:: use the text file with the query to download the data from the api
wget -t 0 --post-file=queryBuildings.txt http://overpass-api.de/api/interpreter --output-document=DownloadBuilding.osm
:: Wait 15 seconds to start the next request
timeout /T 30
:: repeat the last three steps for different queries
@echo [out:xml][maxsize:2000000000];(way[highway~"^(tertiary|motorway|trunk|secondary|residential|motorway_link|trunk_link|primary_link|secondary_link|tertiary_link|living_street|raceway)"](48.803,7.3333,50.087,9.61215););(._;^>;);out; >queryRoad.txt
wget  -t 0 --post-file=queryRoad.txt http://overpass-api.de/api/interpreter --output-document=DownloadRoads.osm
timeout /T 30
@echo [out:xml][maxsize:2000000000];(way["railway"](48.803,7.3333,50.087,9.61215););(._;^>;);out; >queryRail.txt
wget  -t 0 --post-file=queryRail.txt http://overpass-api.de/api/interpreter --output-document=DownloadRail.osm
timeout /T 30
@echo [out:xml][maxsize:2000000000];(way["landuse"](48.803,7.3333,50.087,9.61215););(._;^>;);out; >queryLanduse.txt
wget  -t 0 --post-file=queryLanduse.txt http://overpass-api.de/api/interpreter --output-document=DownloadLanduse.osm
:: copy all features which are lines into a new file, so the new file contains one instead of 5 files only
ogr2ogr -sql "SELECT * FROM lines" -t_srs EPSG:32632 -f GPKG Roads.gpkg DownloadRoads.osm
ogr2ogr -sql "SELECT * FROM lines" -t_srs EPSG:32632 -f GPKG Rail.gpkg DownloadRail.osm
:: copy all features which are multipolygons into a new file, so the new file contains one instead of 5 files only
ogr2ogr -sql "SELECT * FROM multipolygons" -t_srs EPSG:32632 -f GPKG Buildings.gpkg DownloadBuilding.osm
ogr2ogr -sql "SELECT * FROM multipolygons" -t_srs EPSG:32632 -f GPKG Landuse.gpkg DownloadLanduse.osm
:: download the soilmap data, unzip and reproject it
wget https://download.bgr.de/bgr/boden/BUEK250/shp/buek250_mg_utm_v55.zip
tar -xf buek250_mg_utm_v55.zip
ogr2ogr -t_srs EPSG:32632 -f GPKG soilmap.gpkg buek250_mg_utm_v55.shp
:: download the SRTM data and unzip them
wget http://srtm.csi.cgiar.org/wp-content/uploads/files/srtm_5x5/TIFF/srtm_38_03.zip
tar -xf srtm_38_03.zip
wget http://srtm.csi.cgiar.org/wp-content/uploads/files/srtm_5x5/TIFF/srtm_38_02.zip
tar -xf srtm_38_02.zip
wget http://srtm.csi.cgiar.org/wp-content/uploads/files/srtm_5x5/TIFF/srtm_39_02.zip
tar -xf srtm_39_02.zip
wget http://srtm.csi.cgiar.org/wp-content/uploads/files/srtm_5x5/TIFF/srtm_39_03.zip
tar -xf srtm_39_03.zip
:: merge the SRTM tiles and reproject them
gdalwarp -t_srs EPSG:32632 srtm_38_02.tif srtm_38_03.tif srtm_39_03.tif srtm_39_02.tif dem.tif
::Donwload nature reserves from OSM and copy all features which are multipolygons into a new file, so the new file contains one instead of 5 files only
@echo [out:xml][maxsize:2000000000];(way[boundary~"^(national_park|protected_area)"](48.803,7.3333,50.087,9.61215);way[leisure~"^(nature_reserve)"](48.803,7.3333,50.087,9.61215););(._;^>;);out; >queryReserve.txt
wget  -t 0 --post-file=queryReserve.txt http://overpass-api.de/api/interpreter --output-document=DownloadReserves.osm
ogr2ogr -sql "SELECT * FROM multipolygons" -t_srs EPSG:32632 -f GPKG Reserves.gpkg DownloadReserves.osm
:: delete all unnecessary files which were created during the process
del gadm36_DEU_gpkg.zip 
del gadm36_DEU.gpkg
del gadm36_DEUReprojected.gpkg
del RegionenSelect.gpkg
del DownloadRoads.osm
del DownloadRail.osm
del DownloadBuilding.osm
del DownloadLanduse.osm
del DownloadReserves.osm
del queryRail.txt
del queryBuildings.txt
del queryLanduse.txt
del queryRoad.txt
del queryReserve.txt
del buek250_mg_utm_v55.zip
del buek250_color.style
del buek250_mg_utm_v55.cpg
del buek250_mg_utm_v55.dbf
del buek250_mg_utm_v55.prj
del buek250_mg_utm_v55.sbn
del buek250_mg_utm_v55.sbx
del buek250_mg_utm_v55.shp
del buek250_mg_utm_v55.shp.xml
del buek250_mg_utm_v55.shx
del srtm_38_03.zip
del srtm_38_02.zip
del srtm_39_02.zip
del srtm_39_03.zip
del srtm_38_02.tif
del srtm_38_02.hdr
del srtm_38_02.tfw
del srtm_38_03.tif
del srtm_38_03.hdr
del srtm_38_03.tfw
del srtm_39_03.tif
del srtm_39_03.tfw
del srtm_39_03.hdr
del srtm_39_02.tif
del srtm_39_02.hdr
del srtm_39_02.tfw
del "Allgemeine Geschäftsbedingungen.pdf"
del "General Standard Terms and Conditions.pdf"
del license.txt
del Metadaten19139_buek250.pdf
del readme.txt
echo 0 thru 100 = 3 > DEM_rules.txt
echo 100 thru 200 = 4 >> DEM_rules.txt
echo 200 thru 300 = 3 >> DEM_rules.txt
echo 300 thru 500 = 2 >> DEM_rules.txt
echo 500 thru 700 = 1 >> DEM_rules.txt
echo * = 0 >> DEM_rules.txt
echo end >> DEM_rules.txt
echo cat 4 > Soil_rules.txt
echo where NRKART = '39' or NRKART = '40' or NRKART = '41' or NRKART = '42' or NRKART = '43' or NRKART = '61' >> Soil_rules.txt
echo cat 3 >> Soil_rules.txt
echo where NRKART = '25' or NRKART = '38' or NRKART = '44' or NRKART = '45' or NRKART = '51' or NRKART = '80' >> Soil_rules.txt
echo cat 2 >> Soil_rules.txt
echo where NRKART = '1' or NRKART = '2' or NRKART = '19' or NRKART = '26' or NRKART = '46' or NRKART = '47' or NRKART = '48' or NRKART = '54' or NRKART = '55' or NRKART = '56' or NRKART = '58' or NRKART = '59' or NRKART = '60' or NRKART = '62' or NRKART = '63' or NRKART = '65' or NRKART = '67' or NRKART = '68' or NRKART = '69' or NRKART = '72' or NRKART = '74' or NRKART = '76' or NRKART = '79' or NRKART = '82' or NRKART = '83' or NRKART = '84' or NRKART = '88' or NRKART = '89' or NRKART = '93' or NRKART = '94' or NRKART = '95' or NRKART = '96' >> Soil_rules.txt
echo cat 1 >> Soil_rules.txt
echo where NRKART = '3' or NRKART = '15' or NRKART = '16' or NRKART = '17' or NRKART = '18' or NRKART = '20' or NRKART = '21' or NRKART = '22' or NRKART = '23' or NRKART = '24' or NRKART = '27' or NRKART = '28' or NRKART = '29' or NRKART = '32' or NRKART = '37' or NRKART = '49' or NRKART = '50' or NRKART = '52' or NRKART = '53' or NRKART = '57' or NRKART = '64' or NRKART = '66' or NRKART = '70' or NRKART = '71' or NRKART = '75' or NRKART = '77' or NRKART = '78' or NRKART = '81' or NRKART = '85' or NRKART = '90' >> Soil_rules.txt
echo cat 5 > Landuse_rules.txt
echo where landuse = 'conservation' or landuse = 'gass' or landuse = 'gras' or landuse = 'grass' or landuse = 'greenfield' or landuse = 'meadow' or landuse = 'meadow_orchard' or landuse = 'orchard' or landuse = 'orchards_meadow' or landuse = 'pasture' or landuse = 'scrub' or landuse = 'scrubs' >> Landuse_rules.txt
echo cat 4 >> Landuse_rules.txt
echo where landuse = 'agricultural' or landuse = 'agriculture' or landuse = 'apiary' or landuse = 'brownfield' or landuse = 'deer preserve' or landuse = 'excercise_area' or landuse = 'farmland'  or landuse = 'farmyard' or landuse = 'field' or landuse = 'field_block' or landuse = 'flowerbed' or landuse = 'garden' or landuse = 'hedge' or landuse = 'leisure' or landuse = 'park' or landuse = 'recreation_ground' or landuse = 'village green' or landuse = 'village_green' >> Landuse_rules.txt
echo cat 3 >> Landuse_rules.txt
echo where landuse = 'animal' or landuse = 'animal_keeping' or landuse = 'dyke' or landuse = 'plant_nursery'  or landuse = 'proposed' or landuse = 'proving_ground' or landuse = 'range' or landuse = 'timber_yard' or landuse = 'urban_green' or landuse = 'vineyard' or landuse = 'young_forest_plantation' >> Landuse_rules.txt
echo cat 2 >> Landuse_rules.txt
echo where landuse = 'animal_enclosure' or landuse = 'cultural' or landuse = 'forest' or landuse = 'outdoor_seating' or landuse = 'piste' or landuse = 'quarry' or landuse = 'Reitplatz' or landuse = 'woodland' >> Landuse_rules.txt
echo cat 1 >> Landuse_rules.txt
echo where landuse = '*' or landuse = '1' or landuse = 'area' or landuse = 'm#' or landuse = 'n' or landuse = 'o' or landuse = 's' or landuse = 'yes' >> Landuse_rules.txt
echo cat 4 > Size_rules.txt
echo where AreaSize ^> 15000000 >> Size_rules.txt
echo cat 3 >> Size_rules.txt
echo where AreaSize BETWEEN 10000000 and 15000000 >> Size_rules.txt
echo cat 2 >> Size_rules.txt
echo where AreaSize BETWEEN 5000000 and 10000000 >> Size_rules.txt
echo cat 1 >> Size_rules.txt
echo where AreaSize BETWEEN 1000000 and 5000000 >> Size_rules.txt
echo cat 99 >> Size_rules.txt
echo where AreaSize ^< 1000000 >> Size_rules.txt