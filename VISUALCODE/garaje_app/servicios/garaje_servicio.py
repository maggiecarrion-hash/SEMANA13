from modelos.vehiculo import Vehiculo

class GarajeServicio:
	def __init__(self):
		self._vehiculos = []

	def registrar_unidad(self, placa, marca, tipo, capacidad, propietario):
		nueva_unidad = Vehiculo(placa, marca, tipo, capacidad, propietario)
		self._vehiculos.append(nueva_unidad)
		return nueva_unidad

	def obtener_unidades(self):
		return self._vehiculos
