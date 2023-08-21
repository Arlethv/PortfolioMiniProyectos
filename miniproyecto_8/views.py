from django.shortcuts import render
import random

def menu(request):
    respuesta = ""
   
    if request.method == 'POST':
        opcion = int(request.POST.get('opcion', 0))
        
      
        if opcion == 1:
            saldo = random.randint(0, 1000) 
            respuesta = f"<li class='list-group-item text-center' style='font-weight: bold;'>Tu saldo dispobible es de ${saldo}.</li><li class='list-group-item'>0. Volver al menú principal.</li>"
        elif opcion == 2:
                respuesta =  "<li class='list-group-item'>21. Recarga de $25</li><li class='list-group-item'>22. Recarga de $50</li><li class='list-group-item'>23. Recarga de $100</li><li class='list-group-item'>0. Volver al menú principal.</li>"
        elif opcion == 3:
            numero = '555 ' 
            for _ in range(7):
                numero += str(random.randint(0, 9))
            respuesta = f"<li class='list-group-item text-center'>El número de teléfono es: {numero}</li><li class='list-group-item'>0. Volver al menú principal.</li>"
        elif opcion == 4:
            respuesta = "<li class='list-group-item text-center' style='font-weight: bold;'>Paquetes recomendados:</li><li class='list-group-item'>41. Paquete 20GB</li><li class='list-group-item'>42. Paquete 15GB</li><li class='list-group-item'>43. Paquete 10GB</li><li class='list-group-item'>44. Paquete 5GB</li><li class='list-group-item'>45. Paquete 2GB</li>"
        elif opcion == 5:
            respuesta = "<li class='list-group-item text-center' >Llame al 5255 12345678 </li>"
        elif opcion == 6:
            respuesta = "<li class='list-group-item'>Gracias por usar nuestros servicios. Hasta pronto.</li>"
        elif opcion == 0:
            respuesta = ""
        elif opcion==21 or opcion==22 or opcion==23:
             respuesta =  "<li class='list-group-item text-center' style='font-weight: bold;'>Recarga Enviada</li><li class='list-group-item'>0. Volver al menú principal.</li>"
        elif opcion==41 or opcion==42 or opcion==43 or opcion==42:
             respuesta =  "<li class='list-group-item text-center' style='font-weight: bold;'>Paquete Enviado</li><li class='list-group-item'>0. Volver al menú principal.</li>"

    return render(request, 'index.html', {'respuesta': respuesta})

