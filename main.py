import matplotlib.pyplot as plt
from svgpathtools import svg2paths, svg2paths2, wsvg

def char2paths(char): # Implement character with multiple path, maybe ussing parsing

    plt.figure(figsize=(4, 4))
    plt.text(0.5, 0.5, char[0], fontsize=200, ha='center', va='center')
    plt.axis('off')
    filename='.matplot'
    plt.savefig(filename, format='svg')
    plt.close()
    
    paths, _, _ = svg2paths2(filename)
    paths.pop(0)
    wsvg(paths, filename='svgtools.svg')
    
    return paths