from tkinter import *
from math import *

ventana = Tk()
ventana.title("Calculadora CP 1.0")
ventana.geometry("400x550")
ventana.resizable(False,False)
ventana.configure(bg="gray42")
ventana.iconbitmap('calcu.ico')

operador ="" #contiene la operacion a evaluar
texto_pantalla= StringVar() #colocar textvariable en la pantalla(entry)


#Funcionalidades botones------------------------------
def limpiar():
    global operador
    operador = ""
    texto_pantalla.set("0")

def click(b):
    global operador
    operador += str(b)
    texto_pantalla.set(operador)

def resultado():
    global operador
    try:
        r=str(eval(operador))
    except:
        r="ERROR"
    texto_pantalla.set(r)

limpiar()
"""--------------------BOTONES-------------------------
Defino un patron grafico de botones para luego aplicar """

botonColor="gray99"
botonAncho=10
botonAlto=3
#--------------------primera fila-------------------------
boton0=Button(ventana, text=0, bg=botonColor,width=botonAncho,height=botonAlto, command=lambda:click(0)).grid(row=1, column=0, pady=10)
boton1=Button(ventana, text=1, bg=botonColor,width=botonAncho,height=botonAlto, command=lambda:click(1)).grid(row=1, column=1, pady=10)
boton2=Button(ventana, text=2, bg=botonColor,width=botonAncho,height=botonAlto, command=lambda:click(2)).grid(row=1, column=2, pady=10)
boton3=Button(ventana, text=3, bg=botonColor,width=botonAncho,height=botonAlto, command=lambda:click(3)).grid(row=1, column=3, pady=10)
#--------------------segunda fila-------------------------
boton4=Button(ventana, text=4, bg=botonColor,width=botonAncho,height=botonAlto, command=lambda:click(4)).grid(row=2, column=0, pady=10)
boton5=Button(ventana, text=5, bg=botonColor,width=botonAncho,height=botonAlto, command=lambda:click(5)).grid(row=2, column=1, pady=10)
boton6=Button(ventana, text=6, bg=botonColor,width=botonAncho,height=botonAlto, command=lambda:click(6)).grid(row=2, column=2, pady=10)
boton7=Button(ventana, text=7, bg=botonColor,width=botonAncho,height=botonAlto, command=lambda:click(7)).grid(row=2, column=3, pady=10)
#--------------------tercera fila-------------------------
boton8=Button(ventana, text=8, bg=botonColor,width=botonAncho,height=botonAlto, command=lambda:click(8)).grid(row=3, column=0, pady=10)
boton9=Button(ventana, text=9, bg=botonColor,width=botonAncho,height=botonAlto, command=lambda:click(9)).grid(row=3, column=1, pady=10)
botonPi=Button(ventana, text='Pi', bg=botonColor,width=botonAncho,height=botonAlto, command=lambda:click("pi")).grid(row=3, column=2, pady=10)
botoncoma=Button(ventana, text=",", bg=botonColor,width=botonAncho,height=botonAlto, command=lambda:click(',')).grid(row=3, column=3, pady=10)
#--------------------CUARTA fila-------------------------
botonsuma=Button(ventana, text='+', bg=botonColor,width=botonAncho,height=botonAlto, command=lambda:click('+')).grid(row=4, column=0, pady=10)
botonresta=Button(ventana, text='-', bg=botonColor,width=botonAncho,height=botonAlto, command=lambda:click('-')).grid(row=4, column=1, pady=10)
botonMulti=Button(ventana, text='*', bg=botonColor,width=botonAncho,height=botonAlto, command=lambda:click('*')).grid(row=4, column=2, pady=10)
botonDivi=Button(ventana, text="/", bg=botonColor,width=botonAncho,height=botonAlto, command=lambda:click('/')).grid(row=4, column=3, pady=10)
#--------------------quinta fila-------------------------
botonRaiz=Button(ventana, text='√', bg=botonColor,width=botonAncho,height=botonAlto, command=lambda:click('sqrt')).grid(row=5, column=0, pady=10)
botonClear=Button(ventana, text='CE', bg=botonColor,width=botonAncho,height=botonAlto, command=limpiar).grid(row=5, column=1, pady=10)
botonExp=Button(ventana, text='^', bg=botonColor,width=botonAncho,height=botonAlto, command=lambda:click('exp')).grid(row=5, column=2, pady=10)
botonIgual=Button(ventana, text="=", bg=botonColor,width=botonAncho,height=botonAlto, command=resultado).grid(row=5, column=3, pady=10)
#--------------------sexta fila-------------------------
botonParenAbre=Button(ventana, text='(', bg=botonColor,width=botonAncho,height=botonAlto, command=lambda:click('(')).grid(row=6, column=0, pady=10)
botonParenCierra=Button(ventana, text=')', bg=botonColor,width=botonAncho,height=botonAlto, command=lambda:click(')')).grid(row=6, column=1, pady=10)
botonMod=Button(ventana, text='Mod', bg=botonColor,width=botonAncho,height=botonAlto, command=lambda:click('%')).grid(row=6, column=2, pady=10)
botonLog=Button(ventana, text="Log", bg=botonColor,width=botonAncho,height=botonAlto, command=lambda:click('log')).grid(row=6, column=3, pady=10)

pantalla = Entry(ventana, font=("arial",20,"bold"), width=22, borderwidth=10,bg="CadetBlue1", textvariable=texto_pantalla)
pantalla.grid(row=0,column=0,columnspan=4,padx=20,pady=20)

ventana.mainloop()

