# Sistema de Gestión de Restaurante - POO Semana 6

* **Nombre Completo del Estudiante:** Mayerli Melania Granda Quispe
* **Asignatura:** Programación Orientada a Objetos
* **MSc:** Kevin Bolívar Lascano Sánchez
* **Semestre:** Nivel II
* **Paralelo:** F
* **Institución:** Universidad Estatal Amazónica

---

## 1. Descripción del Sistema Desarrollado
Este sistema es una solución modular en Python diseñada para gestionar de forma eficiente los productos de la carta del restaurante "El Buen Sabor". Utilizando la Programación Orientada a Objetos (POO), el programa organiza de manera automatizada el catálogo de comidas y bebidas, facilitando la administración interna del menú mediante una estructura limpia y escalable.

---

## 2. Explicación de la Estructura del Proyecto
El proyecto se encuentra organizado rigurosamente bajo la arquitectura modular exigida por la cátedra, separando las responsabilidades de definición de objetos y los servicios lógicos de control:

```text
restaurante_app/
 ├── modelos/
 │   ├── __init__.py
 │   ├── producto.py      # Clase Padre que define las propiedades generales del menú.
 │   ├── platillo.py      # Clase Hija especializada en comidas y tiempos de preparación.
 │   └── bebida.py        # Clase Hija especializada en líquidos y volumen en mililitros.
 ├── servicios/
 │   ├── __init__.py
 │   └── restaurante.py   # Clase de servicio que administra la colección de productos.
 ├── main.py              # Punto de arranque, pruebas de control e instanciación de objetos.
 └── README.md            # Documentación del proyecto y estructura del sistema.