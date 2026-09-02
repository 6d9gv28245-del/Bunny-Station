BUNNY STATION
Sistema de Recomendación Musical
Cuántos de nosotros hemos puesto un reproductor de música en televisión, o nos hemos puesto nuestros audífonos, y al momento de elegir nuestra música, simplemente no sabemos qué elegir, o ninguna canción nos convence en ese momento, bueno para lidiar con esto, me gustaría desarrollar un sistema de recomendación musical desarrollado en Python 3. El programa está enfocado únicamente en las canciones del artista “Bad Bunny” y tiene como objetivo recomendar canciones al usuario de acuerdo a su estado de ánimo.
El programa hace una serie de preguntas al usuario, cada respuesta de estas preguntas tendrá una puntuación, después, compara la puntuación final con la que se le asignará a cada canción y hace una compatibilidad. 
Al finalizar del proceso, el programa muestra la canción que tiene la misma puntuación que las respuestas.

 
ALGORITMO

emoción = input("como te sientes el dia de hoy?")


if emoción == "Feliz":
    puntos_emoción = 3

if emoción == "Motivado":
    puntos_emoción = 2

if emoción == "Triste":
    puntos_emoción = 1

genéro = input("que género te gustaría escuchar hoy?")


if género == "Pop": 
    puntos_género = 3
    
if género == "Trap":
    puntos_género = 2

if género == "Salsa":
    puntos_género: 1

Total = puntos_emoción + puntos_género





