import tkinter as tk
import tkinter.font as tkFont
import matplotlib.pyplot as plt
import control.matlab as ml



#Main window
window = tk.Tk()
window.title("Bode Diagram")
window.geometry("600x300")
window.resizable(True, True)
fontStyle = tkFont.Font(family="Times", size=20, weight="bold")

#Functions
def funcion(num, den):
    G = ml.tf(num, den)  # Funcion de transferencia
def formarpolinomio():
    polinomio = list(map(float, entradagpoly.get().split())) #Obtener el polinomio separado
    g1 = int(entradag1.get())  #Grado Numerador
    g2 = int(entradag2.get()) #Grado Denominador
    formar(g1, g2, polinomio)  #Formacion de la funcion H(s)
def formar(g1, g2, pol):
    num = [g1 + 1] #Grado Numerador +1 Vector
    den = [g2 + 1] #Grado Denominador +1 Vector
    for j in range(0, len(pol), 1): #Asignacion de los coeficientes para el numerador y denominador
        if j <= g1:
            num.append(pol[j]) #Formación del numerador
        else:
            den.append(pol[j]) #Formación del numerador
    num.pop(0) #Elimininar el primero del elemento del vector para que se ajuste el grado numerador
    den.pop(0) #Elimininar el primero del elemento del vector para que se ajuste el grado denominador
    # print(num) #print the numerator
    # print(den)#print the denominator

    bode(num, den) #Partes del diagrama de bode

def bode(num, den):
    G = ml.tf(num, den) #Funcion de transferencia
    #print(G)  # Imprimir la fraccion total
    polo = ml.pole(G)  # Imprimir polos
    cero = ml.zero(G)  # Imprimir ceros
    mag, phase, w = ml.bode(G) #Magnitud y fase del diagrama de bode
    showcalculos(polo, cero,G) #Impresion de los polos y ceros en la funcion showcalculos


def show():
    plt.show()

def showcalculos(p, c,fun):
    print(fun)
    window = tk.Tk()
    window.title("Calculos")
    window.geometry("600x300")
    window.resizable(True, True)
    fontStyle = tkFont.Font(family="Times", size=20, weight="bold")
    frame2 = tk.Frame(window, borderwidth=5, relief=tk.SUNKEN, bg="pale green")
    frame2.pack(pady=10)
    frame2.config(bg="lightblue")
    frame2.config(width=600, height=600)
    e1 = tk.Label(frame2, text="Polos", bg="pale green", fg="blue", cursor="trek", font=fontStyle)
    e1.pack()
    polos = tk.Label(frame2, text=p)
    polos.pack() #Polos
    e2 = tk.Label(frame2, text="Ceros", bg="pale green", fg="blue", cursor="trek", font=fontStyle)
    e2.pack()
    ceros = tk.Label(frame2, text=c)
    ceros.pack() #Ceros
    botonbode = tk.Button(window, text="Mostrar Diagrama", command=show) #Diagrama de bode magnitud y fase
    botonbode.pack()
    window.mainloop()


e1 = tk.Label(window, text="Bode Diagram", bg="pale green", fg="blue", width=20, font=fontStyle, cursor="trek")
e1.pack()
frame = tk.Frame(window, borderwidth=5, relief=tk.SUNKEN, bg="pale green")
frame.pack(pady=10)
frame.config(bg="lightblue")
frame.config(width=800, height=800)
e2 = tk.Label(frame, text="Grado del numerador", bg="pale green", fg="blue", cursor="trek")
e2.pack()
entradag1 = tk.Entry(frame)
entradag1.pack()
e3 = tk.Label(frame, text="Grado del denominador", bg="pale green", fg="blue", cursor="trek")
e3.pack()
entradag2 = tk.Entry(frame)
entradag2.pack()
e4 = tk.Label(frame, text="!!!Para potencias usar e0(n)!!!", bg="pale green", fg="blue", cursor="trek")
e4.pack()
e5 = tk.Label(frame,
              text="Ingrese los coeficientes (Primero del numerador y Segundo Denominador (Usar espacios entre cada "
                   "uno)",
              bg="pale green", fg="blue", cursor="trek")
e5.pack()
entradagpoly = tk.Entry(frame)
entradagpoly.pack()
botoncalculos = tk.Button(frame, text="Calcular", command=formarpolinomio)
botoncalculos.pack()

window.mainloop()
