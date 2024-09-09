class Usuario:
    def __init__(self, nombre_completo, nickname, clave, tipo, fechadecreacion):
        self.datos = {
            "nombre completo": nombre_completo,
            "nickname": nickname,
            "clave": clave,
            "tipo": tipo,
            "fecha de creacion": fechadecreacion
        }
def menu():
    usuarios = []
    while True:
        print("1. Agregar usuario")
        print("2. Buscar usuario")
        print("3. Eliminar usuario")
        print("4. Salir")
        opcion = int(input("Ingrese su opción: "))
        
        if opcion == 1:
            nombrecompleto = input("Ingrese nombre: ")
            nickname = input("ingrese nickname: ")
            clave = input("Ingrese clave: ")
            tipo = input("Ingrese tipo: ")
            fechadecreacion = input("ingrese la fecha de cracion: ")
            nuevo_usuario = Usuario(nombrecompleto, nickname, clave, tipo, fechadecreacion)
            usuarios.append(nuevo_usuario)
            print("Usuario agregado correctamente")
        
        elif opcion == 2:
            nombre = input("Ingrese nombre de usuario a buscar: ")
            for usuario in usuarios:
                if usuario.datos["nombre completo"] == nombre:
                    print("Usuario encontrado:", usuario.datos)
                    break
                else:
                    print("Usuario no encontrado.")
        elif opcion == 3:
            nombre = input("Ingrese nombre de usuario a eliminar: ")
            for usuario in usuarios:
                if usuario.datos["nombre completo"] == nombre:
                    usuarios.remove(usuario)
                    print("Usuario eliminado.")
                    break
                else:
                    print("Usuario no encontrado.")
        elif opcion == 4:
            print("Finalizado")
            break
        else:
            print("Opción no válida")
menu()                        