from database import creacion_tabla, guardar_cotizacion, mostrar_cotizacion
from dolar import obtener_todos, obtener_dolar_blue, obtener_dolar_oficial, obtener_dolar_cripto, obtener_dolar_tarjeta

if __name__ == "__main__":
    # todo adentro

    datos = obtener_todos()
    blue_venta, blue_compra = obtener_dolar_blue(datos)
    oficial_venta, oficial_compra = obtener_dolar_oficial(datos)
    cripto_venta, cripto_compra = obtener_dolar_cripto(datos)
    tarjeta_venta, tarjeta_compra= obtener_dolar_tarjeta(datos)

    #--------------------------------------------------------------
    creacion_tabla() 
    guardar_cotizacion("Blue", blue_venta, blue_compra)
    guardar_cotizacion("Oficial", oficial_venta, oficial_compra)
    guardar_cotizacion("Cripto", cripto_venta, cripto_compra)
    guardar_cotizacion("Tarjeta", tarjeta_venta, tarjeta_compra)
    mostrar_cotizacion()

