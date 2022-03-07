

class Vendiendo:
      def __init__(self, Comprador = None, Nit = None, Articulo = None, Cantidad = None, Precio_Final = None):
            self.Comprador = Comprador
            self.Nit = Nit
            self.Articulo = Articulo
            self.Cantidad = Cantidad
            self.Precio_Final = Precio_Final
      # def __init__
# Class Vendiendo


class Ventas:
      
      def __init__(self):
            self.head = None
      #def __init__
      
      
      
      def Insert_Nueva_Venta(self, Comprador_insert, Nit_insert, Articulo_insert, Cantidad_insert, Precio_Final_insert):
            new_Vendiendo = Vendiendo(Comprador_insert, Nit_insert, Articulo_insert, Cantidad_insert, Precio_Final_insert)
            new_Vendiendo.next = self.head
            self.head = new_Vendiendo
      # def Insert Nueva Venta
      
      
      
      
      def List_Print(self):
            print_value = self.head
            
            if (print_value is None):
                  print("No se realiso ninguna venta.")
            #if print value is not none
            
            while (print_value):
                  print("Nombre del cliente:", print_value.Comprador)
                  print("Su NIT:", print_value.Nit)
                  print("Compro el articulo:", print_value.Articulo)
                  print("Compro la cantidad de:", print_value.Cantidad)
                  print("Pago un total de:", print_value.Precio_Final)
                  print(" ")
                  print_value = print_value.next
            # While Print Value
      # Def List Print
      
      
# class Ventas


