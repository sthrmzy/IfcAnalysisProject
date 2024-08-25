import pyvista as pv

def visualizar_obj(file_path):
    mesh = pv.read(file_path)
    plotter = pv.Plotter()
    plotter.add_mesh(mesh, color='white', show_edges=True)
    plotter.set_background('black')
    plotter.show()

if __name__ == "__main__":
    file_path = 'data/casa.obj'
    visualizar_obj(file_path)
