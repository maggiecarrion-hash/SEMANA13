import os

class Producto:
    def __init__(self, id_prod, nombre, cantidad, precio):
        self.id_prod = id_prod
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f"ID: {self.id_prod:5} | Nombre: {self.nombre:15} | Stock: {self.cantidad:5} | Precio: ${self.precio:8.2f}"

    def a_linea_texto(self):
        """Prepara el objeto para ser guardado como una fila en el archivo .txt"""
        return f"{self.id_prod},{self.nombre},{self.cantidad},{self.precio}\n"

class Inventario:
    def __init__(self, archivo="inventario.txt"):
        self.productos = {}
        self.nombre_archivo = archivo
        # Intentamos cargar los datos al instanciar la clase
        self.cargar_desde_archivo()

    def cargar_desde_archivo(self):
        """
        Lee el archivo de texto y reconstruye el diccionario.
        Maneja excepciones de archivos no encontrados o permisos.
        """
        try:
            # Si el archivo no existe, lo creamos preventivamente
            if not os.path.exists(self.nombre_archivo):
                with open(self.nombre_archivo, 'w', encoding='utf-8') as f:
                    pass 
                print(f"[INFO] Archivo '{self.nombre_archivo}' creado (nuevo inventario).")
                return

            with open(self.nombre_archivo, 'r', encoding='utf-8') as f:
                for linea in f:
                    if linea.strip():
                        # Dividir la línea por comas
                        id_p, nom, cant, prec = linea.strip().split(',')
                        # Crear el objeto y añadirlo al diccionario
                        self.productos[id_p] = Producto(id_p, nom, int(cant), float(prec))
            
            print(f"[ÉXITO] Se cargaron {len(self.productos)} productos desde el archivo.")

        except FileNotFoundError:
            print("[ERROR] No se encontró el archivo de inventario.")
        except PermissionError:
            print("[ERROR] No hay permisos para leer el archivo.")
        except ValueError:
            print("[ALERTA] El archivo contiene datos corruptos. Verifique el formato.")
        except Exception as e:
            print(f"[ERROR INESPERADO] {e}")

    def guardar_en_archivo(self):
        """Sobrescribe el archivo con la información actualizada de los productos."""
        try:
            with open(self.nombre_archivo, 'w', encoding='utf-8') as f:
                for p in self.productos.values():
                    f.write(p.a_linea_texto())
        except PermissionError:
            print("[ERROR] No se pudo guardar: Permiso denegado.")
        except Exception as e:
            print(f"[ERROR AL GUARDAR] {e}")

    def añadir_producto(self, producto):
        if producto.id_prod in self.productos:
            print(f"Error: El ID {producto.id_prod} ya existe.")
        else:
            self.productos[producto.id_prod] = producto
            self.guardar_en_archivo()
            print(f"Producto '{producto.nombre}' añadido exitosamente.")

    def actualizar_producto(self, id_prod, nueva_cant):
        if id_prod in self.productos:
            self.productos[id_prod].cantidad = nueva_cant
            self.guardar_en_archivo()
            print(f"Stock de ID {id_prod} actualizado.")
        else:
            print("Error: Producto no encontrado.")

    def eliminar_producto(self, id_prod):
        if id_prod in self.productos:
            eliminado = self.productos.pop(id_prod)
            self.guardar_en_archivo()
            print(f"Producto '{eliminado.nombre}' eliminado del archivo.")
        else:
            print("Error: El ID no existe.")

    def mostrar_inventario(self):
        if not self.productos:
            print("\n--- El inventario está vacío ---")
        else:
            print("\n" + "="*55)
            print(f"{'INVENTARIO ACTUAL':^55}")
            print("="*55)
            for p in self.productos.values():
                print(p)
            print("="*55)

def ejecutar_menu():
    sistema = Inventario()

    while True:
        print("\n GESTIÓN DE INVENTARIO PERMANENTE")
        print("1. Añadir nuevo producto")
        print("2. Actualizar cantidad")
        print("3. Eliminar producto")
        print("4. Ver inventario completo")
        print("5. Salir")
        
        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
            try:
                id_p = input("ID único: ")
                nombre = input("Nombre del producto: ")
                cantidad = int(input("Cantidad inicial: "))
                precio = float(input("Precio unitario: "))
                sistema.añadir_producto(Producto(id_p, nombre, cantidad, precio))
            except ValueError:
                print("[ERROR] Entrada inválida. Cantidad debe ser entero y precio decimal.")

        elif opcion == "2":
            id_p = input("ID del producto a modificar: ")
            try:
                nueva_cant = int(input("Nueva cantidad total: "))
                sistema.actualizar_producto(id_p, nueva_cant)
            except ValueError:
                print("[ERROR] La cantidad debe ser un número.")

        elif opcion == "3":
            id_p = input("ID del producto a eliminar: ")
            sistema.eliminar_producto(id_p)

        elif opcion == "4":
            sistema.mostrar_inventario()

        elif opcion == "5":
            print("Cerrando sistema. ¡Hasta pronto!")
            break
        else:
            print("Opción no válida, intente de nuevo.")

if __name__ == "__main__":
    ejecutar_menu()