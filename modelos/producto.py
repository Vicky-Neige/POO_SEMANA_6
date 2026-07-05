class Producto:
    def __init__(self, nombre: str, precio: float, disponible: bool):
        self.nombre: str = nombre
        self.__precio: float = 0.0  
        self.cambiar_precio(precio)  
        self.disponible: bool = disponible

    def obtener_precio(self) -> float:
        return self.__precio

    def cambiar_precio(self, nuevo_precio: float) -> None:
        if nuevo_precio > 0:
            self.__precio = nuevo_precio
        else:
            print(f" Error: El precio para '{self.nombre}' debe ser mayor a cero. No se aplicó el cambio.")

    def mostrar_informacion(self) -> str:
        estado = "Disponible" if self.disponible else "Agotado"
        return f"Producto: {self.nombre} | Precio: ${self.__precio:.2f} | Estado: {estado}"