from servicios.restaurante import Restaurante
from modelos.platillo import Platillo
from modelos.bebida import Bebida

def ejecutar_sistema():
    
    mi_restaurante = Restaurante("El Buen Sabor")

    print("==========================================================")
    print("       SISTEMA DE GESTIÓN DE RESTAURANTE YUMIT            ")
    print("==========================================================")

    platillo1 = Platillo("Encebollado Mixto", 3.50, True, 15)  
    platillo2 = Platillo("Ceviche de Camarón", 2.00, True, 12)  
    
    bebida1 = Bebida("Jugos Naturales", 1.50, True, 400)      
    bebida2 = Bebida("Agua Mineral", 1.00, True, 500)        

    print("\n--- [PRUEBA DE CONTROL] Validación de Seguridad del Precio---")
    
    platillo1.cambiar_precio(-1.00)  
    
    platillo1.cambiar_precio(3.75)   

    mi_restaurante.agregar_producto(platillo1)
    mi_restaurante.agregar_producto(platillo2)
    mi_restaurante.agregar_producto(bebida1)
    mi_restaurante.agregar_producto(bebida2)

    mi_restaurante.mostrar_carta()
    
    print("\n ¡Muchas gracias por usar el sistema, completada con éxito.\n")

if __name__ == "__main__":
    ejecutar_sistema()