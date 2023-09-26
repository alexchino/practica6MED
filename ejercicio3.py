# Elabore una clase estudiante, defina los atributos nombre, apellido, carnet y
# carrera. Utilice un constructor para inicializar los atributos, ademas elabore
# funciones para actualizar los valores de los atributos (nombre, apellido, carnet y
# carrera).
class Estudiante:
    def __init__(self, nombre, apellido, carnet, carrera):
        self.nombre = nombre
        self.apellido = apellido
        self.carnet = carnet
        self.carrera = carrera

    def actualizar_nombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre

    def actualizar_apellido(self, nuevo_apellido):
        self.apellido = nuevo_apellido

    def actualizar_carnet(self, nuevo_carnet):
        self.carnet = nuevo_carnet

    def actualizar_carrera(self, nueva_carrera):
        self.carrera = nueva_carrera

    def __str__(self):
        return f"Nombre: {self.nombre}\nApellido: {self.apellido}\nCarnet: {self.carnet}\nCarrera: {self.carrera}"


estudiante1 = Estudiante("alex", "chavez", "12345", "desarrollo de sortware")
print(estudiante1)

estudiante1.actualizar_nombre("Gilber")
estudiante1.actualizar_carrera("Ingeniería civil")
print("\nDespués de actualizar datos:")
print(estudiante1)
