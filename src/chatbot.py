class Canchabot:

    def __init__(self):

        self.opciones = {

        "inicio":{
            "mensaje": "Bienvendios al Canchabot ¿Como te pudo ayudar?",
            "opciones": [
                "1. Avellaneda"
                "2. La Boca"
                "3. Nuñez"
                "4. La Paternal"
                "5. Liniers"
                "6. Salir"
            ]
        },

        "Avellaneda":{
            "1. Libertadores de America Ricardo E. Bochini"
            "2. Estadio Juan Domingo Peron (Cilindro)"
            "3. Estadio Julio Humberto Grondona"
            "4. Salir"
        },

        "La Boca": {
            "1.Estadio Alberto J. Armando (Bombonera)"
            "2. Salir"
        },

        "Nuñez": {
            "1. Estadio Mâs Monumental"
            "2. Estadio Juan Pasquale"
        },

        "La Paternal":{
            "1. Estadio Diego Armando Maradona"
        },

        "Liniers":{
            
            "1. Estadio José Amalfitani"
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
            print (opcion)

        
    
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
        elif self.estado_actual == "Salir":
            if opcion == "6":
                self.estado_actual = "inicio"
            else:
                self.estado_actual = self.options[self.estado_actual]["opciones"][int(opcion) - 1].split (". ")[1]
       




    def iniciar_chat(self):
        while self.estado_actual != "Salir":
            self.mostrar_mensaje()
            entrada_usuario = input("Elija una opción: ")
            self.entrada(entrada_usuario)
            self.entrada(opcion)


Canchabot = Canchabot()
Canchabot.iniciar_chat()
