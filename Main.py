""" 
      Proyecto Estructura de Datos
      Paul Bauer 
      20210060

      Entrega 1

"""

import InventarioList      # Importanto el codigo del linked list para el inventario
import VentasList          # Importando el codigo del linked list para las ventas
Lista = InventarioList.Inventario()
Salidas = VentasList.Ventas()

def Runner():

   Elementos_Totales = 0
   Ventas_Totales = 0
   Utilidad_Empresa = 0
   
   #Corriendo = 0
   Corriendo = Tabla()
   while (Corriendo != 6):
   
   
         #         Creando / anadiendo un producto
         if (Corriendo == 1):
               print("Entre primero el codigo del articulo")
               Codigo, Encontrado, HeadValue = Codigo_Encontrado(Elementos_Totales)
            
               if (Encontrado == 0):
                     print("Esta creado un nuevo elemento!")
                     Elementos_Totales, Utilidad_Empresa = Nuevo_Elemento(Codigo, Elementos_Totales, Utilidad_Empresa)
               # if Encontrado == 0
               
               if (Encontrado == 1):
                     Utilidad_Empresa = Ingreso_Cantidad(Elementos_Totales, HeadValue, Utilidad_Empresa)
               # if Encontrado == 1
               
               print("Se anadieron correctamente los nuevos productos al inventario!")
            
               Corriendo = Tabla()
         # if Corriendo == 1
         
         
         
         
         #         Generando una venta
         if (Corriendo == 2):
            Comprador, Nit = Info_Basica_Cliente()
            
            Codigo, Encontrado, HeadValue = Articulo_a_Comprar(Elementos_Totales)
            
            if (Encontrado == 0):
                  pass
            #if Encontrado == 0
            
            else:
                  Ventas_Totales, Utilidad_Empresa = Proceso_Facturacion(Comprador, Nit, HeadValue, Ventas_Totales, Utilidad_Empresa)
            # else
            
            Corriendo = Tabla()
         # if Corriendo == 2
         
         
         
         
         
         #        Imprimimos la utilidad de la empresa
         if (Corriendo == 3):
            print("La utilidad de la empresa es de:", Utilidad_Empresa)
            Corriendo = Tabla()
         # if Corriendo == 3
         
         
         
         
         #        Imprimir todo el inventario
         if (Corriendo == 4):
            Lista.List_Print()
            
            Corriendo = Tabla()
         # if Corriendo == 4
         
         
         
         
         #        Imprimir todas las ventas
         if (Corriendo == 5):
            Salidas.List_Print()
            
            Corriendo = Tabla()
         # if Corriendo == 5
         
         
         
         
         #        Entrada invalilda
         if (Corriendo < 1 or Corriendo > 6):
            print("Entrada invalida.")
            Corriendo = Tabla()
         #If Corriendo < 1 or Corriendo > 6
         
   # While corriendo != 6
   
   if Corriendo == 6:
      print("Ok, adios!")
   # if Corriendo == 6
# def Runner







def Tabla():
   print(" ")
   print("Que es lo que quiere hacer?")
   print("1) Entrada de articulos.")
   print("2) Salida / Venta de articulos.")
   print("3) Calculo de la utilidad total de la empresa.")
   print("4) Mostrar todo el inventario.")
   print("5) Mostrar todas las ventas.")
   print("6) Salir.")
   
   Seleccionado = int(input())
   
   return(Seleccionado)
# def Tabla








def Codigo_Encontrado(Elementos_Totales):

   Codigo = int(input())  # Pedimos al usuario el codigo
   
   Encontrado, HeadValue = Lista.Existencia(Codigo, Elementos_Totales)
   
   return(Codigo, Encontrado, HeadValue)

# def Codigo Encontrado







   # Creamos un nuevo elemento en el inventario
def Nuevo_Elemento(Codigo, Elementos_Totales, Utilidad_Empresa):
      print("Entre el nombre del elemento:")
      Nombre = input()
         
      print("Ingrese la cantidad entrante:")
      Cantidad = int(input())
         
      print("Entre el precio de compra por unidad: (Cuanto costo cada articulo que ingresa al inventario)")
      Precio_Compra = int(input())
      
      print("Entre el precio de venta por unidad: (Por cuanto desea vender cada articulo)")
      Precio_Venta = int(input())
      
      Lista.Insert_New_Element(Codigo, Nombre, Cantidad, Precio_Compra, Precio_Venta)
      
      Elementos_Totales = Elementos_Totales + 1
      
      Utilidad_Empresa = Utilidad_Empresa - (Precio_Compra * Cantidad)
      return(Elementos_Totales, Utilidad_Empresa)
