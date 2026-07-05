class Restaurante:
    def __init__(self, nombre_establecimiento: str):
        self.nombre_establecimiento: str = nombre_establecimiento
        self.lista_productos: list = [] 

    def agregar_producto(self, producto) -> None:
        self.lista_productos.append(producto)

    def mostrar_carta(self) -> None:
        print(f"\n======= CARTA DE {self.nombre_establecimiento.upper()} =======")
        if not self.lista_productos:
            print("La carta se encuentra vacía por el momento.")
            return

        for producto in self.lista_productos:
            print(producto.mostrar_informacion())
        print("==================================================")