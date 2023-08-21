import random
from django.http import HttpResponse
from django.shortcuts import render
from django.template import Template , Context
import os

unidades = ['', 'uno', 'dos', 'tres', 'cuatro', 'cinco', 'seis', 'siete', 'ocho', 'nueve']
decenas = ['', 'diez', 'veinte', 'treinta', 'cuarenta', 'cincuenta', 'sesenta', 'setenta', 'ochenta', 'noventa']
decenasEspeciales = ['diez', 'once', 'doce', 'trece', 'catorce', 'quince', 'dieciséis', 'diecisiete', 'dieciocho', 'diecinueve']
escalasNumericas = ['', 'mil','millones', 'billones']



def plantilla(request):
    return render(request, 'index.html')


def numeroaPalabras(numero):
    if numero == 0:
        return 'cero'
    elif numero < 0 or numero >= 1e12:
        return 'Valor fuera del rango permitido. Ingresa un número entre 0 y 999,999,999,999.'
    else:
        numeroaTexto = str(numero).split('.')
        numeroEntero = int(numeroaTexto[0])
        numeroDecimal = int(numeroaTexto[1]) if len(numeroaTexto) > 1 else 0

        numeroEnteroTexto = convertirParteEntera(numeroEntero)
        respuesta = numeroEnteroTexto

        if numeroDecimal > 0:  
            numeroaDecimalTexto = convertirParteEntera(numeroDecimal) 
            respuesta += ' punto ' + numeroaDecimalTexto

        return respuesta
  
def convertirParteEntera(numero):
   
    if numero < 10:
        return unidades[numero]
    elif numero < 20:
        return decenasEspeciales[numero - 10]
    elif numero < 100:
        unidad = numero % 10
        decena = numero // 10
        return decenas[decena] + (' y ' + unidades[unidad] if unidad > 0 else '')
    elif numero < 1000:
        centena = numero // 100
        resto = numero % 100
        if centena == 1 and resto > 0:
            return 'ciento ' + convertirParteEntera(resto)
        elif centena == 1 and resto == 0:
            return "cien"
        elif centena == 7:
            return "setecientos " + convertirParteEntera(resto)
        elif centena == 9:
            return 'novecientos ' + convertirParteEntera(resto)
        else:
            return unidades[centena] + 'cientos' + (' ' + convertirParteEntera(resto) if resto > 0 else '')
    else:
      contador = 0
      respuesta = ''
      while numero > 0:
         grupo = numero % 1000
        
         if grupo > 0:
            if contador == 1 and grupo == 1:
               respuesta = escalasNumericas[contador] + ' ' + respuesta
            elif contador==2 and grupo == 1 :
                 respuesta = 'un millon'+ ' ' + respuesta
            else:
               respuesta = convertirParteEntera(grupo) + (' ' + escalasNumericas[contador] if contador > 0 else '') + ' ' + respuesta
         numero = numero // 1000
         contador += 1
         print(respuesta)
      return respuesta.strip()


    
def convertirParteDecimal(numero):
    decimalEnTexto = numero
    return convertirParteEntera(decimalEnTexto)

def convertirNumero(request):
    if request.method == 'POST':
        numero = request.POST.get('numero')
        try:
            numero = float(numero)
            respuesta = numeroaPalabras(numero)
        except ValueError:
            respuesta = "Ingresa un número válido."
        return render(request, 'index.html', {'respuesta': respuesta})
    return render(request, 'index.html')
