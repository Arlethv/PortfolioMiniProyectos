from django.shortcuts import render, redirect
import random

palabras = ["html","css","python","django","sql","api","docker","git","backend","frontend","crud","devops"]
palabra_seleccionada = random.choice(palabras)
adivinar_palabra = ["_" for _ in palabra_seleccionada]
intentos = 3

def adivinarLetra(letra):
    global adivinar_palabra
    if letra in palabra_seleccionada:
        for i in range(len(palabra_seleccionada)):
            if palabra_seleccionada[i] == letra:
                adivinar_palabra[i] = letra
        return True
    else:
        return False

def FindelJuego():
    if "_" not in adivinar_palabra:
        return "ganar"
    elif intentos == 0:
        return "perder"
    else:
        return "continuar"
intentos = 3

def juego_ahorcado(request):
    
    global intentos, adivinar_palabra, palabra_seleccionada
    mensaje = ""

    if request.method == "POST":
        letra = request.POST.get("letra")
        if letra is not None:
            letra = letra.lower()
            if adivinarLetra(letra):
                mensaje = "¡Correcto!"
            else:
                intentos  -= 1
                mensaje = "Incorrecto"
    status = FindelJuego()
    if status == "ganar":
        mensaje = "¡Ganaste!"
        reiniciar() 
    elif status == "perder":
        mensaje = "¡Perdiste! La palabra anterior era '{}'".format(palabra_seleccionada)
        reiniciar() 
        
        # Restablecer vlos valores al finalizar el juego
        adivinar_palabra = ["_" for _ in palabra_seleccionada]
        intentos  = 3
        palabra_seleccionada = random.choice(palabras)
        
    letras=[]
    letras = [chr(letra) for letra in range(65, 91)] 

    juego= {
        "intentos": intentos ,
        "adivinar_palabra": adivinar_palabra,
        "mensaje": mensaje,
        "letras": letras
    }
    return render(request, "index.html", juego)

def reiniciar():
    global intentos , adivinar_palabra, palabra_seleccionada
    intentos  = 3
    palabra_seleccionada = random.choice(palabras)
    adivinar_palabra = ["_" for _ in palabra_seleccionada]

