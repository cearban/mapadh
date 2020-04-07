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
import gdal
from gdalconst import *

def compute_vertical_scale(min_x,min_y,max_x,max_y,min_z,max_z):
    """
        compute the vertical scale of elevation values in the terrain coverage
    """
    print "min_x: " , min_x
    print "min_y: " , min_y
    print "max_x: " , max_x
    print "max_y: " , max_y
    print "min_z: " , min_z
    print "max_z: " , max_z
    scale = (max_z - min_z) / (0.5 * math.sqrt( ((max_x - min_x) * (max_x - min_x)) + ((max_y - min_y) * (max_y - min_y)) ))
    # scale = 0.123885108064
    print "scale: " , scale 
    return scale

class mbr:
    """
        representation of an MBR
    """        
    def __init__(self,min_x,min_y,max_x,max_y):
        self.min_x = min_x
        self.min_y = min_y
        self.max_x = max_x
        self.max_y = max_y

    def __str__(self):
        return (str(self.min_x) + ',' + str(self.min_y) + ',' + str(self.max_x) + ',' + str(self.max_y))

class coord:
    """ 
        representation of a coord
    """    
    def __init__(self,x,y):
        self.x = x
        self.u = y
        
class camera:
    """
        representation of a camera in pov-ray sdl
    """    
    def __init__(self):
        self.location = ['','','']
        self.look_at = ['','','']

    def set_location(self,location_x,location_z,location_y):
        self.location[0] = location_x
        self.location[1] = location_z
        self.location[2] = location_y

    def set_lookat_pos(self,lookat_x,lookat_y,lookat_z):
        self.look_at[0] = lookat_x
        self.look_at[1] = lookat_y
        self.look_at[2] = lookat_z
        
    def __str__(self):
        out_str = 'camera {\n' + 'location <' + self.location[0] + ',' + self.location[1] + ',' + self.location[2] + '>\n'
        out_str = out_str + 'look_at <' + self.look_at[0] + ',' + self.look_at[1] + ',' + self.look_at[2] + '>\n}'
        return out_str
        
class light_source:
    """
        representation of a light source in pov-ray sdl
    """    
    def __str__(self):
        out_str = 'light_source\n { \n <0, 3000, 0> color <1,1,1>\n}'
        return out_str

class height_field:
    """
        representation of a height field in pov-ray sdl        
    """    
    def __init__(self,hf_source_image,overlay_image,z_scale):
        self.height_field_raster = hf_source_image
        self.topo_overlay = overlay_image
        self.z_scale = z_scale
        
    def __str__(self):
        out_str = 'height_field {\n'
        out_str = out_str + 'gif "'
        out_str = out_str + self.height_field_raster
        out_str = out_str + '"\n smooth \n pigment {\n'
        out_str = out_str + 'image_map {\n png "'
        out_str = out_str + self.topo_overlay
        out_str = out_str + '"\n interpolate 2 \n once \n } \n'
        out_str = out_str + 'rotate <90, 0, 0>\n }\n scale <1,'
        out_str = out_str + self.z_scale
        out_str = out_str + ', 1>\n }'
        return out_str
    
class povray_scene:
    """
        representation of a scene in pov-ray sdl
    """    
    def __init__(self):
        self.light_source = light_source()
    
    def add_camera(self,camera):
        self.camera = camera

    def add_light_source(self,light_source):
        self.light_source = light_source

    def add_height_field(self,height_field):
        self.height_field = height_field
    
    def __str__(self):
        return str(self.camera) + str(self.light_source) + str(self.height_field)

