import matplotlib.pyplot as plt
import pyvista as pv
import trimesh
import numpy as np


def char2svg(char):
    plt.figure(figsize=(4, 4))  # Tamaño de la figura
    plt.text(0.5, 0.5, char[0], fontsize=200, ha='center', va='center')  # Ajustes del texto
    plt.axis('off')  # Ocultar los ejes
    filename=char[0]+'.svg'
    plt.savefig(filename, format='svg', bbox_inches='tight', pad_inches=0)  # Guardar la ilustración en formato SVG
    # plt.show()

    return filename

def extrude_svg_to_obj(svg_file, distance, output_obj_file):
    # Cargar el archivo SVG utilizando trimesh
    mesh = trimesh.load(svg_file)

    # Obtener los límites del modelo en el eje z
    z_min, z_max = mesh.bounds

    # Crear una nueva malla extruida a lo largo del eje z
    extruded_mesh = mesh.extrude(distance)

    # Mover la malla extruida para que el límite inferior coincida con el límite original
    extruded_mesh[1].apply_translation([0,0,0])

    # Guardar la malla extruida como un archivo OBJ
    extruded_mesh[1].export(output_obj_file, file_type='obj')

    mesh = pv.read(output_obj_file)
    plotter = pv.Plotter()
    plotter.add_mesh(mesh)
    plotter.add_axes()
    plotter.show()


if __name__=='__main__':

    # char = input("Ingrese un carácter: ")
    char = 'B'
    filename=char2svg(char)
    extrude_svg_to_obj(filename,1,char+'_3d.obj')
