# Importamos las herramientas de telegram
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Importamos dotenv para leer el archivo .env(dodne guardo el token de manera privada)
from dotenv import load_dotenv
import os

# Importamos nuestras funciones
from database import guardar_cotizacion, creacion_tabla
from dolar import obtener_todos, obtener_dolar_blue, obtener_dolar_oficial, obtener_dolar_cripto, obtener_dolar_tarjeta

# Carga las variables del archivo .env
load_dotenv()

# Lee el token del archivo .env, nunca hardcodeado
TOKEN = os.getenv("TELEGRAM_TOKEN")

#-----------------------------------------------------------------------------------
#Funcion que inciializa y muestra comandos:
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        """ Bienvenido a Cotizado Bot 🤖
        
    Estos son los comandos disponibles:
        /blue - Dólar Blue
        /oficial - Dólar Oficial
        /cripto - Dólar Cripto
        /tarjeta - Dólar Tarjeta """
    )
    
# Esta función se ejecuta cuando alguien escribe /blue
# update contiene info del mensaje (quién lo mandó, a qué chat responder)
# context contiene info del bot (no lo usamos acá pero telegram lo exige)
async def blue(update: Update, context: ContextTypes.DEFAULT_TYPE):
    datos = obtener_todos()  # una sola llamada a la API
    venta, compra = obtener_dolar_blue(datos)
    await update.message.reply_text(
        f"💵🚨 Dólar Blue\n"
        f"Venta: ${venta}\n"
        f"Compra: ${compra}"
    )
    guardar_cotizacion("Blue", venta, compra)

async def oficial(update: Update, context: ContextTypes.DEFAULT_TYPE):
    datos = obtener_todos()  # una sola llamada a la API
    venta, compra = obtener_dolar_oficial(datos)
    await update.message.reply_text(
        f"💵 Dólar Oficial\n"
        f"Venta: ${venta}\n"
        f"Compra: ${compra}"
    )
    guardar_cotizacion("Oficial", venta, compra)

async def cripto(update: Update, context: ContextTypes.DEFAULT_TYPE):
    datos = obtener_todos()  # una sola llamada a la API
    venta, compra = obtener_dolar_cripto(datos)
    await update.message.reply_text(
        f"💵🪙 Dólar Cripto\n"
        f"Venta: ${venta}\n"
        f"Compra: ${compra}"
    )
    guardar_cotizacion("Cripto", venta, compra)

async def tarjeta(update: Update, context: ContextTypes.DEFAULT_TYPE):
    datos = obtener_todos()  # una sola llamada a la API
    venta, compra = obtener_dolar_tarjeta(datos)
    await update.message.reply_text(
        f"💵💳 Dólar Tarjeta\n"
        f"Venta: ${venta}\n"
        f"Compra: ${compra}"
    )
    guardar_cotizacion("Tarjeta", venta, compra)

    

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start",start))
app.add_handler(CommandHandler("blue",blue))
app.add_handler(CommandHandler("oficial",oficial))
app.add_handler(CommandHandler("cripto",cripto))
app.add_handler(CommandHandler("tarjeta",tarjeta))
app.run_polling()
