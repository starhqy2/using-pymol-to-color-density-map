from pymol.cmd import *

def msave(prefix="",frames="",width="0", height ="0",dpi = 150,ray=0,bg="white",ray_trace_mode="3"):
    bg_color(bg)
    #set("antialias", "2")
    #set("ray_trace_mode", ray_trace_mode)
    for i in range(1, int(frames)+1):
        frame(i)
        png(prefix + str(i).zfill(4),width, height, dpi, ray)
     #  s="s"+str(i)
     #   scene(s, "store")
     #   mview("store", scene=s)
extend("msave", msave)
        
    
    

