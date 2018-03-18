from tkinter import *

import MySQLdb  #My Sql
import sqlite3  #sqlite 3
import fdb      #firebird


#TecnologiaDeDados ="MySql"
#TecnologiaDeDados = "SqLite"
TecnologiaDeDados="Firebird"
ProxForm = False

def BancoDeDados():
    global TecnologiaDeDados
    if TecnologiaDeDados=="MySql":
        DATABASE = 'cadastro'
        USER = 'root'
        PSSWD = ''
        HOST = '127.0.0.1'
        try:
            
            conexao = MySQLdb.connect(db=DATABASE,user=USER,passwd=PSSWD,host=HOST)
            status=True
            return status,conexao
        except:
            status=False
            return status,False

    elif TecnologiaDeDados=="SqLite":
        try:
            conexao = sqlite3.connect("Cadastro.db")
            status=True
            return status,conexao
            
            
        except:
            status=False
            return status,False

    elif TecnologiaDeDados=="Oracle":
        pass

    elif TecnologiaDeDados=="Firebird":
         try:
            DIRETORIO='CADASTRO.FDB'
            USER='sysdba'
            PASS='masterkey'

            conexao = fdb.connect(dsn=DIRETORIO, user=USER, password=PASS)
            status=True
            return status,conexao
            
            
         except:
            status=False
            return status,False


class Login:
    def __init__(self,master):
        self.master = master
        self.master.title("Login")
        
        imagem = PhotoImage(file="logo.png")
        Logo = Label(root, image=imagem)
        Logo.imagem = imagem
        Logo.grid(row=1,column=1,columnspan=3,pady=2,padx=2,stick= S)

        
        Label(self.master,text="Usuario:",font=("Roboto","20")).grid(row=2,column=1,pady=2,padx=4)
        Label(self.master,text="Senha:",font=("Roboto","20")).grid(row=3,column=1,pady=2,padx=4)
        self.informacoes = Label(self.master,text="...",font=("Times New Roman","16"))
        self.informacoes.grid(row=4,column=2,pady=2,padx=4)

        
        self.usuario = Entry(self.master,font=("Times New Roman","19"),width=25)
        self.usuario.grid(row=2,column=2,ipady=4,columnspan = 2,pady=4)
        self.usuario.focus_force()

        self.senha = Entry(self.master,font=("Times New Roman","19"),width=25,show="•",fg="darkgrey")
        self.senha.grid(row=3,column=2,ipady=4,columnspan = 2,pady=4)
        
        self.login = Button(self.master,text="Login",font=("Stark","16"),width=15,command = self.Login).grid(row=5,column=2)
        self.conexaoBD = Label(self.master,text="•",font=("Oswald","16","bold"),fg="yellow")
        self.conexaoBD.grid(row=1,column=3,pady=2,padx=4,stick= E)
        self.BotaoConexao()
        

    def BotaoConexao(self):
        status,conexao= BancoDeDados()
        if status:
            self.conexaoBD["fg"]="green" #conectou no bd
        elif not status:
            self.conexaoBD["fg"]="red" #nao conectou no bd
        
    def Login(self):
        usuario = self.usuario.get()
        senha = self.senha.get()
        status,conexao= BancoDeDados()
        if not status:
            self.informacoes["text"]= "Nao foi possivel conectar com o banco de dados"
            self.BotaoConexao()
            
        else:
            self.BotaoConexao()
            cursor = conexao.cursor()

            sql="Select usuario , senha from usuarios where usuario like '%s'" %usuario 
            cursor.execute(sql)
            resultSet= cursor.fetchall()
            conexao.close()
            
            try:
                usuarioResultSet=resultSet[0][0]
                senhaResultSet=resultSet[0][1]
                
                if usuario == usuarioResultSet and senha == senhaResultSet:
                    self.informacoes["text"]= "Login bem sucedido"
                    global ProxForm
                    ProxForm = True
                    self.master.destroy()
                    

                elif usuario == usuarioResultSet and senha != senhaResultSet:
                    self.informacoes["text"]= "Senha Incorreta"
                    self.senha.delete(0,END)
                    self.senha.focus_force()
                else:
                    self.informacoes["text"]= "Usuario nao encontrado"
                    self.usuario.delete(0,END)
                    self.senha.delete(0,END)
                    self.usuario.focus_force()

            except Exception as erro: 
                
                self.informacoes["text"]= "Usuario nao encontrado"
                self.usuario.delete(0,END)
                self.senha.delete(0,END)
                self.usuario.focus_force()
                    
        
 

        
        

janelaX = 430
janelaY = 300

root= Tk()
root.title("Login")
root.maxsize(430,300)
root.geometry("%dx%d"%(janelaX,janelaY))

root.withdraw()
root.update_idletasks() 
x = ((root.winfo_screenwidth() - janelaX)/2)
y = ((root.winfo_screenheight() - janelaY)/2)
root.geometry("+%d+%d" % (x, y))
root.deiconify()
Login(root)
#root.iconbitmap('py.ico')
root.mainloop()

if ProxForm:
    import MenuPrincipal
    


