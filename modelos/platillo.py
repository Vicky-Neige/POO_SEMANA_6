from modelos.producto import Producto

class Platillo(Producto):
    def __init__(self, nombre: str, precio: float, disponible: bool, tiempo_preparacion: int):
        super().__init__(nombre, precio, disponible)
        self.tiempo_preparacion: int = tiempo_preparacion  

    def mostrar_informacion(self) -> str:
        info_padre = super().mostrar_informacion()
        return f"{info_padre} | Tiempo Prep: {self.tiempo_preparacion} min"