#  uvicorn API_Main:app --reload
# http://127.0.0.1:8000/docs


from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()



database_inventario = []




class elemento_inventario(BaseModel):
      producto_codigo: int
      producto_nombre: str
      producto_cantidad: int
      producto_Precio_compra: int
      producto_precio_venta: int
# Class Inventario



@app.get('/inventario_completo')
def get_inventario():
      return (database_inventario)
# def get inventario


@app.post('/nuevo_elemento_del_inventario')
def crear_elemento(nuevo_elemento: elemento_inventario):
      database_inventario.append(nuevo_elemento.dict())
      return (database_inventario[-1])
# def Crear Elemento


#  Obtener  un elemento con su codigo
@app.get('/elemento_especifico/{codigo_ingresado}')
def print_elemento_espefico(codigo_ingresado: int):
      
      for Loop in range(len(database_inventario)):
            if (database_inventario[Loop].producto_codigo == codigo_ingresado):
                  return (database_inventario[Loop])
            # if producto codigo == codigo ingresado
      #for Loop in database inventario
      
      return("Error")
      
      
      #return (database_inventario[codigo_ingresado])
# def Elemento Especifico



"""

database_ventas = []


class facturas_de_venta(BaseModel):
      factura_comprador: str
      factura_nit: int
      factura_articulo: str
      factura_cantidad: int
      factura_precio_final: int
# class facturas de ventas


@app.get('/todas_las_ventas')
def mostrar_ventas():
      return (database_ventas)
# def crear nueva venta

@app.post('/nueva_factuacion')
def crear_nueva_venta(nueva_venta: facturas_de_venta):
      database_ventas.append(nueva_venta.dict())
#def Crear nueva venta
"""





















































#fin.
