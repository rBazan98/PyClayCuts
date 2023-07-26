# ## PSEUDO OPERATIONS ##    
#     # points = localize_disconected((clay_volume))
#     # cutter_volume = extrude_svg_to_obj(path2,10,'./models/'+char+'.obj')
#     # base_volume = extrude_svg_to_obj(path3,10,'./models/'+char+'.obj')
#     # suports = voronoi_lines(points).extrude
#     # base_volume = diff(base_volume,cutter_volume)
#     # base_volume = slice(base_volume,base_height)
#     # cutter_volume = diff(cutter_volume,clay_volume)
#     # final_model = join(base_volume,cutter_volume,suports)/
#     print("")
#     pass


import matplotlib.pyplot as plt
from svgpathtools import svg2paths, svg2paths2, wsvg
from svgpathtools import Path, Line 
import pyvista as pv
import trimesh
# import numpy as np
# import drawsvg as draw
# import svgwrite
from textwrap import dedent
# import svg
# import os


def extrude_svg_to_obj(svg_file, distance, output="extruded.obj"):
    base = trimesh.load(svg_file)
    extruded_base = base.extrude(distance)
    extruded_base.export(output, file_type='obj')
    # extruded_mesh[1].apply_translation([0,0,0]) << This is a translation example

    mesh = pv.read(output)
    center_diff=list(map(lambda x: x*-1,mesh.center))
    mesh.translate(center_diff,inplace=True)
    
    # flip vertical axe towards positive y
    mesh.points[:,1] = - mesh.points[:,1]

    plotter = pv.Plotter()
    plotter.add_mesh(mesh)
    plotter.add_axes()
    plotter.show_grid()
    plotter.show()
    
    return mesh


def char2svg(char):

    plt.figure(figsize=(4, 4))
    plt.text(0.5, 0.5, char[0], fontsize=200, ha='center', va='center')
    plt.axis('off')
    filename='matplot.svg'
    # filename='matplot_'+char+'.svg'
    plt.savefig(filename, format='svg')
    
    return filename


def run():

    filename = char2svg('Q')
    paths, attr, svg_attr = svg2paths2(filename) 
    paths.pop(0); attr.pop(0);
    # for idx, path in enumerate(paths):
    #     paths[idx] = path.reversed()
    paths[0].normal()

    wsvg(paths, attributes=attr, svg_attributes=svg_attr, filename='svgtools.svg')

    # extrude_svg_to_obj("./examples/offset_codebase.svg",10)

if __name__=='__main__':
    run()

