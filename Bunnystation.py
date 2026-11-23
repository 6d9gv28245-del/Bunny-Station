print("====================================")
print("          BUNNY-STATION")
print("       TU MUSICA, TU MOMENTO")
print("====================================")

def saludar_usuario(nombre):
    print("--------------------------------------------")
    print("hola",nombre,"!", "Bienvenid@ a BUNNY-STATION :)")
    print("--------------------------------------------")

nombre = input("Cual es tu nombre?: ")
saludo = saludar_usuario(nombre)

def inicio_usuario():
    print()
    print("               MENU PRINCIPAL")
    print("--------------------------------------------")
    inicio = input("estas listo para encontrar tu musica de hoy? si, no: ")
    
    if inicio == "si":
        print ("Okay! continuemos")
    elif inicio == "no": 
        print("Gracias por usar BUNNY-STATION")
        exit()
    else:
        print("respuesta no valida")
        exit()

inicio_usuario()

archivo = open("historial.txt", "w")
archivo.close()

lista_canciones = {
    50:["Ni bien ni mal","Quien tu eres","Tenemos que hablar","Otra noche en miami","Solo de mi"],
    60:["Si veo a tu mama","La dificil","Pero ya no","La santa","La zona"],   
    70:["El mundo es mio","Te mudaste","Hoy cobre","Yo visto asi","La noche de anoche"],
    80:["Moscow mule","despues de la playa","Un ratito","Neverita","Efecto"],
    90:["Nadie sabe","Monaco","Fina","Hibiki","Mr october"],
    100:["Nuevayol","Voy a llevarte pa pr","Baile inolvidable","Perfumito nuevo","Weltita"],
    110:["Como antes","Vete","Booker t","Dakiti","Party"],
    120:["Ojitos lindos","Un coco","Los pits","Acho pr","Enseñame a bailar"],
    130:["Ignorantes","Una vez","Trellas","El apagon","Kloufrens"]
}
canciones_genero = [
    ["pop","Moscow mule","Neverita","Efecto"],
    ["trap","Chambea","Booker t","Dakiti"],
    ["sadcore","Amorfoda","Otro atardecer","un coco"]
]

continuar = "si"

while continuar == "si":
    print()
    print("============================================")
    print("             PERSONALIZA TU MUSICA")
    print("============================================")
    print()

    emocion = input("como te sientes el dia de hoy? (feliz,motivado,triste): ")
    emocion = emocion.lower().strip()
    
    if emocion == "feliz":
        puntos_emocion = 10
    elif emocion == "motivado":
        puntos_emocion = 20
    elif emocion == "triste":
        puntos_emocion = 30
    else:
        print("respuesta no valida")
        continue
    print()
    
    genero = input("que genero te gustaría escuchar hoy? (pop,trap,sadcore): ")
    genero = genero.lower().strip()
    
    if genero == "pop": 
        puntos_genero = 10
    elif genero == "trap":
        puntos_genero = 20
    elif genero == "sadcore":
        puntos_genero = 30
    else:
        print("respuesta no valida")
        continue
    print()
   
    actividad = input("que estas haciendo? (tarea,limpiando,descansando): ")
    actividad = actividad.lower().strip()
    if actividad == "tarea":
        puntos_actividad = 10
    elif actividad == "limpiando":
        puntos_actividad = 20
    elif actividad == "descansando":
        puntos_actividad = 30
    else:
        print("respuesta no valida")
        continue
    print()
   
    preferencia = input("quieres escuchar una cancion para cantar o relajarte? (cantar,relajarme): ")
    preferencia = preferencia.lower().strip()
    if preferencia == "cantar":
        puntos_preferencia = 10

    elif preferencia == "relajarme":
        puntos_preferencia = 20
    else:
        print("respuesta no valida")
        continue
    print()
    
    horario = input("es de dia o de noche? (dia,noche): ")
    horario = horario.lower().strip()
    if horario == "dia":
        puntos_horario = 10
    elif horario == "noche":
        puntos_horario = 20
    else:
        print("respuesta no valida")
        continue
   
    total = puntos_emocion + puntos_genero + puntos_actividad + puntos_preferencia + puntos_horario
    
    print()
    print("============================================")
    print("              TUS RESULTADOS")
    print("============================================")
    print()
    print("PUNTOS OBTENIDOS:", total)

    print()
    print("--------------------------------------------")
    print("       CANCIONES SEGUN TU GENERO")
    print("--------------------------------------------")

    for fila in canciones_genero:
        if genero == fila[0]:
            for i in range(1,len(fila)):
                print(i, "-", fila[i])

    print()
    print("--------------------------------------------")
    print("           TUS RECOMENDACIONES")
    print("--------------------------------------------")

    if total in lista_canciones:
        canciones = lista_canciones[total]
        print("1.",canciones[0])
        print("2.",canciones[1])
        print("3.",canciones[2])
        print("4.",canciones[3])
        print("5.",canciones[4])
   
    print()
        
    def mensaje(total):
        if total >= 50 and total <= 70:
            print("¡Muy buena elección!")
        elif total >= 80 and total <= 100:
            print("¡Esta combinación se escucha bien!")
        elif total >= 110 and total <= 130:
            print("¡Hoy necesitas canciones muy intensas!")

    mensaje(total)
    
    print()
    print("--------------------------------------------")
    print("          GUARDANDO HISTORIAL")
    print("--------------------------------------------")
    
    archivo = open("historial.txt","a")

    archivo.write("Nombre: " + nombre + "\n")
    archivo.write("Emocion: " + emocion + "\n")
    archivo.write("Genero: " + genero + "\n")
    archivo.write("Puntos obtenidos: " + str(total) + "\n")
    archivo.write("----------------------\n")

    archivo.close()

    print("Informacion guardada correctamente")
    print()

    continuar = input("quieres otra recomndación?:(si/no)")

print()
print("============================================")
print("             CONSULTAR HISTORIAL")
print("============================================")
    

consultar = input("Quieres consultar tu historial? si/no:")

if consultar == "si":

    archivo = open("historial.txt","r")

    contenido = archivo.read()

    print()
    print("--------------------------------------------")
    print("             HISTORIAL MUSICAL")
    print("--------------------------------------------")
    print(contenido)

    archivo.close()

archivo = open("historial.txt", "w")
archivo.close()

print()
print("============================================")
print("          GRACIAS POR USAR")
print("             BUNNY-STATION")
print("           ¡HASTA LA PROXIMA!")
print("============================================")


    
