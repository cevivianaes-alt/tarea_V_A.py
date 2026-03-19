"""
Sistema básico de gestión de tareas desarrollado en Python.

El programa permite registrar, visualizar, editar y marcar tareas
como completadas mediante un menú interactivo en consola.
"""

from datetime import datetime

tareas = []
contador_id = 1

def mostrar_menu_principal():
    print("\n--- Gestor de Tareas ---")
    print("1. Agregar tarea")
    print("2. Ver todas las tareas")
    print("3. Marcar tarea como completada")
    print("4. Ver tareas completadas")
    print("5. Editar tarea")
    print("6. Salir")

def agregar_tarea():
    """
    Solicita al usuario la información básica de una tarea y la registra
    en la lista principal del sistema.

    La función crea un diccionario que almacena los datos ingresados
    (título, descripción y prioridad), asigna un identificador único
    mediante un contador incremental y registra la fecha y hora de
    creación de la tarea.
    """
    global contador_id
    titulo = input("Ingrese el título de la tarea: ")
    descripcion = input("Ingrese la descripción de la tarea: ")
    prioridad = input("Ingrese la prioridad: ")
    
    tarea = {
        'id': contador_id,
        'titulo': titulo,
        'descripcion': descripcion,
        'prioridad': prioridad,
        'estado': 'pendiente',
        'fecha_creacion': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    
    tareas.append(tarea)
    contador_id += 1
    print("Tarea agregada correctamente")

def ver_tareas():
    """
    Muestra en pantalla todas las tareas registradas que se encuentran
    en la lista principal.

    Si no existen tareas almacenadas, el sistema informa al usuario que
    no hay registros disponibles. En caso contrario, se recorre la lista
    y se presentan los datos.
    """

    if not tareas:
        print("No hay tareas pendientes")
    else:
        for i, tarea in enumerate(tareas):
            print(f"{i + 1}. Título: {tarea['titulo']}, Descripción: {tarea['descripcion']}, Prioridad: {tarea['prioridad']}")
            
def completar_tarea():
    """
    Actualiza el estado de una tarea registrada dentro del gestor.
    La función permite seleccionar una tarea existente mediante su
    posición dentro de la lista principal y modificar su atributo
    de estado, indicando que la actividad ha sido finalizada.
    """
    ver_tareas()
    try:
        numero_tarea = int(input("Ingrese el número de la tarea que desea marcar como completada: "))
        if 1 <= numero_tarea <= len(tareas):
            tareas[numero_tarea - 1]['estado'] = 'completada'
            print("Tarea marcada como completada")
        else:
            print("Número de tarea inválido")
    except ValueError:
        print("Entrada inválida. Por favor, ingrese un número.")
        
def ver_tareas_completadas():
    """ 
    Presenta únicamente las tareas cuyo estado indica que han sido finalizadas.
    Para ello se realiza un filtrado sobre la colección principal de
    tareas, seleccionando los registros cuyo atributo 'estado'
    corresponde a "completada". Esto permite separar las actividades
    finalizadas de aquellas que continúan pendientes dentro del sistema.
    """

    completadas = [tarea for tarea in tareas if tarea.get('estado') == 'completada']
    if not completadas:
        print("No hay tareas completadas.")
    else:
        print("\n--- Tareas Completadas ---")
        for i, tarea in enumerate(completadas):
            print(f"{i + 1}. Título: {tarea['titulo']}, Descripción: {tarea['descripcion']}, Prioridad: {tarea['prioridad']}")

def eliminar_tarea():
    """
    Permite eliminar una tarea almacenada en el sistema.
    Primero se muestran las tareas registradas para que el usuario pueda
    identificar cuál desea eliminar. Luego se solicita el número de la
    tarea seleccionada y se valida que exista dentro del rango permitido.
    """

    ver_tareas()
    try:
        numero = int(input("Ingrese el número de la tarea que desea eliminar: "))
        if 1 <= numero <= len(tareas):
            confirmar = input("¿Está seguro de eliminar esta tarea? (s/n): ")   
            if confirmar.lower() == "s":
                tareas.pop(numero - 1)
                print("Tarea eliminada correctamente")
            else:
                print("Eliminación cancelada")
        else:
            print("Número inválido")     
    except ValueError:
        print("Entrada inválida")           

def editar_tarea():
    """
    Esta función permite modifica los datos asociados a una tarea previamente registrada.
    Una vez identificada la tarea dentro de la lista de almacenamiento,
    el sistema permite reemplazar ciertos atributos relevantes como
    título, descripción, prioridad o fecha límite. Esta operación
    permite actualizar la información de una tarea sin necesidad de
    eliminarla y volver a registrarla.
    """

    ver_tareas()
    try:
        numero = int(input("Ingrese el número de la tarea que desea editar: "))
        if 1 <= numero <= len(tareas):  
            tarea = tareas[numero - 1]
            nuevo_titulo = input("Nuevo título: ")
            nueva_descripcion = input("Nueva descripción: ")
            nueva_prioridad = input("Nueva prioridad: ")
            nueva_fecha = input("Nueva fecha límite: ")
            tarea["titulo"] = nuevo_titulo
            tarea["descripcion"] = nueva_descripcion
            tarea["prioridad"] = nueva_prioridad
            tarea["fecha_limite"] = nueva_fecha
            print("Tarea editada correctamente")
        else:
            print("Número inválido")
    except ValueError:
        print("Entrada inválida")

def main():
    """
    Estructura de control principal del programa.
    Mantiene activo el menú del gestor de tareas hasta que el usuario
    seleccione la opción de salir.
    """

    while True:
        mostrar_menu_principal()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_tarea()
        elif opcion == "2":
            ver_tareas()
        elif opcion == "3":
            completar_tarea()
        elif opcion == "4":
            ver_tareas_completadas()
        elif opcion == "5":
            editar_tarea()
        elif opcion == "6":
            print("Finalizado")
            break


if __name__ == "__main__":
    main()

    


    
