import matplotlib.pyplot as plt
from svgpathtools import svg2paths, svg2paths2, wsvg
# import pyvista as pv
# import trimesh
# import numpy as np
# import drawsvg as draw
# import svgwrite
from textwrap import dedent
# import svg
import os

# def extrude_svg_to_obj(svg_file, distance, output):
#     base = trimesh.load(svg_file)
#     extruded_base = base.extrude(distance)
#     extruded_base[1].export(output, file_type='obj')    # extruded_mesh[1].apply_translation([0,0,0]) << This is a translation example

#     mesh = pv.read(output)
#     center_diff=list(map(lambda x: x*-1,mesh.center))
#     mesh.translate(center_diff,inplace=True)
    
#     # flip vertical axe towards positive y
#     mesh.points[:,1] = - mesh.points[:,1]

#     plotter = pv.Plotter()
#     plotter.add_mesh(mesh)
#     plotter.add_axes()
#     plotter.show_grid()
#     plotter.show()
    
#     return mesh



# def run():
#     char = input("Letter: ")
#     path = char2svg(char) #parte interna (arcilla)
#     #path2 = expand_svg() << cubierta externa (plastico)
#     #path3 = expand_svg() << cubierta base (plastico)
#     #path4? 

#     clay_volume = extrude_svg_to_obj(path,10,'./models/'+char+'.obj')


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

# def create_offset(svg_path, offset_distance, output_path):
#     # Load the SVG file
#     dwg = svgwrite.Drawing(svg_path)

#     # Create a new SVG figure with an offset
#     offset_drawing = dwg.g()
#     for element in dwg.elements:
#         if isinstance(element, svgwrite.path.Path):
#             offset_path = element.offset(offset_distance)
#             offset_drawing.add(offset_path)

#     # Save the offset SVG file
#     dwg.add(offset_drawing)
#     dwg.saveas(output_path)


def char2svg(char):

    plt.figure(figsize=(4, 4))
    plt.text(0.5, 0.5, char[0], fontsize=200, ha='center', va='center')
    plt.axis('off')
    filename='matplot.svg'
    # filename='matplot_'+char+'.svg'
    plt.savefig(filename, format='svg')
    
    return filename


if __name__=='__main__':

    filename = char2svg('%')
    paths, attr, svg_attr = svg2paths2(filename) 
    paths.pop(0); attr.pop(0);
    wsvg(paths, attributes=attr, svg_attributes=svg_attr, filename='svgtools.svg')