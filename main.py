import matplotlib.pyplot as plt
import pyvista as pv
import trimesh
import numpy as np


def char2svg(char):
    plt.figure(figsize=(4, 4))
    plt.text(0.5, 0.5, char[0], fontsize=200, ha='center', va='center')
    plt.axis('off')
    file_path='./images/'+char[0]+'.svg'
    plt.savefig(file_path, format='svg', bbox_inches='tight', pad_inches=0)
    # plt.show()

    return path

def extrude_svg_to_obj(svg_file, distance, output_obj_file):
    mesh = trimesh.load(svg_file)

    z_min, z_max = mesh.bounds

    extruded_mesh = mesh.extrude(distance)

    extruded_mesh[1].apply_translation([0,0,0])

    extruded_mesh[1].export(output_obj_file, file_type='obj')

    mesh = pv.read(output_obj_file)
    plotter = pv.Plotter()
    plotter.add_mesh(mesh)
    plotter.add_axes()
    plotter.show()


if __name__=='__main__':

    char = input("Letter: ")
    path=char2svg(char)
    extrude_svg_to_obj(path,1,'./models/'+char+'.obj')
