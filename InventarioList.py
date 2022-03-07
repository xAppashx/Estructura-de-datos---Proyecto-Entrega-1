


class ElementoInventario:
      
      def __init__(self, codigo = None, Nombre = None, cantidad = None, Precio_Compra = None, Precio_Venta = None):   #Has to be called __init__ !
            self.codigo = codigo
            self.Nombre = Nombre
            self.cantidad = cantidad
            self.Precio_Compra = Precio_Compra
            self.Precio_Venta = Precio_Venta
            self.next = None
      # Def __init__ 
      
# Class ElementoInventario


class Inventario:
      
      def __init__(self):
            self.head = None
      # Def __init__
      
         # --adding an element--      
      def Insert_New_Element(self, codigo_insert, Nombre_insert, Cantidad_insert, Precio_Compra_insert, Precio_Venta_Insert):
            new_Element = ElementoInventario(codigo_insert, Nombre_insert, Cantidad_insert, Precio_Compra_insert, Precio_Venta_Insert)
            new_Element.next = self.head
            self.head = new_Element
      # Def Insert New Element
      
      
         # --removing an element--
      def Remove_Element(self, Removing):
            head_value = self.head
            
            
            if (head_value is not None):
                  
                  if (head_value.codigo == Removing):
                        self.head = head_value.next
                        head_value = None
                  # if HeadValue.Codigo == Removing
                  
            # if Head Value isn't None
            
            while (head_value is not None):
                  
                  if (head_value.codigo == Removing):
                        break
                  # if HeadValue.codigo == Removing
                  
                  previous = head_value
                  head_value = head_value.next
            # While Head Value isn't None
            
            if (head_value == None):
                  print("No se encontro el elemento, no se puede procesar.")
                  return
            # if Head Value == None
            
            previous.next = head_value.next
            head_value = None
            
      # Def Remove_Element
      
      
      
      
         # --Verificar si un elemento existe base a un codigo especifico--      
      def Existencia(self, existente, Elementos_Totales):
            head_value = self.head
            
            if (head_value == None):
                  
                  return(0, None)
            # if head_value == None
            
            
            else:
                  iteracion = 0
                  while (iteracion < Elementos_Totales):
            
                        if (head_value.codigo == existente):
                              print("Codigo encontrado!")
                              return(1, head_value)
                              break
                        # If head value = existente
                        iteracion = iteracion + 1
                        head_value = head_value.next
                  # while iteracion < Elementos_Totales
                  
                  if (iteracion == Elementos_Totales):
                        
                        return(0, None)
                  # if iteracion == Elementos Totales
            

      # Def Existencia
      
      
      def List_Print(self):
            print_value = self.head
            
            if (print_value is None):
               print("Inventario vacio !")
               
            
            while (print_value):
                  print("Codigo:", print_value.codigo)
                  print("Nombre:", print_value.Nombre)
                  print("Cantidad:", print_value.cantidad)
                  print("Precio de compra:", print_value.Precio_Compra)
                  print("Precio de venta:", print_value.Precio_Venta)
                  print(" ")
                  print_value = print_value.next
            # While Print Value
            
      # Def List Print
      
      
      
      
      def Devolver_Valores(self, Head_Value):
            head_value = self.head
            
            while (head_value is not None):
            
                  if (head_value == Head_Value):
                        return(head_value.Nombre, head_value.cantidad, head_value.Precio_Compra, head_value.Precio_Venta)
                        break
                  # if head_value = HeadValue
                  
                  previous = head_value
                  head_value = head_value.next
            # while head value is not none
            
      # Def Devolver Valores
      
      
      
      def Modificar_Elemento(self, HeadValue, Nueva_Cantidad):
            head_value = self.head
            
            while (head_value is not None):
            
                  if (head_value == HeadValue):
                        head_value.cantidad = Nueva_Cantidad
                        break
                  # if head_value = HeadValue
                  
                  previous = head_value
                  head_value = head_value.next
            # while head value is not none
            
      # Def Devolver Valores            
      
      
      
      
      
# Class Inventario





















































