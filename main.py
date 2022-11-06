from tkinter import Tk, Button, Entry, Label
# Configuración ventana principal
root = Tk()
root.title("Calculadora POO")
root.resizable(0,0)
root.geometry("290x252")
#root.geometry("400x400")
# Configuración pantalla de salida 
pantalla = Label(root, width=19, bg="black", fg="white", borderwidth=0, font=("arial", 18, "bold"))
pantalla.grid(row=0, column=0, columnspan=4, padx=1, pady=1)

#COMANDOS

base = []
operando = []
numeros = []
final = ""

def num1():
    res = "1"
    pantalla.configure(text = res)
    base.append("1")
    numeros.append(1)
def num2():
    res = "2"
    pantalla.configure(text = res)
    base.append("2")
    numeros.append(2)
def num3():
    res = "3"
    pantalla.configure(text = res)
    base.append("3")
    numeros.append(3)
def num4():
    res = "4"
    pantalla.configure(text = res)
    base.append("4")
    numeros.append(4)
def num5():
    res = "5"
    pantalla.configure(text = res)
    base.append("5")
    numeros.append(5)
def num6():
    res = "6"
    pantalla.configure(text = res)
    base.append("6")
    numeros.append(6)
def num7():
    res = "7"
    pantalla.configure(text = res) 
    base.append("7") 
    numeros.append(7)  
def num8():
    res = "8"
    pantalla.configure(text = res)
    base.append("8")
    numeros.append(8)
def num9():
    res = "9"
    pantalla.configure(text = res)
    base.append("9")
    numeros.append(9)


def mas():
    res = "+"
    pantalla.configure(text = res)
    base.append("+")
    operando.append("+")
def menos():
    res = "-"
    pantalla.configure(text = res)
    base.append("-")
    operando.append("-")
def prod():
    res = "*"
    pantalla.configure(text = res)
    base.append("*")
    operando.append("*")
def divis():
    res = "/"
    pantalla.configure(text = res)
    base.append("/")
    operando.append("/")
def punt():
    res = "."
    pantalla.configure(text = res)
    base.append(".")
    numeros.append(".")
# Funcion operaciones

def operacion(a, b, c):
    if c == "+":
        return (a+b)
    if c == "-":
        return  (a-b) 
    if c == "*":
        return (a*b)
    if c == "/":
        return (a/b)

def listastring(s):
    str1 = ""
    for l in s:
        str1 += str(l)
    return str1

##otra = (listastring(base)).split(opera)

def igual():
    x = (listastring(base)).split(operando[0])


    prim = x[0]
    segu = x[1]
    base.append("=")
    #base.append(strfinal)
    #base.append(x)
    base.append(operacion(float(prim), float(segu), operando[0]))
    pantalla.configure(text = base)

# Configuración botones
#NUMEROS
boton_1 = Button(root, text="1", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=num1).grid(row=1, column=0, padx=1, pady=1, sticky="w")
boton_2 = Button(root, text="2", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=num2).grid(row=1, column=1, padx=1, pady=1, sticky= "w")
boton_3 = Button(root, text="3", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=num3).grid(row=1, column=2, padx=1, pady=1, sticky= "w")
boton_4 = Button(root, text="4", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=num4).grid(row=2, column=0, padx=1, pady=1, sticky= "w")
boton_5 = Button(root, text="5", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=num5).grid(row=2, column=1, padx=1, pady=1, sticky= "w")
boton_6 = Button(root, text="6", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=num6).grid(row=2, column=2, padx=1, pady=1, sticky= "w")
boton_7 = Button(root, text="7", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=num7).grid(row=3, column=0, padx=1, pady=1, sticky= "w")
boton_8 = Button(root, text="8", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=num8).grid(row=3, column=1, padx=1, pady=1, sticky= "w")
boton_9 = Button(root, text="9", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=num9).grid(row=3, column=2, padx=1, pady=1, sticky= "w")
#OPERADORES
boton_igual = Button(root, text="=", width=20, height=3, bg="red", fg="white", borderwidth=0, cursor=" hand2", command=igual).grid(row=4, column=0, columnspan=2, padx=1, pady=1, sticky= "w")
boton_punto = Button(root, text=".", width=9, height=3, bg="spring green", fg="black", cursor="hand2", borderwidth=0, command=punt).grid(row=4, column=2, padx=1, pady=1, sticky= "w")
boton_mas = Button(root, text="+", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2", command=mas).grid(row=1, column=3, padx=1, pady=1, sticky= "w")
boton_menos = Button(root, text="-", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2", command=menos).grid(row=2, column=3, padx=1, pady=1, sticky= "w")
boton_multiplicacion = Button(root, text="*",  width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2", command=prod).grid(row=3, column=3, padx=1, pady=1, sticky= "w")
boton_division = Button(root, text="/", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2", command=divis).grid(row=4, column=3, padx=1, pady=1, sticky= "w")

root.mainloop()
