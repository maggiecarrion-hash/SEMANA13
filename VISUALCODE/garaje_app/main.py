import tkinter as tk
from servicios.garaje_servicio import GarajeServicio
from ui.app_tkinter import AppGaraje

if __name__ == "__main__":
	root = tk.Tk()
	# Conectamos la lógica profesional con la ventana
	servicio = GarajeServicio()
	app = AppGaraje(root, servicio)
	root.mainloop()
