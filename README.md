# using-pymol-to-color-density-map

Problem: Now, I have a viral density map (from Cryo-EM), then I want to color it in different colors from the centre to outside surface.


Solution:

assumption my density map name is HPV
First step, create a pseudoatom in the centre of the virus, the coordinate can be get when HPV loading.
##$isosurface HPV_surf, HPV*, level = 1.2
##$pseudoatom origin, pos = (454, 454, 454), label = origin
Second step, create a color ramp, which you can define the distance range and color range.
##$ramp_new ramp, origin, [240, 280], [white, warmapink]
Third step, apply color ramp to density map.
##$color ramp, HPV_surf
