print("BIENVENIDO A BUNNY-STATION")

def saludar_usuario(nombre):
    print("hola",nombre)
nombre = input("Cual es tu nombre?:")
saludo = saludar_usuario(nombre)

def inicio_usuario():
    inicio = input("estas listo para encontrar tu musica de hoy? si,no:")
    if inicio == "si":
        print ("continuemos")
    else: 
        print("programa terminado")
        exit()
inicio_usuario()

emocion = input("como te sientes el dia de hoy?: (feliz,motivado,triste)")

if emocion == "feliz":
    puntos_emocion = 10

if emocion == "motivado":
    puntos_emocion = 20

if emocion == "triste":
    puntos_emocion = 30

genero = input("que genero te gustaría escuchar hoy?: (pop,trap,sadcore)")

if genero == "pop": 
    puntos_genero = 10
    
if genero == "trap":
    puntos_genero = 20

if genero == "sadcore":
    puntos_genero = 30
    
actividad = input("que estas haciendo?: (tarea,limpiando,descansando)")

if actividad == "tarea":
    puntos_actividad = 10
    
if actividad == "limpiando":
    puntos_actividad = 20
    
if actividad == "descansando":
    puntos_actividad = 30
    
preferencia = input("quieres escuchar una cancion para cantar o relajarte?: (cantar,relajarme)")

if preferencia == "cantar":
    puntos_preferencia = 10

if preferencia == "relajarme":
    puntos_preferencia = 20
    
horario = input("es de dia o de noche?: (dia,noche)")
if horario == "dia":
    puntos_horario = 10
if horario == "noche":
    puntos_horario = 20
    

total = puntos_emocion + puntos_genero + puntos_actividad + puntos_preferencia + puntos_horario
print("PUNTOS OBTENIDOS:")

print(total)


if total == 50:
    print("CANCIONES RECOMENDADAS:")
    print("1. Ni bien ni mal")
    print("2. Quien tu eres?")
    print("3. Tenemos que hablar")
    print("4. Otra noche en miami")
    print("5. Solo de mi")

if total == 90:  
    print("CANCIONES RECOMENDADAS:")
    print("1. Si veo a tu mama")
    print("2. La dificil")
    print("3. Pero ya no")
    print("4. La santa")
    print("5. La zona")

if total == 100:    
    print("CANCIONES RECOMENDADAS:")
    print("1. El mundo es mio")
    print("2. Te mudaste")
    print("3. Hoy cobre")
    print("4. Yo visto asi")
    print("5. La noche de anoche")


def mensaje(total):
    if total == 50:
        print("¡Muy buena elección!")
    elif total == 90:
        print("¡Esta combinación se escucha bien!")
    elif total == 100:
        print("¡Hoy necesitas canciones muy intensas!")

mensaje(total)




    
