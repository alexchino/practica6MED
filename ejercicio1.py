class Articulo:
    def __init__(self, nombre, cantidad, precio):
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def vender(self, cantidad_vendida):
        if cantidad_vendida <= 0:
            return "La cantidad vendida debe ser mayor que cero."
        elif cantidad_vendida > self.cantidad:
            return "No hay suficientes unidades disponibles para la venta."
        else:
            self.cantidad -= cantidad_vendida
            total_venta = cantidad_vendida * self.precio
            return f"Se vendieron {cantidad_vendida} unidades de {self.nombre}. Total a pagar: ${total_venta}"

    def agregar_stock(self, cantidad_nueva):
        if cantidad_nueva <= 0:
            return "La cantidad a agregar al stock debe ser mayor que cero."
        else:
            self.cantidad += cantidad_nueva
            return f"Se agregaron {cantidad_nueva} unidades de {self.nombre} al stock. Stock total: {self.cantidad} unidades."

    def __str__(self):
        return f"Nombre: {self.nombre}\nCantidad en stock: {self.cantidad}\nPrecio por unidad: ${self.precio}"

if __name__ == "__main__":

    producto1 = Articulo("Camisa", 20, 25.0)

 
    print("Información del artículo:")
    print(producto1)

 
    print("\nVenta:")
    resultado_venta = producto1.vender(5)
    print(resultado_venta)

 
    print("\nAgregar stock:")
    resultado_stock = producto1.agregar_stock(10)
    print(resultado_stock)

   
    print("\nInformación actualizada del artículo:")
    print(producto1)