# def Nuevo Elemento








   # El articulo ya existe en el inventario y le anadimos una cantidad
def Ingreso_Cantidad(Codigo, HeadValue, Utilidad_Empresa):
      Nombre, Cantidad, Precio_Compra, Precio_Venta = Lista.Devolver_Valores(HeadValue)
      
      print("Usted se refiere al producto", Nombre)
      
      print("Cual es la cantidad del producto ingresando? ")
      Ingresando = int(input())
      
      Cantidad = Cantidad + Ingresando
      
      Lista.Modificar_Elemento(HeadValue, Cantidad)
      
      Utilidad_Empresa = Utilidad_Empresa - (Precio_Compra * Ingresando)
      print("Se realiso exitosamente el ingreso de los nuevos productos!")
      return(Utilidad_Empresa)
#Def Ingreso Cantidad








   # -- Pedimos el nombre y Nit del cliente--
def Info_Basica_Cliente():
      print("Cual es el nombre del cliente?")
      Comprador = input()
      
      print("Cual es su NIT?")
      Nit = int(input())
      
      return(Comprador, Nit)
      
# def Info Basica Cliente







   #-- Definimos que articulo se vende y si ese existe.--
def Articulo_a_Comprar(Elementos_Totales):
      print("Que articulo desea comprar el cliente?")
      print("Entrar su codigo: ")
      
      Encontrado = 0
      while (Encontrado != 1):  #Corre asta que se encuentre un codigo existente / que abortemos el proceso voluntariamente
            Codigo, Encontrado, HeadValue = Codigo_Encontrado(Elementos_Totales)  #Verifico si el elemento existe y cual es.
            
            #Si el elemento existe
            if (Encontrado == 1):   
                  return(Codigo, Encontrado, HeadValue)
            #if Encontrado == 1
            
            
            #Si el elemento no se encontro
            if (Encontrado == 0):
                  print("No se encontro un articulo con ese codigo.")
                  Que_Hacer = 3
                  
                  while (Que_Hacer < 1 or Que_Hacer > 2):
                        print("Que desea hacer?")
                        print("1) Volver a entrar un codigo")
                        print("2) Abortar el proceso de venta")
                  
                        Que_Hacer = int(input())
                  
                        if (Que_Hacer == 1):
                              print("Entre de nuevo el codigo:")
                        #if Que hacer == 1
                  
                        if (Que_Hacer == 2):
                              print("Se aborto el proceso de venta.")
                              return(0, 0, 0)
                        # If Que Hacer == 2
                        
                        if (Que_Hacer < 1 or Que_Hacer > 2):
                              print("Entrada invalida.")
                        # if Que_Hacer < 1 or Que_Hacer > 2
                  
                  #While Que Hacer < 1 or Que_Hacer > 2
                  
            # if Encontrado == 0
       
       # While Encontrado != 1
       
# def Articulo_a_Comprar








   # -- Si todo esta en orden, procedemos a la facturacion--
def Proceso_Facturacion(Comprador, Nit, HeadValue, Ventas_Totales, Utilidad_Empresa):
 
      Nombre, Cantidad, Precio_Compra, Precio_Venta = Lista.Devolver_Valores(HeadValue)
      
      print("El cliente desea comprar", Nombre)
      print("Cuanto desea comprar de ese articulo?")
      print("Tomando en cuenta que hay", Cantidad, "articulos disponibles en el inventario.")
      Cantidad_Venta = int(input())
      
      while (Cantidad_Venta > Cantidad):
            print("No se puede procesar la venta, no tenemos sufisamientes articulos en el inventario.")
            print("Volver a entrar la cantidad que desea comprar el cliente.")
            print("Cantidad max: ", Cantidad)
            Cantidad_Venta = int(input())
      # while Cantidad Venta > Cantidad
      
      Cantidad = Cantidad - Cantidad_Venta
      Lista.Modificar_Elemento(HeadValue, Cantidad)
      
      
      Precio_Final = Cantidad_Venta * Precio_Venta
      
      print("El precio que debe de pagar el cliente es de $", Precio_Final)
      
      Salidas.Insert_Nueva_Venta(Comprador, Nit, Nombre, Cantidad_Venta, Precio_Final)
      
      Ventas_Totales = Ventas_Totales + 1
      print("Se ejecuto exitosamente la nueva venta!")
      
      Utilidad_Empresa = Utilidad_Empresa + (Cantidad_Venta * Precio_Venta)
      return(Ventas_Totales, Utilidad_Empresa)
#def Proceso Facturacion



























































#fin.