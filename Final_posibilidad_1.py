import csv  #SE IMPORTA EL MODULO

def leer_archivo_csv(): #SE CREA UNA FUNCION PARA LEER EL ARCHIVO CSV JUNTO A UN BLOQUE PARA CAPTURAR ERRORES
    try:
        with open('recursosPython.csv', 'r') as archivo: #SE ABRE EL ARCHIVO EN MODO LECTURA Y SE DENOMINA COMO ARCHIVO
            print("\n/// LEYENDO ARCHIVO CSV ///")
            lector = csv.reader(archivo, delimiter=';') #EL LECTOR POSEE UN DELIMITADOR PARA QUE ENTIENDA QUE CADA DATOS ESTA SEPARADO DE UN ;
            next(lector)  # SE SALTEA LA PRIMER FILA, LA CUAL POSEE LOS DATOS DEL ENCABEZADO
            
            datos = { #DICCIONARIO VACIO
                'DNI': [],
                'Nombre': [],
                'Apellido': [],
                'Email': [],
                'Fecha de nacimiento': [],
                'Lugar de residencia': []
            }
            
            for fila in lector: #ITERAMOS SOBRE LAS FILAS SIGUIENTES DEL LECTOR PARA CAPTURAR LOS DATOS Y LLENAR EL DICCIONARIO
                if len(fila):
                    datos['DNI'].append(fila[0])
                    datos['Nombre'].append(fila[1])
                    datos['Apellido'].append(fila[2])
                    datos['Email'].append(fila[3])
                    datos['Fecha de nacimiento'].append(fila[4])
                    datos['Lugar de residencia'].append(fila[5])

                    #print(datos)#
            
            print("/// ARCHIVO LEÍDO EXITOSAMENTE ///") #EN CASO DE LEER CORRECTAMENTE EL ARCHIVO SE IMPRIME UN MENSAJE, Y SE RETORNA AL DICCIONARIO
            return datos
            
    except FileNotFoundError:
        print("\n/// ERROR /// NO SE ENCONTRÓ EL ARCHIVO: recursosPython.csv ///") #EN ESTE CASO SI NO SE ENCUENTRA EL ARCHIVO NOS MUESTRA ESTE MENSAJE
        return None

def buscar_por_apellido(datos, apellido): #COMO EL EJERCICIO LO SOLICITABA, CREAR UNA FUNCION PARA CARGAR UN APELLIDO Y QUE DE RESULTADOS CON CIERTOS PARAMETROS
    encontrados = False
    print("\n=================================")
    print("=== RESULTADOS DE LA BUSQUEDA ===") #PANTALLA DE RESULTADOS
    print("=================================")
    
    for i in range(len(datos['Apellido'])): #ESTE FOR TIENE COMO PROPOSITO BUSCAR Y ENCONTRAR LAS COINCIDENCIAS DEL APELLIDO OMITIENDO LAS MAYUSCULAS Y MINUSCULAS
        if datos['Apellido'][i].lower() == apellido.lower():
            print(f"\nDNI: {datos['DNI'][i]}")
            print(f"Nombre: {datos['Nombre'][i]}")
            print(f"Apellido: {datos['Apellido'][i]}")
            print(f"Email: {datos['Email'][i]}")
            print(f"Fecha de nacimiento: {datos['Fecha de nacimiento'][i]}")
            print(f"Lugar de residencia: {datos['Lugar de residencia'][i]}")
            print("-" * 40)
            encontrados = True
    
    if not encontrados:
        print(f"\nNO SE ENCONTRARON PERSONAS CON ESE APELLIDO {apellido}") #EN CASO DE NO COINCIDIR

def guardar_por_ciudad(datos): #SE CREA FUNCION PARA GUARDAR/EXPORTAR EL ARCHIVO CON LAS COINCIDENCIAS DEL LUGAR DE RESIDENCIA, SE CREA EN UN BLOQUE DE TRY PARA CAPTURAR POSIBLES ERRORES
    try:
        with open('personas_sf_cba.csv', 'w', newline='') as archivo: #NOMBRE DE ARCHIVO EN MODO ESCRITURA
            escritor = csv.writer(archivo)
            
            # SE ESCRIBE EL ENCABEZADO DEL ARCHIVO CON LA ESTRUCTURA YA PROPORCIONADA
            escritor.writerow(['DNI', 'Nombre', 'Apellido', 'Email', 
                             'Fecha de nacimiento', 'Lugar de residencia'])
            
            # SE GUARDA LA LISTA DE PERSONAS CON LA COINCIDENCIA
            personas_guardadas = 0
            for i in range(len(datos['Lugar de residencia'])):
                if datos['Lugar de residencia'][i].lower() in ['santa fe', 'cordoba']:
                    escritor.writerow([
                        datos['DNI'][i],
                        datos['Nombre'][i],
                        datos['Apellido'][i],
                        datos['Email'][i],
                        datos['Fecha de nacimiento'][i],
                        datos['Lugar de residencia'][i]
                    ])
                    personas_guardadas += 1
            
            print(f"\n/// SE GUARDARON {personas_guardadas} PERSONAS EN personas_sf_cba.csv ///")
    
    except Exception as e:
        print(f"\nError al guardar el archivo: {e}")

def mostrar_menu(): #MENU PARA RECORRER CON LAS DIFERENTES OPCIONES Y VALORES
    print("\n========================")
    print("=== MENÚ DE OPCIONES ===")
    print("========================")
    print("1. BUSCAR POR APELLIDO")
    print("2. EXPORTAR PERSONAS CON RESIDENCIA EN: SANTA FE Y CORDOBA")
    print("3. SALIR")

def main(): #LA ESTRUCTURA PRINCIPAL DONDE SE JUNTAN LAS DEMAS FUNCIONES Y SE CREA ESTE MENU PARA CONSULTARLAS
    datos = leer_archivo_csv()
    if not datos:
        return
    
    while True:
        mostrar_menu()
        opcion = input("\nSELECCIONE UNA OPCION (1-3): ")
        
        if opcion == "1":
            apellido = input("\nINGRESE EL APELLIDO A BUSCAR: ") #LLAMA A LA FUNCION BUSCAR POR APELLIDO
            buscar_por_apellido(datos, apellido)
        elif opcion == "2": #LLAMA A LA FUNCION GUARDAR POR CIUDAD
            guardar_por_ciudad(datos)
        elif opcion == "3": #CARTEL DE DESPEDIDA
            print("\nHASTA LUEGO!")
            break
        else:
            print("\n/// OPCION NO VALIDA. INTENTE NUEVAMENTE ///")
        
        input("\nPRESIONE ENTER PARA CONTINUAR...")

if __name__ == "__main__":
    main()