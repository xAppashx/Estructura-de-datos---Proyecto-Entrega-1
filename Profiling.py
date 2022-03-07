import Main
import cProfile

import InventarioList      # Importanto el codigo del linked list para el inventario
import VentasList          # Importando el codigo del linked list para las ventas
Lista = InventarioList.Inventario()
Salidas = VentasList.Ventas()

# Creo elementos en las 2 listas encadenadas sino no funccionara el profiling.
"""
Lista.Insert_New_Element(11, "Manzanas", 33, 2, 3)
Lista.Insert_New_Element(12, "Bananos", 52, 1, 3)

Salidas.Insert_Nueva_Venta("Enrique", 135927, "Bananos", 12, 36)
Salidas.Insert_Nueva_Venta("Pedro", 390475, "Manzanas", 6, 18)

"""


def Tabla():
   print("Que profiling quiere hacer?")
   print("0) Salir")
   print("1) Tabla")
   print("2) Codigo_Encontrado")
   print("3) Nuevo_Elemento")
   print("4) Ingreso_Cantidad  // No funcciona en el profiling.")  #Necesio darle un espacio en memoria especifico para que funcciona. Funcciona en el main, pero no aqui.
   print("5) Info_Basica_Cliente")
   print("6) Articulo_a_Comprar")
   print("7) Proceso_Facturacion // No funcciona en el profiling.")  #Necesio darle un espacio en memoria especifico para que funcciona. Funcciona en el main, pero no aqui.")
   
   Opcion = int(input())
   return(Opcion)
#Def Tabla



Opcion = 3
Opcion = Tabla()

while Opcion != 0:
   
   if Opcion == 1:
      print("")
      print("Profiling de la funccion 'Tabla' :")
      cProfile.run('Main.Tabla()')
      
      Opcion = Tabla()
   #if Opcion == 1
   
   
   
   if Opcion == 2:
      print("")
      print("Profiling de la funccion 'Codigo_Encontrado' :")
      print("Ingrese el numero 11")
      cProfile.run('Main.Codigo_Encontrado(2)')
      
      Opcion = Tabla()
   # if Opcion = 2
   
   
   
   if Opcion == 3:
      print("")
      print("Profiling de la funccion 'Nuevo_Elemento' :")
      cProfile.run('Main.Nuevo_Elemento(13, 2, 25)')
      
      Opcion = Tabla()
   #If Opcion == 3
   
   
   
   if Opcion == 4:
      print("")
      #print("Profiling de la funccion 'Ingreso_Cantidad' :")
      #cProfile.run('Main.Ingreso_Cantidad(11, 0, 7)')
      print("El profiling no funccionara. Proceso abortado.")
      print("")
      
      Opcion = Tabla()
   # if Opcion == 4
   
   
   
   if Opcion == 5:
      print("")
      print("Profiling de la funccion 'Info_Basica_Cliente' :")
      cProfile.run('Main.Info_Basica_Cliente()')
      
      Opcion = Tabla()
   # If Opcion == 5
   
   
   
   if Opcion == 6:
      print("")
      print("Profiling de la funccion 'Articulo_a_Comprar' :")
      cProfile.run('Main.Articulo_a_Comprar(2)')
      
      Opcion = Tabla()
   #if Opcion == 6
   
   
   
   if Opcion == 7:
      print("")
      #print("Profiling de la funccion 'Proceso_Facturacion' :")
      #cProfile.run('Main.Proceso_Facturacion(Gorge, 3294850, 4, 9, 15)')  Tambien necesito el espacio especifico en memoria. No funccionara aqui.
      print("No funccionara. Proceso abortado.")
      print("")
      Opcion = Tabla()
   # If Opcion == 7
   
   
   
   if Opcion < 0 or Opcion > 7:
      print("Entrada invalida.")
      Opcion = Tabla()
   # if Opcion invalida.
   
#While Opcion != 0

if Opcion == 0:
   print("Ok, adios!")


