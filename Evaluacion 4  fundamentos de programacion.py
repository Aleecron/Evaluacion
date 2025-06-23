usuarios = {"Nombres": [], "Sexos": [], "Contraseñas": []}

def ingresarusuario(usuarios):
    while True:
        print("---INGRESAR USUARIO----")
        nombre = input("Escriba su nombre: ").capitalize()
        if nombre in usuarios["Nombres"]:
            print("Usuario ya existe. Intento otro")
            return
        sexo = input("INGRESE SU SEXO, SOLO SE ACEPTARA F O M:").upper()
        if sexo not in ("F", "M"):
            print("Seleccione solo F o M")
            return
        contraseña = input("Ingrese su contraseña, mínimo 8 caracteres y al menos 1 número: ").strip() 
        if len(contraseña) < 8 or not any(numero.isdigit() for numero in contraseña): 
            print("Contraseña Invalida") 
            return
        else:
            print("Contraseña valida\n" 
                  "usario ingresado con exito!")
        usuarios["Nombres"].append(nombre)
        usuarios["Sexos"].append(sexo)
        usuarios["Contraseñas"].append(contraseña)
      
        

def buscarusuario(usuarios):
    buscar_usuario = input("Indique el nombre del usuario que desea buscar: ").capitalize()
    if buscar_usuario in usuarios["Nombres"]:
        indice = usuarios["Nombres"].index(buscar_usuario)
        print(f"Usuario: {buscar_usuario}, el Sexo del usuario es : {usuarios['Sexos'][indice]} y la contraseña es {usuarios["Contraseñas"][indice] }")
    else:
        print("Usuario no encontrado.")

def eliminar_usuario(usuarios):
    eliminar = input("Indique el nombre del usuario que desea eliminar: ").capitalize()
    if eliminar in usuarios["Nombres"]:
        indice = usuarios["Nombres"].index(eliminar)
        for indice in usuarios:
            usuarios[indice].pop(indice)
        print("Usuario eliminado con éxito!")
    else:
        print("El usuario no se encuentra.")

def menu():
    while True:
        try:
            print("1.- Ingresar usuario")
            print("2.- Buscar usuario")
            print("3.- Eliminar usuario")
            print("4.- Salir")
            opcion = int(input("Seleccione Una Opción: "))
            if opcion == 1:
                ingresarusuario(usuarios)
            elif opcion == 2:
                buscarusuario(usuarios)
            elif opcion == 3:
                eliminar_usuario(usuarios)
            elif opcion == 4:
                print("Programa terminado...")
                break
            else:
                print("Debe ingresar una opción válida!")
        except ValueError:
            print("Valor no válido")
menu()