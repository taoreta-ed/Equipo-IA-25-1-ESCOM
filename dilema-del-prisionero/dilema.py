# Recuerda hacer pip install gspread oauth2client
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Configura el acceso a Google Sheets
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("dilema-del-prisionero-442816-78d33b6bfc70.json", scope)
client = gspread.authorize(creds)

# Abre la hoja de cálculo y selecciona la hoja
spreadsheet = client.open("Dilema del prisionero") 
worksheet = spreadsheet.sheet1  # Puedes cambiar a la hoja específica que quieras

# Función para obtener la elección y enviar el dato a Google Sheets
def enviar_eleccion():
    print("Selecciona una opción:")
    print("1. Cooperar")
    print("2. Traicionar")
    
    opcion = input("Ingresa el número de la opción: ")
    if opcion == "1":
        eleccion = "Cooperar"
    elif opcion == "2":
        eleccion = "Traicionar"
    else:
        print("Opción inválida.")
        return enviar_eleccion()  # Vuelve a pedir la opción si no es válida

    # Envía la elección a una celda de la hoja
    worksheet.update("A1", [[eleccion]])  # Asegúrate de pasar el valor como una lista de listas

    print(f"Se ha registrado '{eleccion}' en la hoja de cálculo.")

# Ejecuta el programa
enviar_eleccion()
