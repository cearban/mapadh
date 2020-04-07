"""
render a perspective view of a map created from a wcs & wms data source

povray is used to do the 3d rendering & needs to be installed somewhere
we also need gdal & it`s python bindings installed

example useage:

python perspectiveviewbuilder.py 326000 671500 328500 674000 bgs_50k_geol ne my_bgs_50k_scene

creates a png scene looking NE showing holyrood park & bgs geology map draped over os terrain 

python perspectiveviewbuilder.py 326000 671500 328500 674000 os_10k_topo ne my_os_10k_scene

creates a png scene looking NE showing holyrood park & os 10k topo map draped over os terrain

python perspectiveviewbuilder_v2.py 320000 660000 325000 665000 os_50k_topo ne my_os_50k_scene

creates a png scene lookin NE over the pentland hill/penecuik & os 50k topo map draped over os terrain

@ moment the wcs only has 1:10k Profile DTM data for OS grid square NT

"""


import os
import sys
import urllib
import math
import time


def render_2_5D_scene(min_x,min_y,max_x,max_y,overlay_type,look_dir,scene_name,workdir):
    working_dir = workdir
   
    starttime = time.time() 
    
    aoi = str(min_x) + ',' + str(min_y) + ',' + str(max_x) + ',' + str(max_y) 

    # ogc wcs request to grab dtm
    wcs_request_str = 'http://129.215.169.69:666/cgi-bin/mapserv.exe?map=os_profile_dtm_wcs_b.map&SERVICE=WCS&VERSION=1.0.0&REQUEST=GetCoverage&COVERAGE=os_dem&CRS=EPSG:27700&BBOX=' + aoi + '&WIDTH=500&HEIGHT=500&FORMAT=image/tif'

    # ogc wms requestto grab overlay map   
    edina_os_50k_wms_str = 'http://canisp.edina.ac.uk:7992/cgi-mapserv/mapserv?map=mapfiles/os/WMS_OS_Raster_50k.map&SERVICE=WMS&VERSION=1.1.1&REQUEST=GetMap&LAYERS=Raster_50k&SRS=EPSG:27700&BBOX=' + aoi +'&WIDTH=1000&HEIGHT=1000&FORMAT=png'
    edina_os_10k_wms_str = 'http://canisp.edina.ac.uk:7992/cgi-mapserv/mapserv?map=mapfiles/os/WMS_OS_Raster_10k.map&SERVICE=WMS&VERSION=1.1.1&REQUEST=GetMap&LAYERS=Raster_10k&SRS=EPSG:27700&BBOX=' + aoi +'&WIDTH=1000&HEIGHT=1000&FORMAT=png'
    edina_bgs_50k_wms_str = 'http://canisp.edina.ac.uk:7992/cgi-mapserv/mapserv?map=mapfiles/bgs/Geology_Maps_50k.map&SERVICE=WMS&VERSION=1.1.1&REQUEST=GetMap&LAYERS=bgs50k&SRS=EPSG:27700&BBOX=' + aoi + '&WIDTH=1000&HEIGHT=1000&FORMAT=png'

    if overlay_type == 'os_10k_topo':
        wms_request_str = edina_os_10k_wms_str

    if overlay_type == 'os_50k_topo':
        wms_request_str = edina_os_50k_wms_str

    if overlay_type == 'bgs_50k_geol':
        wms_request_str = edina_bgs_50k_wms_str

    # from mapserver wcs grab a float32 geotiff 
    dem = urllib.URLopener()
    dem.retrieve(wcs_request_str,(working_dir + 'dem_from_wcs.tif'))        
    got_wcs = time.time()
    wcsinterval = got_wcs - starttime

    # from mapserver wms we grab a png to overlay
    overlay = urllib.URLopener()
    overlay.retrieve(wms_request_str,(working_dir + 'map_overlay_from_wms.png'))

    got_wms = time.time()
    wmsinterval = got_wms - got_wcs

    print 'wcs time: ', wcsinterval
    print 'wms time: ', wmsinterval
       
    
    
def main():
    if len(sys.argv) == 9:
        min_x = sys.argv[1]
        min_y = sys.argv[2]
        max_x = sys.argv[3]
        max_y = sys.argv[4]
        overlay_type = sys.argv[5]
        look_dir = sys.argv[6]
        scene_name = sys.argv[7]
        workdir = sys.argv[8]
        render_2_5D_scene(int(min_x),int(min_y),int(max_x),int(max_y),overlay_type,look_dir,scene_name,workdir)
    else:
        print 'usage perspectiveviewbuilder_v2.py min_x min_y max_x max_y overlay look_dir scene_name workdir'
        
if __name__ == '__main__':
    main()

    



    






