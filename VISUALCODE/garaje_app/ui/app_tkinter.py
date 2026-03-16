import tkinter as tk
from tkinter import ttk, messagebox

class AppGaraje:
	def __init__(self, root, servicio):
		self.root = root
		self.servicio = servicio
		self.root.title("Gestión de Garaje - Transporte Pesado")
		self.root.geometry("750x500")

		frame = tk.LabelFrame(root, text=" Registro de Unidades ", padx=15, pady=15)
		frame.pack(padx=10, pady=10, fill="x")

		tk.Label(frame, text="Placa:").grid(row=0, column=0, sticky="w")
		self.ent_placa = tk.Entry(frame)
		self.ent_placa.grid(row=0, column=1, padx=5, pady=5)

		tk.Label(frame, text="Marca:").grid(row=0, column=2, sticky="w")
		self.ent_marca = tk.Entry(frame)
		self.ent_marca.grid(row=0, column=3, padx=5, pady=5)

		tk.Label(frame, text="Tipo:").grid(row=1, column=0, sticky="w")
		self.ent_tipo = tk.Entry(frame)
		self.ent_tipo.grid(row=1, column=1, padx=5, pady=5)

		tk.Label(frame, text="Capacidad (Ton):").grid(row=1, column=2, sticky="w")
		self.ent_cap = tk.Entry(frame)
		self.ent_cap.grid(row=1, column=3, padx=5, pady=5)

		tk.Label(frame, text="Propietario:").grid(row=2, column=0, sticky="w")
		self.ent_prop = tk.Entry(frame, width=30)
		self.ent_prop.grid(row=2, column=1, columnspan=2, padx=5, pady=10, sticky="w")

		tk.Button(frame, text="Registrar", command=self.guardar, bg="green", fg="white").grid(row=2, column=3)

		self.tabla = ttk.Treeview(root, columns=("PL", "MA", "TI", "CA", "PR"), show="headings")
		self.tabla.heading("PL", text="Placa"); self.tabla.heading("MA", text="Marca")
		self.tabla.heading("TI", text="Tipo"); self.tabla.heading("CA", text="Ton"); self.tabla.heading("PR", text="Propietario")
		self.tabla.pack(padx=10, pady=10, fill="both", expand=True)

	def guardar(self):
		p, m, t, c, pr = self.ent_placa.get(), self.ent_marca.get(), self.ent_tipo.get(), self.ent_cap.get(), self.ent_prop.get()
		if all([p, m, t, c, pr]):
			self.servicio.registrar_unidad(p, m, t, c, pr)
			self.actualizar_tabla()
			self.limpiar()
		else:
			messagebox.showwarning("Error", "Complete todos los campos")

	def actualizar_tabla(self):
		self.tabla.delete(*self.tabla.get_children())
		for v in self.servicio.obtener_unidades():
			self.tabla.insert("", "end", values=(v.placa, v.marca, v.tipo, f"{v.capacidad} Ton", v.propietario))

	def limpiar(self):
		for e in [self.ent_placa, self.ent_marca, self.ent_tipo, self.ent_cap, self.ent_prop]: e.delete(0, "end")
