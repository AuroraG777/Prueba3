Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import csv
... lista=[]
... diccionario={}
... def categoria(puntos)
...     if puntos>=0 and puntos<=40:
...         cat="Amateur"
...     elif puntos>=41 and puntos<=80:
...         cat="Principiante"
...     elif puntos>=81 and puntos<=120:
...         cat="Avanzado"
...     elif puntos>120:
...         cat="Ídolos"
...     return cat
... def promedio():
...     acum=0
...     cant=len(lista)
...     if cant>0:
...         for x in lista:
...             acum=acum+int(x[puntos])
...             prom=acum/cant
...             print("Puntaje acumulado:",acum)
...             print("Puntaje promedio :",prom)
... def mayor():
...     mayor=0
...     for x in lista:
...         if int(x['puntos'])>int(mayor):
...             mayor=x['puntos']
...         else:
...             mayor=mayor
...      print("El puntaje mayor es: ",mayor)
... def actualizar(buscar_id):
...     buscar_id=int(input(print("Ingrese ID del equipo que desea actualizar":))
...         encontrado=False
...         for x in lista:
...           if buscar_id==int(x["id",x['id'],"nombre",x['nombre'],"puntos",x['puntos'])
...              encontrado=True
...              break
...           if encontrado=False:
...               print("ID no existe")
... while (True):
...     print("")
...     print(".-.-.-.-M E N U.-.-.-")
...     print("1.-Agregar equipo")
...     print("2.-Listar equipo")
...     print("3.-Actualizar nombre de equipo por ID")
...     print("4.-Generar base de datos")
...     print("5.-Cargar base de datos")
...     print("6.-Estadísticas")
    print("0.-Salir")
    op=int(input("Ingrese una opción :"))
    if op==1:
        print("")
        print(".-.-A G R E G A R  E Q U I P O.-.-")
        id=int(input("Ingrese ID:"))
        nombre=(input("Ingrese nombre:"))
        puntos=int(input("Ingrese cantidad de puntos:"))
        categoria(puntos)
        diccionario={"id":id,"nombre":nombre,"puntos":puntos,"categoria":categoria}
        lista.append(diccionario)
        print("")
    elif op==2:
        print(".-.-.-L I S T A  D E  E Q U I P O S.-.-.-")
        for x in lista:
            print("id",x['id'],"nombre",x['nombre'],"puntos",x['puntos'],"categoria",x['categoria'])
            print("")
    elif op==3:
        actualizar(buscar_id)
        print("")
    elif op==4:
        with open ('bbdd_equipos.csv','w',newline='') as bbdd_equipos:
        campos=['id','nombre','puntos','categoria']
        escritor_csv=csv.DictWriter(bbdd_equipos,fieldnames=campos)
        escritor_csv.writeheader()
        escritor_csv.writerows(lista)
        print("")
    elif op==5:
        with open ('bbdd_equipos.csv','r',newline='') as bbdd_equipos:
        lector_csv=csv.reader(bbdd_equipos)
        for fila in lector_csv:
            lista.append(fila)
        print("")
    elif op==6:
        print(".-.-.- E S T A D Í S T I C A S .-.-.-.-")
        promedio()
        mayor()
        
        print("")
    elif op==0:
        print("ADIÓS...")
        print("")
