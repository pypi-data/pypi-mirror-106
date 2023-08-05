# Ruleta rusa
## _Proyecto con fines académicos_

Si quieres testear este paquete, te recomiendo hacerlo con el siguiente código: 
```
import ruletarusa as rr

def menu():
    """Funció que conté el menú del programa"""
    print("---------------------- RULETA RUSA ------------------------")
    print("-----------------------------------------------------------")


numero_jugadores = int(input("Indica el número de jugadores: "))
juego = rr.Juego(numero_jugadores)

while not juego.finJuego():
    print()
    menu()
    juego.ronda()

print("Juego terminado.")
print("-----------------------------------------------------------")
```

También te dejo el enlace a mi repositorio con el proyecto finalizado.
https://github.com/cfsergio/RuletaRusa