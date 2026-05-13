


class Tienda():
    def __init__(self):
        self.lista={
                }   
        
    def agregar(self):
        producto=input('Introduce nombre del producto\n')
        precio_producto=float(input('Introduce su precio\n'))
        self.lista[producto]=precio_producto
        
    def exportartxt(self):
        with open ('lista.txt','w',  ) as f: 
            
            f.write(str(self.lista))
    
    def i_pantalla(self):
        print('Lista de Precios 2026')
        print('---------------------')
        for clave,valor in self.lista.items():
            print(f'El precio de {clave} es de {valor}')
        print('\n')



mi_tienda=Tienda()


print('Opciones :\n')

print('1º Añadir datos a la lista\n' \
    '\n'
    '2º Imprimir por pantalla la lista\n' \
    '\n'
    '3º Exportar lista a un Documento.txt'\
    '\n'
    '\n'
    '4º Salr'\
    '\n')


Salir =False

while Salir == False:

    opcion=input('Seleccione una opcion\n')

    if opcion == '1':
        mi_tienda.agregar()
    if opcion== '2':
        mi_tienda.i_pantalla()
    if opcion == '3':
        mi_tienda.exportartxt()
    if opcion =='4':
        print('Gracias por usar nuestros servicios')
        Salir = True
    

