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
    worksheet.update("A2", [[eleccion]])  # pasar el valor como una lista de listas

    print(f"Se ha registrado '{eleccion}' en la hoja de cálculo.")


#Preguntar como considera al otro prisionero
print("¿Cómo consideras al otro prisionero?")
print("1. Amigo")
print("2. Cae mal")
print("3. X")
amigo = input("Selecciona una opción: ")
if amigo == "1":
    print("\n\n\n - - - - - - - - - - - - - - - - - - - - - - - -")
    print("Recuerda que es amigo, no te va a traicionar")
    relacion = "Amigo"
elif amigo == "2":
    print("\n\n\n - - - - - - - - - - - - - - - - - - - - - - - -")
    print("Traiciona, recuerda que te robó tu gansito")
    relacion = "Enemigo"
else:
    print("\n\n\n - - - - - - - - - - - - - - - - - - - - - - - -")
    print("Es posible que te traicione, elige sabiamente")
    relacion = "X"
worksheet.update("A4", [[relacion]])

# Ejecuta el programa
enviar_eleccion()
