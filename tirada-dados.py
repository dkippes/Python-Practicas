import random

def tiradaDeDados():
    "Tira los dados, luego pregunta si desea seguir jugando sino concluye"
    numAlt1 = elegirDados()
    numAlt2 = elegirDados()

    suma = numAlt1 + numAlt2
    print("Los numeros tirados son", numAlt1 ,"y ", numAlt2 ," su suma es: ", suma)
    continuar = input("Ingrese 'si', si desea continuar: ")
    continuarTirandoSi_(continuar)

def elegirDados():
    "Elije un valor random de entre 1-6"
    return (random.randint(1, 6))

def continuarTirandoSi_(valor):
    "Tira los dados si el jugador escribe si, sino termina su sesion"
    tiradaDeDados() if valor == "si" else print("Su sesion a terminado")
    

tiradaDeDados()