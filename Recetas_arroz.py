import json

# Especificamos el nombre del archivo JSON
nombre_archivo = 'receta_arroz.json'

# Creamos un diccionario con la receta
receta = {
    "nombre": "Arroz Blanco",
    "raciones": 4,
    "ingredientes": {
        "arroz blanco de grano mediano o largo": "1 taza o 200 g",
        "agua": "2 tazas o 500 ml",
        "sal": "1/2 cucharadita o 3 g",
        "aceite o manteca": "1 cucharada o 15 g"
    },
    "instrucciones": [
        "Enjuaga el arroz bajo agua fría hasta que el agua salga clara.",
        "En una olla, calienta el aceite o manteca a fuego medio.",
        "Agrega el arroz y sofríe durante unos minutos hasta que esté ligeramente dorado.",
        "Añade el agua y la sal a la olla.",
        "Cuando el agua comience a hervir, reduce el fuego al mínimo y tapa la olla.",
        "Cocina durante 18-20 minutos o hasta que el agua se haya absorbido.",
        "Retira del fuego y deja reposar durante 5 minutos antes de servir."
    ]
}

# Abrimos el archivo en modo escritura
with open(nombre_archivo, 'w', encoding='utf-8') as f:
    # Usamos json.dump para escribir el diccionario en el archivo
    json.dump(receta, f, ensure_ascii=False, indent=4)

print(f"Archivo '{nombre_archivo}' creado exitosamente.")

class RecetaArrozBlanco:
    def __init__(self):
        self.nombre = receta["nombre"]
        self.raciones = receta["raciones"]
        self.ingredientes = receta["ingredientes"]
        self.instrucciones = receta["instrucciones"]

    def mostrar_ingredientes(self):
        """Muestra los ingredientes de la receta."""
        print("Ingredientes para", self.nombre + ":")
        for ingrediente, cantidad in self.ingredientes.items():
            print(f"- {ingrediente}: {cantidad}")

    def mostrar_instrucciones(self):
        """Muestra las instrucciones de la receta."""
        print("Instrucciones para", self.nombre + ":")
        for instruccion in self.instrucciones:
            print(instruccion)

    def calcular_ingredientes(self):
        """Calcula los ingredientes necesarios según las raciones deseadas."""
        while True:  # Bucle para validar la entrada del usuario
            try:
                raciones_deseadas = int(input("Introduce el número de raciones deseado: "))
                if raciones_deseadas > 0:
                    break
                else:
                    print("Por favor, introduce un número mayor que 0.")
            except ValueError:
                print("Por favor, introduce un número válido.")

        factor = raciones_deseadas / self.raciones
        ingredientes_calculados = {}
        
        for ingrediente, cantidad in self.ingredientes.items():
            # Convertir cantidad a gramos si es necesario
            if 'taza' in cantidad:
                cantidad_num = float(cantidad.split()[0]) * 200 * factor  # Suponiendo que 1 taza = 200g
                ingredientes_calculados[ingrediente] = f"{cantidad_num:.2f} g"
            elif 'ml' in cantidad:
                cantidad_num = float(cantidad.split()[0]) * factor  # ml se multiplica directamente
                ingredientes_calculados[ingrediente] = f"{cantidad_num:.2f} ml"
            elif 'cucharada' in cantidad:
                cantidad_num = float(cantidad.split()[0]) * factor  # cucharaditas se multiplican directamente
                ingredientes_calculados[ingrediente] = f"{cantidad_num:.2f} cucharaditas"
            elif 'cucharada' in cantidad:
                cantidad_num = float(cantidad.split()[0]) * factor  # cucharadas se multiplican directamente
                ingredientes_calculados[ingrediente] = f"{cantidad_num:.2f} cucharadas"

        # Imprimir los ingredientes calculados
        print(f"Ingredientes para {raciones_deseadas} raciones de {self.nombre}:")
        for ingrediente, cantidad in ingredientes_calculados.items():
            print(f"- {ingrediente}: {cantidad}")
        
        return ingredientes_calculados

# Crear una instancia de la receta y mostrar los ingredientes e instrucciones
receta_arroz = RecetaArrozBlanco()
receta_arroz.mostrar_ingredientes()
receta_arroz.mostrar_instrucciones()
receta_arroz.calcular_ingredientes()