def contador(nombre_archivo):
    # Inicializar contadores de letras y espacios
    contador_letras = 0
    contador_espacios = 0
    # Abrir el archivo en modo lectura
    with open(nombre_archivo, "r") as f:
        # Leer todo el contenido del archivo
        contenido = f.read()
        # Iterar sobre cada caracter en el contenido del archivo
        for caracter in contenido:
            # Verificar si el caracter es una letra
            if caracter.isalpha():
                contador_letras += 1  # Incrementar contador de letras
            # Verificar si el caracter es un espacio en blanco
            elif caracter.isspace():
                contador_espacios += 1  # Incrementar contador de espacios
    # Retornar la cantidad de letras y la cantidad de espacios contados
    return contador_letras, contador_espacios
# Nombre del archivo a procesar
nombre_archivo = "dato2.txt"
# Abrir el archivo para leer su contenido y calcular las estadísticas
with open(nombre_archivo, 'r') as archivo:
    contenido = archivo.read()  # Leer contenido completo del archivo
    # Llamar a la función contador para obtener las estadísticas
    total_letras, total_espacios = contador(nombre_archivo)
    # Imrimir las estadísticas obtenidas
    print("Cantidad de letras en el archivo:", total_letras)
    print("Cantidad de espacios en el archivo:", total_espacios)
# Imprimir el contenido del archivo
print("Contenido del archivo:")
print(contenido)
