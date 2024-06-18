import os, json
from datetime import datetime
from usuario import Usuario

instancias = []

CURDIR = os.path.dirname(os.path.abspath(__file__))
FILENAME = "usuarios.txt"
FILE = os.path.join(CURDIR, FILENAME)

try:
    with open(FILE) as file:
        linea = file.readline()

        while linea:
            usuario = json.loads(linea)
            instancias.append(
			    Usuario(usuario.get("nombre"), usuario.get("apellido"), usuario.get("email"), usuario.get("genero"))
		    )
            linea = file.readline()

        for usuario in instancias:
            print()
            print("Usuario:", usuario.nombre)
            print("Apellido:", usuario.apellidos)
            print("Email:", usuario.email)
            print("Genero:", usuario.genero)
        
except Exception as e:
    with open("error.log", "a+") as log:
        log.seek(0)
        print(log.read())
        now = datetime.now()
        log.write(f"[{now.strftime('%Y-%m-%d %H:%M:%S')}] ERROR: {e}\n")
        log.seek(0)
        print(log.read())