import matplotlib.pyplot as plt
import pyvista as pv
import trimesh
import numpy as np


def char2svg(char):
    plt.figure(figsize=(4, 4))
    plt.text(0.5, 0.5, char[0], fontsize=200, ha='center', va='center')
    plt.axis('off')
    path='./images/'+char[0]+'.svg'
    plt.savefig(path, format='svg')
    # plt.show()

    return path

def extrude_svg_to_obj(svg_file, distance, output_obj_file):
    mesh = trimesh.load(svg_file)

    extruded_mesh = mesh.extrude(distance)

    # extruded_mesh[1].apply_translation([0,0,0]) << This is a translation example
    extruded_mesh[1].export(output_obj_file, file_type='obj')

    mesh = pv.read(output_obj_file)
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


if __name__=='__main__':

    char = input("Letter: ")
    path = char2svg(char) #parte interna (arcilla)
   #path2 = expand_svg() << cubierta externa (plastico)
   #path3 = expand_svg() << cubierta base (plastico)

## PSEUDO OPERATIONS ##    
    # clay_volume = extrude_svg_to_obj(path,10,'./models/'+char+'.obj')
    # points = localize_disconected((clay_volume))
    # cutter_volume = extrude_svg_to_obj(path2,10,'./models/'+char+'.obj')
    # base_volume = extrude_svg_to_obj(path3,10,'./models/'+char+'.obj')
    # suports = voronoi_lines(points).extrude
    # base_volume = diff(base_volume,cutter_volume)
    # base_volume = slice(base_volume,base_height)
    # cutter_volume = diff(cutter_volume,clay_volume)
    # final_model = join(base_volume,cutter_volume,suports)/