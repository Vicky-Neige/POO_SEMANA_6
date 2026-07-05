from modelos.producto import Producto

class Bebida(Producto):
    def __init__(self, nombre: str, precio: float, disponible: bool, volumen_ml: int):
        super().__init__(nombre, precio, disponible)
        self.volumen_ml: int = volumen_ml  

    def mostrar_informacion(self) -> str:
        info_padre = super().mostrar_informacion()
        return f" {info_padre} | Tam: {self.volumen_ml} ml"