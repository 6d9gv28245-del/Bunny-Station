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