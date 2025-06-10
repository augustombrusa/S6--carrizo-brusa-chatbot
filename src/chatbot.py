class Canchabot:
    def __init__(self):
        self.opciones = {
            "inicio": {
                "mensaje": "Bienvenidos al Canchabot ¿Como te puedo ayudar?",
                "opciones": [
                    "1. Avellaneda",
                    "3. Nuñez",
                    "4. La Paternal",
                    "5. Liniers",
                    "6. Salir"
                ]
            },
            "Avellaneda": {
                "mensaje": "Opciones en Avellaneda:",
                "opciones": [
                    "1. Libertadores de America Ricardo E. Bochini",
                    "2. Estadio Juan Domingo Peron (Cilindro)",
                    "3. Estadio Julio Humberto Grondona",
                    "4. Salir"
                ]
            },
            "La Boca": {
                "mensaje": "Opciones en La Boca:",
                "opciones": [
                    "1. Estadio Alberto J. Armando (Bombonera)",
                    "2. Salir"
                ]
            },
            "Nuñez": {
                "mensaje": "Opciones en Nuñez:",
                "opciones": [
                    "1. Estadio Mâs Monumental",
                    "2. Estadio Juan Pasquale",
                ]
            },
            "La Paternal": {
                "mensaje": "Opciones en La Paternal:",
                "opciones": [
                    "1. Estadio Diego Armando Maradona",
                ]
            },
            "Liniers": {
                "mensaje": "Opciones en Liniers:",
                "opciones": [
                    "1. Estadio José Amalfitani",
                ]
            },
            "Salir": {
                "mensaje": "¡Gracias por usar Canchabot!",
                "opciones": []
            }
        }
        self.estado_actual = "inicio"

    def mostrar_mensaje(self):
        print(self.opciones[self.estado_actual]["mensaje"])
        if self.opciones[self.estado_actual]["opciones"]:
            for opcion in self.opciones[self.estado_actual]["opciones"]:
                print(opcion)

    def entrada(self, opcion):
        if self.estado_actual == "inicio":
            if opcion == "1":
                self.estado_actual = "Avellaneda"
            elif opcion == "2":
                self.estado_actual = "La Boca"
            elif opcion == "3":
                self.estado_actual = "Nuñez"
            elif opcion == "4":
                self.estado_actual = "La Paternal"
            elif opcion == "5":
                self.estado_actual = "Liniers"
            elif opcion == "6":
                self.estado_actual = "Salir"
        else:
            try:
                opcion_num = int(opcion)
                if 1 <= opcion_num <= len(self.opciones[self.estado_actual]["opciones"]):
                    nueva_opcion = self.opciones[self.estado_actual]["opciones"][opcion_num - 1]
                    if nueva_opcion == "Salir":
                        self.estado_actual = "inicio"  # Vuelve al menú principal
                    else:
                        self.estado_actual = nueva_opcion.split(". ")[1]  # Extrae el nombre del estado
                else:
                    print("Opción inválida. Por favor, elija una opción válida.")
            except (ValueError, IndexError):
                print("Opción inválida. Por favor, ingrese un número.")

    def iniciar_chat(self):
        while self.estado_actual != "Salir":
            self.mostrar_mensaje()
            entrada_usuario = input("Elija una opción: ")
            self.entrada(entrada_usuario)

# Instancia y ejecuta el chatbot
canchabot = Canchabot()
canchabot.iniciar_chat()