"""
render a perspective view of a map created from a wcs & wms data source

povray is used to do the 3d rendering & needs to be installed somewhere

example useage:

python perspectiveviewbuilder.py 326000 671500 328500 674000 bgs_geol ne

creates a png scene looking NE showing holyrood park & bgs geology map draped over os terrain 

python perspectiveviewbuilder.py 326000 671500 328500 674000 os_topo ne

creates a png scene looking NE showing holyrood park & os 10k topo map draped over os terrain 

@ moment the wcs only has 1:10k Profile DTM data for OS grid square NT

"""

import os
import sys
import urllib

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

def render_2_5D_scene(aoi_min_x,aoi_min_y,aoi_max_x,aoi_max_y,overlay,look_dir):
    dem_filename = 'digimap_src_dem.gif'
    topo_map_filename = 'digimap_topo_map.png'
    scene_def_filename = 'digimap_scene.pov'
    output_scene_filename = 'digimap_perspective_view.png'
    min_x,min_y,max_x,max_y = aoi_min_x,aoi_min_y,aoi_max_x,aoi_max_y
    scene_aoi = mbr(min_x,min_y,max_x,max_y)    
    dem_res = 10
    working_dir = 'D:\\tmp\\'

    wcs_cover_width = (max_x - min_x) / dem_res
    wcs_cover_height =  (max_y - min_y) / dem_res

    # OGC WCS GetCoverage() request to retrive terrain coverage from jrcc OS 10k Profile DEM 
    wcs_request_str = 'http://129.215.169.69:666/cgi-bin/mapserv.exe?map=os_profile_dtm_wcs_b.map&SERVICE=WCS&VERSION=1.0.0&REQUEST=GetCoverage&COVERAGE=os_dem&CRS=EPSG:27700&BBOX=' + str(scene_aoi) + '&WIDTH=' + str(wcs_cover_width) + '&HEIGHT=' + str(wcs_cover_height) + '&FORMAT=image/gif'    

    # OGC WMS GetMap() request to retrieve OS 10k map from EDINA MapServer instance
    edina_os_10k_raster_wms = 'http://canisp.edina.ac.uk:7992/cgi-mapserv/mapserv?map=mapfiles/os/WMS_OS_Raster_10k.map&SERVICE=WMS&VERSION=1.1.1&REQUEST=GetMap&LAYERS=Raster_10k&SRS=EPSG:27700&BBOX=' + str(scene_aoi) +'&WIDTH=1000&HEIGHT=1000&FORMAT=png'

    # OGC WMS GetMap() request to retrieve BGS 50k map from EDINA MapServer instance
    edina_bgs_50k_wms_str = 'http://canisp.edina.ac.uk:7992/cgi-mapserv/mapserv?map=mapfiles/bgs/Geology_Maps_50k.map&SERVICE=WMS&VERSION=1.1.1&REQUEST=GetMap&LAYERS=bgs50k&SRS=EPSG:27700&BBOX=' + str(scene_aoi) + '&WIDTH=1000&HEIGHT=1000&FORMAT=png'
    
    if overlay == 'os_topo':
        wms_request_str = edina_os_10k_raster_wms
        
    if overlay == 'bgs_geol':
        wms_request_str = edina_bgs_50k_wms_str
                         
    # retrive DEM image
    dem_image = urllib.URLopener()
    dem_image.retrieve(wcs_request_str,(working_dir + dem_filename))

    # retrieve topo overlay image
    topo_map_image = urllib.URLopener()
    topo_map_image.retrieve(wms_request_str,(working_dir + topo_map_filename))
        
    # create a new pov-ray scene description file controlling the perspective rendering
    outpf = open((working_dir + scene_def_filename),'w')
    my_scene = povray_scene()

    # create a new camera in the scene, where the camera is and what it looks at
    # these are is 0>1 positions
    # we will need to have a conversion from rw to scene coordinates...

    my_camera = camera()

    # set camera location at LL looking down to middle of AOI

    if look_dir == 'ne':    
        my_camera.set_location('0','.5','0')

    if look_dir == 'se':        
        my_camera.set_location('0','.5','1')

    if look_dir == 'sw':
        my_camera.set_location('1','.5','1')

    if look_dir == 'nw':        
        my_camera.set_location('1','.5','0')

    my_camera.set_lookat_pos('.75','0','.75')
    my_scene.add_camera(my_camera)

    # add a heightfield to the scene with the surface defined by the retrieved dem
    # texture for the heightfield is the retrieved topo map from the WMS

    # we are using a vertical scale of .25
    
    my_height_field = height_field(dem_filename,topo_map_filename,'.2')
    my_scene.add_height_field(my_height_field)

    # write the pov-ray scene description file to disk
    outpf.write(str(my_scene))
    outpf.close()

    # run pov-ray to render the scene based on the contents of the scene description file
    # we can tweek various options here

    cmd = 'D:/Service_Delivery/3D/pvengine.exe /render ' + working_dir + scene_def_filename + ' +A +W800 +H800 +O' + working_dir + output_scene_filename + ' /exit'
    os.system(cmd)
    
def main():
    if len(sys.argv) == 7:
        min_x = sys.argv[1]
        min_y = sys.argv[2]
        max_x = sys.argv[3]
        max_y = sys.argv[4]
        overlay_type = sys.argv[5]
        look_dir = sys.argv[6]
        render_2_5D_scene(int(min_x),int(min_y),int(max_x),int(max_y),overlay_type,look_dir)
    else:
        print 'usage perspectiveviewbuilder.py min_x min_y max_x max_y overlay look_dir'
        
if __name__ == '__main__':
    main()
        
        
             