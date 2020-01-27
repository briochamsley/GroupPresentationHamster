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