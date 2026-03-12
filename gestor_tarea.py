areas = []
contador_id = 1

tareas = []
def mostrar_menu_principal():
    print("\n--- Gestor de Tareas ---")
    print("1. Agregar tarea")
    print("2. Ver todas las tareas")
    print("3. Marcar tarea como completada")
    print("4. Ver tareas completadas")
    print("5. Salir")

def agregar_tarea():
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
    if not tareas:
        print("No hay tareas pendientes")
    else:
        for i, tarea in enumerate(tareas):
            print(f"{i + 1}. Título: {tarea['titulo']}, Descripción: {tarea['descripcion']}, Prioridad: {tarea['prioridad']}")
            
def completar_tarea():
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
    completadas = [tarea for tarea in tareas if tarea.get('estado') == 'completada']
    if not completadas:
        print("No hay tareas completadas.")
    else:
        print("\n--- Tareas Completadas ---")
        for i, tarea in enumerate(completadas):
            print(f"{i + 1}. Título: {tarea['titulo']}, Descripción: {tarea['descripcion']}, Prioridad: {tarea['prioridad']}")

def eliminar_tarea():
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
        print("Finalizado")
        break

    