def render_2_5D_scene(min_x,min_y,max_x,max_y,overlay_type,look_dir,scene_name, min_z, max_z):


    working_dir = 'D:\\tmp\\'
    scene_def_filename = 'digimap_scene.pov'
    output_scene_filename = scene_name + '.png'

  #  starttime = time.time() 
    
  #  aoi = str(min_x) + ',' + str(min_y) + ',' + str(max_x) + ',' + str(max_y) 

    # ogc wcs request to grab dtm
  #  wcs_request_str = 'http://129.215.169.69:666/cgi-bin/mapserv.exe?map=os_profile_dtm_wcs_b.map&SERVICE=WCS&VERSION=1.0.0&REQUEST=GetCoverage&COVERAGE=os_dem&CRS=EPSG:27700&BBOX=' + aoi + '&WIDTH=500&HEIGHT=500&FORMAT=image/tif'

    # ogc wms requestto grab overlay map   
  #  edina_os_50k_wms_str = 'http://canisp.edina.ac.uk:7992/cgi-mapserv/mapserv?map=mapfiles/os/WMS_OS_Raster_50k.map&SERVICE=WMS&VERSION=1.1.1&REQUEST=GetMap&LAYERS=Raster_50k&SRS=EPSG:27700&BBOX=' + aoi +'&WIDTH=1000&HEIGHT=1000&FORMAT=png'
  #  edina_os_10k_wms_str = 'http://canisp.edina.ac.uk:7992/cgi-mapserv/mapserv?map=mapfiles/os/WMS_OS_Raster_10k.map&SERVICE=WMS&VERSION=1.1.1&REQUEST=GetMap&LAYERS=Raster_10k&SRS=EPSG:27700&BBOX=' + aoi +'&WIDTH=1000&HEIGHT=1000&FORMAT=png'
  #  edina_bgs_50k_wms_str = 'http://canisp.edina.ac.uk:7992/cgi-mapserv/mapserv?map=mapfiles/bgs/Geology_Maps_50k.map&SERVICE=WMS&VERSION=1.1.1&REQUEST=GetMap&LAYERS=bgs50k&SRS=EPSG:27700&BBOX=' + aoi + '&WIDTH=1000&HEIGHT=1000&FORMAT=png'

   # if overlay_type == 'os_10k_topo':
   #     wms_request_str = edina_os_10k_wms_str

    # if overlay_type == 'os_50k_topo':
    #    wms_request_str = edina_os_50k_wms_str

    # if overlay_type == 'bgs_50k_geol':
    #    wms_request_str = edina_bgs_50k_wms_str

    # from mapserver wcs grab a float32 geotiff 
    # dem = urllib.URLopener()
    # dem.retrieve(wcs_request_str,(working_dir + 'dem_from_wcs.tif'))        
    # got_wcs = time.time()
    # wcsinterval = got_wcs - starttime

    # from mapserver wms we grab a png to overlay
    # overlay = urllib.URLopener()
    # overlay.retrieve(wms_request_str,(working_dir + 'map_overlay_from_wms.png'))

    # got_wms = time.time()
    # wmsinterval = got_wms - got_wcs
   
    # run gdalinfo to compute statistics - we need these later on to compute vertical scale
   # cmd = '"D:/FWTools2.4.7/bin/gdalinfo.exe" ' + ' -stats ' + ' D:/tmp/dem_from_wcs.tif'
   # os.system(cmd)
    
    # use gdal api to grab min/max values from dem tif
    # alternative to using gdal api would be to parse the xml created when we run gdalinfo
    # gdal_dataset = gdal.Open((working_dir + 'dem_from_wcs.tif'), GA_ReadOnly)
    # band_1 = gdal_dataset.GetRasterBand(1)
    # min_z = band_1.GetMinimum()
    # max_z = band_1.GetMaximum()

   
    # run gdal_translate to convert the geotiff from the wcs to a scaled heightmap gif
    # so all values will be put into bins between 0 and 255
   # cmd = '"D:\FWTools2.4.7/bin/gdal_translate.exe"' + ' -of GIF -scale ' + 'D:/tmp/dem_from_wcs.tif D:/tmp/dem_from_wcs.gif'
   # os.system(cmd)


    # compute the vertical scale     
    v_scale = compute_vertical_scale(min_x,min_y,max_x,max_y,min_z,max_z)

    # close the gdal dataset
    gdal_dataset = None


   # gdal_complete = time.time()
   # gdalinterval = gdal_complete - got_wms 
    
    # create a new pov-ray scene description file controlling the perspective rendering
    outpf = open((working_dir + scene_def_filename),'w')
    my_scene = povray_scene()

    # create a new camera and set look direction    
    my_camera = camera()

    if look_dir == 'ne':    
        my_camera.set_location('0','.5','0')

    if look_dir == 'se':        
        my_camera.set_location('0','.5','1')

    if look_dir == 'sw':
        my_camera.set_location('1','.5','1')

    if look_dir == 'nw':        
        my_camera.set_location('1','.5','0')

    # set where the camera looks
    my_camera.set_lookat_pos('.5','0','.5')
    my_scene.add_camera(my_camera)

    # create a new heightfield, setting the scale value to what we calculated above from the wcs tif
    my_height_field = height_field('dem_from_wcs.gif','map_overlay_from_wms.png',str(v_scale))
    my_scene.add_height_field(my_height_field)

    # write the .pov file to disk
    outpf.write(str(my_scene))
    outpf.close()

     # run pov-ray to render the scene based on the contents of the scene description file
    # we can tweek various options here

    # cmd = 'D:/Service_Delivery/3D/pvengine.exe /render ' + working_dir + scene_def_filename + ' +A +W800 +H800 -D +O' + working_dir + output_scene_filename + ' /exit'
    # os.system(cmd)
    
   
   # rendered = time.time()
   # renderinterval = rendered - wrote_scene

   # print 'wcs time: ', wcsinterval
   # print 'wms time: ', wmsinterval
   # print 'gdal time: ', gdalinterval
   # print 'sceneinterval: ', sceneinterval
   # print 'render time: ' , renderinterval

    
    # clean up - delete the xml file created by gdal for the tif grabbed from the wcs
    # we need to do this to ensure that gdalinfo always recomputes stats afresh
    os.remove((working_dir + 'dem_from_wcs.tif.aux.xml'))
    
    
def main():
    if len(sys.argv) == 10:
        min_x = sys.argv[1]
        min_y = sys.argv[2]
        max_x = sys.argv[3]
        max_y = sys.argv[4]
        overlay_type = sys.argv[5]
        look_dir = sys.argv[6]
        scene_name = sys.argv[7]
        min_z = sys.argv[8]
        max_z = sys.argv[9]
        
        render_2_5D_scene(int(min_x),int(min_y),int(max_x),int(max_y),overlay_type,look_dir,scene_name, int(min_z), int(max_z) )
    else:
        print 'usage perspectiveviewbuilder_v2.py min_x min_y max_x max_y overlay look_dir scene_name'
        
if __name__ == '__main__':
    main()

    



    






