import tkinter as tk
from tkinter import *



class App(tk.Frame):
    def __init__(self,master=None):
        tk.Frame.__init__(self,master)
        self.grid()
        self.botao()
        self.edit()

    def edit(self):
        self.edit1=tk.Entry(self,width = 32)
        self.edit1["font"]=("Allstar","22")
        self.edit1.grid(row=1,column=1,columnspan=4)        

    def botao(self):
        # ao invez de criar todos botoes automaticamente, crio um ciclo for
        # para criar os botoes que estao dentro de uma lista
        
        botoes=["CE","C","◄","÷","7","8","9","X","4","5","6","-","1","2","3","+","+/-","0",",","="]
        linha = 2
        coluna =1
        
        for Bot in botoes:
            comando = lambda x=Bot : self.calcular(x)
            self.botao=tk.Button(self,text=Bot,height=1,width=7,command = comando )
            self.botao["font"]=("Allstar","20")
            if Bot.isnumeric():# se for um numero vai ter a cor branca se for caractere prata
                self.botao["bg"]="white"
            else:
                self.botao["bg"]="silver"
            self.botao.grid(row = linha, column =coluna) #posicionamento dos botoes no grid
            if coluna == 4:
                coluna = 1
                linha +=1
            else:
                coluna+=1


    def Resolve(self): #funçao responsavel por resolver matematicamente uma string
                        # tambem da alguns tratamentos para evitar erros, como por exemplo se a string for '5+'
                        # adiciona-se o 0 no final, e se tiver letras printa ENTRADA INVALIDA
        try:

            calculo = self.edit1.get()
            temp=""
            if not calculo[(len(calculo))-1].isnumeric():
                calculo+='0'
            for x in range(len(calculo)):
                if calculo[x] == 'X':
                    temp+="*"
                elif calculo[x] == '÷':
                    temp+="/"
                elif calculo[x] == ',':
                    temp+="."
                else:
                    temp+=str(calculo[x])
            resultado = eval(temp)
            resultado = str(resultado)
            temp2=""
            for x in range(len(resultado)):
                if resultado[x] == ".":
                    temp2+=","
                else:
                    temp2+=str(resultado[x])

                              
            return temp2

        except:
            return "ENTRADA INVALIDA"
            
            
    
    def calcular(self,valor): #funçao responsavel pelos calculos 
        global UltimoValor
        if valor == '=':
            UltimoValor = '='
            temp2=self.Resolve()
            if temp2== "ENTRADA INVALIDA" and self.edit1.get() != "":
                self.edit1.delete(0,END)
                self.edit1.insert(END,temp2)
            elif temp2== "ENTRADA INVALIDA" and self.edit1.get() == "":
                self.edit1.insert(END,'')
            else:
                self.edit1.delete(0,END)
                self.edit1.insert(END,temp2)
                

        elif valor == "CE" or valor =="C":
            self.edit1.delete(0,END)
        elif valor =="◄":
            texto = self.edit1.get()
            if texto == "ENTRADA INVALIDA":
                self.edit1.delete(0,END)
            else:
                texto[0:(len(texto))-1]
                self.edit1.delete(0,END)
                self.edit1.insert(END,texto[0:(len(texto))-1])
        elif valor == "+/-":
            resultado = self.Resolve()
            if resultado== "ENTRADA INVALIDA" and self.edit1.get() == "" or self.edit1.get() == "ENTRADA INVALIDA": 
                self.edit1.delete(0,END)
                self.edit1.insert(END,resultado)
            else:   
                temp=""
                for x in range(len(resultado)):
                    if resultado[x] == ",":
                        temp+="."
                    else:
                        temp+=str(resultado[x])
                temp=float(temp)
                           
                temp = -1*temp

                if (temp-(int(temp))) == 0:
                    text = str(int(temp))
                else:
                    text = "%5.2f" %(temp)

                temp2=""
                for x in range(len(text)):
                    if text[x] == ".":
                        temp2+=","
                    else:
                        temp2+=str(text[x])

                

                self.edit1.delete(0,END)
                self.edit1.insert(END,temp2) 

            
            
        else:
            texto = self.edit1.get()
            operadores = ['+','-','*','X','÷',',']
            if texto.isnumeric() and UltimoValor=="=" and valor.isnumeric():
                UltimoValor = valor
                self.edit1.delete(0,END)
                self.edit1.insert(END,valor)
            elif texto == 'ENTRADA INVALIDA':
                self.edit1.delete(0,END)
                self.edit1.insert(END,valor)
            elif texto == "" and (valor in operadores):
                self.edit1.insert(END,'0'+ str(valor))
                
            else:
                self.edit1.insert(END,valor)
                 
        
           
UltimoValor = 'V'       

       
root=tk.Tk()
MyApp=App(master=root)
MyApp.master.title("Calculadora")
MyApp.master.maxsize(1920,1024)
#MyApp.master.geometry("515x500")
MyApp.mainloop()

