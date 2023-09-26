# Usando clases elabore un programa para simular una cuenta de usuario, asigne
# los atributos y métodos que considere necesarios
class Usuario:
    def __init__(self, nombre, apellido, correo, saldo_inicial=0.0):
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.saldo = saldo_inicial

    def depositar(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad
            return f"Depósito de ${cantidad} realizado con éxito. Saldo actual: ${self.saldo}"
        else:
            return "La cantidad a depositar debe ser mayor que cero."

    def retirar(self, cantidad):
        if cantidad > 0:
            if cantidad <= self.saldo:
                self.saldo -= cantidad
                return f"Retiro de ${cantidad} realizado con éxito. Saldo actual: ${self.saldo}"
            else:
                return "Saldo insuficiente para realizar el retiro."
        else:
            return "La cantidad a retirar debe ser mayor que cero."

    def consultar_saldo(self):
        return f"Saldo actual de {self.nombre} {self.apellido}: ${self.saldo}"

    def __str__(self):
        return f"Nombre: {self.nombre} {self.apellido}\nCorreo: {self.correo}\nSaldo: ${self.saldo}"


if __name__ == "__main__":
    
    usuario1 = Usuario("alexander", "canales", "alex@icluod.com", 9000.0)

    
    print("Información del usuario:")
    print(usuario1)

    
    print("\nDepósito:")
    resultado_deposito = usuario1.depositar(900)
    print(resultado_deposito)

    
    print("\nRetiro:")
    resultado_retiro = usuario1.retirar(500)
    print(resultado_retiro)

    
    print("\nConsulta de saldo:")
    saldo_actual = usuario1.consultar_saldo()
    print(saldo_actual)

    
    print("\nInformación actualizada del usuario:")
    print(usuario1)
