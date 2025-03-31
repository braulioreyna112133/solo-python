def modificar_con_memoryview():
    datos = bytearray(b"Pythonista")  # Creamos un bytearray
    print("Antes:", datos)

    vista = memoryview(datos)  # Creamos la vista de memoria
    vista[6:9] = b"XYZ"  # Modificamos una parte del bytearray sin copiarlo
    
    print("Después:", datos)

# Ejecutar la función
modificar_con_memoryview()
    