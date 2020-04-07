camera {
location <0,.5,0>
look_at <.5,0,.5>
}light_source
 { 
 <0, 3000, 0> color <1,1,1>
}height_field {
gif "dem_from_wcs.gif"
 smooth 
 pigment {
image_map {
 png "map_overlay_from_wms.png"
 interpolate 2 
 once 
 } 
rotate <90, 0, 0>
 }
 scale <1,0.123885108064, 1>
 }