import matplotlib.pyplot as plt
from tkinter import *
from tkinter import ttk
import webbrowser
corFundo = "#1e1e1e"
root = Tk()
root.title("Analise de Estudo de Casos")
root.geometry("400x400")
root.wm_resizable(False, False)
root.configure(background=corFundo)
title = Label(root, text="Analise de Estudos de Casos", bg=corFundo, fg="white", font=("Arial", 18, "bold"))
title.place(relx=0.5, rely=0.3, anchor=CENTER)

IFPBLogoImg = PhotoImage(file="IFPBLOGO.png")

def Avaliacao01():
	dados = [28.19, 31.64] # Segurança Desabilitada
	labels = ['Desabilitada', 'Habilitada']# CMM = Consumo Maximo de Memoria
	fig1, ax1 = plt.subplots()
	ax1.pie(dados, labels=labels, autopct='%1.1f%%', shadow=False, startangle=90)
	ax1.axis('equal')
	plt.title("Consumo maximo de memoria na aplicação (10Min)")
	plt.show()

def Avaliacao02():
	dados = [1625.00, 1687.50] # Segurança Desabilitada
	labels = ['Desabilitada', 'Habilitada']# CMM = Consumo Maximo de Memoria
	fig1, ax1 = plt.subplots()
	ax1.pie(dados, labels=labels, autopct='%1.1f%%', shadow=False, startangle=90)
	ax1.axis('equal')
	plt.title("Tempo Efetivo de Processamento (5Min)")
	plt.show()

def Avaliacao03():
	dados = [1000, 52.77, 17.96, 41.0, 525.0, 50.0, 47.0]
	labels = ["Requisições", "Media", "Desvio Padrao", "Min", "Max", "Med", "Mod"]
	fig1, ax1 = plt.subplots(figsize=(6,5))
	ax1.pie(dados, labels=labels, autopct='%1.1f%%', shadow=False, startangle=90, pctdistance=0.85)
	ax1.axis('equal')
	ax1.legend()
	plt.title("Avaliação do Tempo de resposta para obtenção do token")
	
	plt.show()

def Artigo():
	webbrowser.open('https://drive.google.com/file/d/1CVwWWo85v_VN0rbq79vv4Scbt9064STV/view?usp=sharing')

ava01Btn = ttk.Button(root, text="Ver Avaliação 01", command=Avaliacao01)
ava01Btn.place(relx=0.20, rely=0.5, anchor=CENTER)

ava02Btn = ttk.Button(root, text="Ver Avaliação 02", command=Avaliacao02)
ava02Btn.place(relx=0.48, rely=0.5, anchor=CENTER)

ava03Btn = ttk.Button(root, text="Ver Avaliação 03", command=Avaliacao03)
ava03Btn.place(relx=0.75, rely=0.5, anchor=CENTER)

DocBtn = ttk.Button(root, text="Ver Artigo", command=Artigo, width=40)
DocBtn.place(relx=0.48, rely=0.6, anchor=CENTER)

IFPBLogoLbl = Label(root, image=IFPBLogoImg, bg=corFundo, bd=0)
IFPBLogoLbl.place(relx=0.5, rely=1, anchor=S)

root.mainloop()



