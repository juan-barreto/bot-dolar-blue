import requests

#Me devuelve el valor de venta del dolar blue
def obtener_dolar_blue():
    respuesta = requests.get("https://dolarapi.com/v1/dolares")

    datos = respuesta.json()
    for dolar in datos:

        if dolar["casa"] == "blue":
            return dolar["venta"]

if __name__ == "__main__":
    print(obtener_dolar_blue())