emocion = input("como te sientes el dia de hoy?")

if emocion == "feliz":
    puntos_emocion = 10

if emocion == "motivado":
    puntos_emocion = 20

if emocion == "triste":
    puntos_emocion = 30

genero = input("que genero te gustaría escuchar hoy?")

if genero == "pop": 
    puntos_genero = 10
    
if genero == "trap":
    puntos_genero = 20

if genero == "sadcore":
    puntos_genero = 30
    
actividad = input("que estas haciendo?")

if actividad == "tarea":
    puntos_actividad = 10
    
if actividad == "limpiando":
    puntos_actividad = 20
    
if actividad == "descansando":
    puntos_actividad = 30
    
preferencia = input("quieres escuchar una cancion para cantar o relajarte?")

if preferencia == "cantar":
    puntos_preferencia = 10

if preferencia == "relajarme":
    puntos_preferencia = 20
    
horario = input("es de dia o de noche?")
if horario == "dia":
    puntos_horario = 10
if horario == "noche":
    puntos_horario = 20
    

total = puntos_emocion + puntos_genero + puntos_actividad + puntos_preferencia + puntos_horario
print("PUNTOS OBTENIDOS:")

print(total)


if total == 50:
    print("CANCIÓNES RECOMENDADAS:")
    print("1.NADIE SABE LO QUE VA A PASAR MAÑANA")
    print("2.Vete")
if total == 90:  
    print("3.MR.OCTOBER")
    print("4.BOOKER T")
    
if total == 100:    
    print("5.VUELVE CANDY B")
    print("6.MONACO")


def mensaje(total):
    if total == 50:
        print("¡Muy buena elección!")
    elif total == 90:
        print("¡Esta combinación se escucha bien!")
    elif total == 100:
        print("¡Hoy necesitas canciones muy intensas!")

mensaje(total)




    