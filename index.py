
import tkinter
import math

ventana = tkinter.Tk()
ventana.geometry("400x300")

'''
Para añadir una propiedad a una variable añadimos usamos tkinter.loQueQueremosUsar y la primera letra debe 
debe ser en mayusculas
'''


etiqueta = tkinter.Label( text = 'Ingresos de Gloria')
etiqueta.pack()
cajaTexto1 = tkinter.Entry(ventana)
cajaTexto1.pack()

etiqueta = tkinter.Label( text = 'Ingresos de Miguel')
etiqueta.pack()
cajaTexto2 = tkinter.Entry(ventana)
cajaTexto2.pack()

etiqueta = tkinter.Label( text = 'Gastos totales del mes')
etiqueta.pack()
cajaTexto3 = tkinter.Entry(ventana)
cajaTexto3.pack()

def crearVariables():
        persona1 = cajaTexto1.get()
        persona2 = cajaTexto2.get()
        gastos = cajaTexto3.get()
        ingresos = (persona1 + persona2)
        porcentaje = int(ingresos) / 100
        mp = math.ceil( int(persona2) / porcentaje)
        total1 = math.ceil(int(gastos) * mp / 100)
        total2 = int(gastos) - total1
        print (total1, total2)
'''
Habia fallado añadiendo () al final de la funcion en el command por eso no me retornaba nada.
'''
boton1 = tkinter.Button( text = 'Pulsa para comenzar', command = crearVariables)
boton1.pack()



ventana.mainloop()