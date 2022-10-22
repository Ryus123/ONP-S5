"""---------------------------------IMPORT------------------------------------"""
from cProfile import label
import os
from turtle import color, position
import matplotlib.pyplot as plt
import numpy as np
import random
import pandas as pd

"""---------------------------------EXERCICE------------------------------------"""

"Utilisation de (def :) pour éviter que la machine execute des calculs non nécessaire à répétition"

###Exercice 1
#--1. Tracer la cos(x) sur [0; 10pie] avec linspace
t = np.linspace(0,10*np.pi)
def f_cos(x):
    f_cos = np.cos(x)
    plt.plot(f_cos)
    plt.show()
#f_cos(t)

#--2. Tracer différents graphiques (minimum 4) de la fonction ci-dessus
couleur = ["red", "orange", "yellow", "green"]
def graph_multi():
    for i in range(len(couleur)):
        t2 = np.linspace(0, 10 * np.pi, random.randrange(10, 100))
        f_cos2 = np.cos(t2)
        plt.subplot(2,2,i+1)
        plt.plot(f_cos2, couleur[i])
    plt.show()
#graph_multi()

#--3. Superposer sur le graphe de la question 1 le tracé de la fonction 𝑦
def f_y(x):
    f_y = np.exp(-x/10)*np.cos(x)
    plt.plot(x,np.cos(x),"b",label='cos(x)')
    plt.plot(x,f_y,"r",label='f_y(x)')
    plt.legend()
    plt.grid()
    plt.xlabel("Axe des x")
    plt.ylabel("Valeur de f(x)")
    plt.title("Supperposition f_cos et f_y")
    plt.show()
#f_y(t)

###Exercice 2
#--1.
def trace_f(t,x,y, col1, col2): ###Evite de réécrire 3 fois les mêmes ligne
    plt.plot(t, x, col1, label="x(t)")
    plt.plot(t, y, col2, label="y(t)")
    plt.grid()
    plt.xlabel("Axe des x")
    plt.ylabel("Valeur de f(x)")
    plt.title("Supperposition x(t) et y(t)")
    plt.show()

def f_xy1():
    txy1= np.linspace(0,2*np.pi)
    x1 = np.sin(txy1)/(1+np.cos(txy1)**2)
    y1 = (np.sin(txy1)*np.cos(txy1))/(1+np.cos(txy1)**2)
    trace_f(txy1, x1, y1, "y","g")
#f_xy1()

#--2.
def f_xy2():
    txy2 = np.linspace(0, 10*np.pi)
    x2 = txy2*np.cos(txy2)
    y2 = txy2*np.sin(txy2)
    trace_f(txy2, x2, y2, "r","b")
#f_xy2()

#--3.
def f_xy3():
    txy3 = np.linspace(0, 2*np.pi)
    x3 = 16*np.sin(txy3)**3
    y3 = 13*np.cos(txy3) - 5*np.cos(2*txy3) - 2*np.cos(3*txy3) - np.cos(4*txy3)
    trace_f(txy3, x3, y3, "g", "orange")
#f_xy3()

###EXERCICE 3
#--1. 
chm = os.getcwd()+"\DataTD\DataTD5\company_sales_data.csv"
Donnees = pd.read_csv(chm, delimiter=",")
df = pd.DataFrame(Donnees)
#--2.

"""Graphe company profit per month"""
def graph1():
    x = df["month_number"]
    y = df["total_profit"]
    plt.plot(x,y,"b")
    plt.xlabel("Month number")
    plt.ylabel("Profit in dollar")
    plt.title("Company profit per month")
    plt.show()
#graph1()

"""Graphe Company Sales data of last year"""
def graph2():
    x = df["month_number"]
    y = df["total_profit"]
    plt.plot(x,y,"r", linewidth=3, linestyle="--",marker="o", markerfacecolor="k", markersize=7, label="Profit data of last year")
    plt.legend(loc="lower right")
    plt.xlabel("Month number")
    plt.ylabel("Profit in dollar")
    plt.title("Company Sales data of last year")
    plt.show()
#graph2()

"""Graphe Tooth paste Sales data"""
def graph3():
    x = df["month_number"]
    y = df["toothpaste"]
    plt.plot(x,y, "o", label="Tooth paste Sales data")
    plt.grid(linestyle="--")
    plt.xlabel("Month Number")
    plt.ylabel("Number of units Sold")
    plt.title("Tooth paste Sales data")
    plt.legend(loc="upper left")
    plt.show()
#graph3()

"""Graphe Profit data"""
def graph4():
    plt.hist(df["total_profit"], bins= np.arange(150000, 325001, 25000), label="Profit data")
    plt.legend(loc="upper right")
    plt.xlabel("profit range in dollar")
    plt.ylabel("Actual Profit in dollar")
    plt.title("Profit data")
    plt.grid(linestyle="--", color="b", axis="y")
    plt.show()
#graph4()

"""BoxPlot Profit in dollar"""
def graph5():
    plt.boxplot(df["total_profit"], vert=False)
    plt.title("BoxPlot Profit in dollar")
    plt.show()
#graph5()

"""Sales data"""
def graph6():
    l = ["facecream", "facewash", "toothpaste", "bathingsoap", "shampoo", "moisturizer"]
    l_col = ["b","orange", "green", "red", "purple", "brown"]
    for i in range(6):
        nom = l[i]
        plt.plot(df["month_number"],df[nom], l_col[i],linewidth=3,marker="o", markerfacecolor=l_col[i], markersize=7, label=nom+" Sales Data")
        plt.legend(loc="upper left")
    plt.xlabel("Month Number")
    plt.ylabel("Sales units in number")
    plt.title("Sales data")
    plt.show()
#graph6()

"""Facewash and facecream sales data"""
def graph7():
    x,fc,fw = df["month_number"], df["facecream"], df["facewash"]
    plt.bar(x-0.1,fc,width=0.2, color="b", label="Face cream sales data")
    plt.bar(x+0.1,fw, width=0.2, color="orange", label="Face Wash sales data")
    plt.legend(loc="upper left")
    plt.grid(linestyle="--", color="b")
    plt.xlabel("Month Number")
    plt.ylabel("Sales units in number")
    plt.title("Facewash and facecream sales data")
    plt.show()
#graph7()