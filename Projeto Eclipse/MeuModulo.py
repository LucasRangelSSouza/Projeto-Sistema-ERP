'''
Created on 17 de mar de 2018

@author: Jarvi
'''
from tkinter import *
from tkinter import ttk

import MySQLdb  #My Sql
import sqlite3  #sqlite 3
import fdb      #firebird

TecnologiaDeDados='Firebird'
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
    elif TecnologiaDeDados=="Firebird":
         try:
            DIRETORIO='CADASTRO.FDB'
            USER='sysdba'
            PASS='masterkey'

            conexao = fdb.connect(dsn=DIRETORIO, user=USER, password=PASS)
            status=True
            return status,conexao
            print('ok') 
         except:
            status=False
            return status,False
    else:
        status=False
        return status,False






def IniciaCadastroUsuarios():
    telaX = 935
    telaY = 380

    topo= Toplevel()
    topo.title("Cadastro de Usuarios")
    topo.maxsize(935,380)
    topo.minsize(935,380)
    topo.geometry("%dx%d"%(janelaX,janelaY))

    topo.withdraw()
    topo.update_idletasks() 
    x = ((topo.winfo_screenwidth() - telaX)/2)
    y = ((topo.winfo_screenheight() - telaY)/2)
    topo.geometry("+%d+%d" % (x, y))
    topo.deiconify()

     
    CadastroUsuarios(topo)

    topo.mainloop()

def IniciaCadastroDeProdutos():
    telaX = 1050
    telaY = 600

    raiz = Toplevel()
    raiz.geometry("1050x600")
    raiz.title("Cadastro de Produtos")
    raiz.maxsize(1050,600)
    raiz.minsize(1050,600)
    raiz.geometry("%dx%d"%(janelaX,janelaY))

    raiz.withdraw()
    raiz.update_idletasks() 
    x = ((raiz.winfo_screenwidth() - telaX)/2)
    y = ((raiz.winfo_screenheight() - telaY)/2)

    raiz.geometry("+%d+%d" % (x, y))
    raiz.deiconify()

    Cadastro_de_Produtos(raiz)
    raiz.mainloop()

def IniciaMenuPrincipal():
    

    janelaX = 1366
    janelaY = 768
    
    root= Tk()
    root.title("Rangel Tech Soluçoes")
    root.maxsize(1920,1024)
    root.geometry("%dx%d"%(janelaX,janelaY))


    root.withdraw()
    root.update_idletasks()

    x = ((root.winfo_screenwidth() - janelaX)/2)
    y = ((root.winfo_screenheight() - janelaY)/10)
    root.geometry("+%d+%d" % (x, y))
    root.deiconify()




    MenuPrincipal(root)
    root.mainloop()        

    
        
class MenuPrincipal:
    def __init__(self,master):
        self.master = master
        
        
        self.menu = Menu(master)
        
        
        self.MenuDeCadastro = Menu(self.menu) # Criando a opçao principal do menu cadastro
        self.MenuDeCadastro.add_command(label="Cadastro de Usuarios",command = self.CadastrarUsuarios) # opçoes do menu Cadastro
        self.MenuDeCadastro.add_command(label="Cadastro de Produtos",command = self.CadastrarProdutos)

        self.menu.add_cascade(label="Cadastro",menu=self.MenuDeCadastro) #criando a opçao em cascata o menu cadastro

        master.config(menu=self.menu)
        
        imagem = PhotoImage(file="fundo.png") 
        self.fundo = Label(image=imagem)
        self.fundo.imagem = imagem
        self.fundo.pack(pady=100)

        
    def CadastrarUsuarios(self):
        IniciaCadastroUsuarios()
    def CadastrarProdutos(self):
        IniciaCadastroDeProdutos()
        


class CadastroUsuarios:
    def __init__(self,raiz):
        self.raiz = raiz
        

       
        
        img = PhotoImage(file="Imagens/user.png")
        Logo = Label(self.raiz, image= img)
        Logo.image = img
        Logo.place(x=10,y=50)
            
               
        xlabels = 300
        ylabels = 30

        xEdits = 480
        yEdits = 30
        
        

        Label(self.raiz,text="ID:",font=("Roboto","15")).place(x=xlabels,y=ylabels + 0) #

        status,conexao= BancoDeDados()
        cursor = conexao.cursor()
        sql="SELECT MAX(id) from usuarios" 
        cursor.execute(sql)
        resultSet= cursor.fetchall()
        conexao.close()
        Id= resultSet[0][0]
        
               

        self.ID = Label(self.raiz,font=("Times New Roman","15"),width=5,text=Id,relief=GROOVE)
        self.ID.place(x=xEdits,y=yEdits + 0)
        
        Label(self.raiz,text="Usuario:",font=("Roboto","15")).place(x=xlabels,y=ylabels + 40)#

        self.usuario = Entry(self.raiz,font=("Times New Roman","15"),width=26)
        self.usuario.place(x=xEdits,y=yEdits + 40)
        self.usuario.focus_force()


        Label(self.raiz,text="Senha:",font=("Roboto","15")).place(x=xlabels,y=ylabels + 80) #

        self.senha = Entry(self.raiz,font=("Times New Roman","15"),width=26,show="•",fg="darkgrey")
        self.senha.place(x=xEdits,y=yEdits + 80)


        Label(self.raiz,text="Confirme a Senha:",font=("Roboto","15")).place(x=xlabels,y=ylabels + 120) #

        self.Confsenha = Entry(self.raiz,font=("Times New Roman","15"),width=26,show="•",fg="darkgrey")
        self.Confsenha.place(x=xEdits,y=yEdits + 120)
       
        
        Label(self.raiz,text="Funcionario",font=("Roboto","15")).place(x=xlabels,y=ylabels + 160) #
        
        funcionariosValues=('Selecione o Funcionario', 'Teste1', 'Teste2')
        self.Funcionario = StringVar()
        self.Funcionario = ttk.Combobox(self.raiz,textvariable=self.Funcionario,font=("Times New Roman","15"),width=24,state='readonly')
        self.Funcionario['values'] = funcionariosValues
        self.Funcionario.current(0)
        self.Funcionario.place(x=xEdits,y=yEdits + 160)

        Label(self.raiz,text="Perfil de usuario:",font=("Roboto","15")).place(x=xlabels,y=ylabels + 200) #
        
        PerfilValues=('Selecione o Perfil', 'Administrador', 'Usuario', 'Caixa', 'Gerente')
        self.Perfil = StringVar()
        self.Perfil = ttk.Combobox(self.raiz,textvariable=self.Perfil,font=("Times New Roman","15"),width=24,state='readonly')
        self.Perfil['values'] = PerfilValues
        self.Perfil.current(0)
        self.Perfil.place(x=xEdits,y=yEdits + 200)

        self.Informacoes = Label(self.raiz,text="",font=("Roboto","15")) 
        self.Informacoes.place(x=380,y=270) #

        self.Salvar = Button(self.raiz,text="Salvar",font=("Stark","16"),width=15,command = self.salvar).place(x=350,y=320)
        self.Cancelar = Button(self.raiz,text="Cancelar",font=("Stark","16"),width=15,command = self.cancelar).place(x=550,y=320)

        self.Pesquisar = Button(self.raiz,text="Pesquisar",font=("Stark","16"),width=15,command = self.pesquisar).place(x=780,y=25)

        
        
    def salvar(self):
        

        status,conexao= BancoDeDados()
        cursor = conexao.cursor()

        sql1="SELECT MAX(id) from usuarios" 
        cursor.execute(sql1)
        resultSet1= cursor.fetchall()
        

        Id= (resultSet1[0][0])+1
        Usuario = self.usuario.get()
        Senha= self.senha.get()
        ConfimSenha= self.Confsenha.get()
        Funcionario= self.Funcionario.current()
        Perfil = self.Perfil.current()
        
        sql="SELECT ID from usuarios where USUARIO like '%s'" %Usuario 
        cursor.execute(sql)
        resultSet= cursor.fetchall()
        try:
            JaCadastrado = (resultSet[0][0]) > 0
        except IndexError:
            JaCadastrado = False

        if len(Usuario) < 1:
            self.Informacoes["text"]= "Necessario preencher o Usuario"
            self.usuario.focus_force()
            conexao.close()
        elif len(Senha) < 1:
            self.Informacoes["text"]= "Necessario preencher a Senha"
            self.senha.focus_force()
            conexao.close()
        elif len(ConfimSenha) < 1:
            self.Informacoes["text"]= "Necessario confirmar a Senha"
            self.Confsenha.focus_force()
            conexao.close()
        elif Senha != ConfimSenha:
            self.Informacoes["text"]= "As senhas nao conferem"
            self.senha.delete(0,END)
            self.Confsenha.delete(0,END)
            self.senha.focus_force()
            conexao.close()
        elif Funcionario < 1:
            self.Informacoes["text"]= "Selecione um Funcionario"
            self.Funcionario.focus_force()
            conexao.close()
        elif Perfil < 1:
            self.Informacoes["text"]= "Selecione um perfil de usuario"
            self.Perfil.focus_force()
            conexao.close()
        
        elif JaCadastrado:
            self.Informacoes["text"]= "Nome de Usuario já Cadastrado"
            self.usuario.delete(0,END)
            self.usuario.focus_force()
            conexao.close()
        else:
            status,conexao= BancoDeDados()
            cursor = conexao.cursor()
            sql="INSERT INTO USUARIOS (ID, USUARIO, SENHA, PERFIL, FUNCIONARIO) VALUES ( %d, '%s', '%s', %d, %d);" %(Id,Usuario,Senha,Funcionario,Perfil)
            cursor.execute(sql)
            conexao.commit()
            conexao.close()
            self.Informacoes["text"]= "Usuario Cadastrdo com sucesso"
            self.usuario.delete(0,END)
            self.senha.delete(0,END)
            self.Confsenha.delete(0,END)
            self.Funcionario.current(0)
            self.Perfil.current(0)
            self.usuario.focus_force()
            self.ID["text"] = Id+1

    def cancelar(self):
        self.Informacoes["text"]= ""
        self.usuario.delete(0,END)
        self.senha.delete(0,END)
        self.Confsenha.delete(0,END)
        self.Funcionario.current(0)
        self.Perfil.current(0)
        self.usuario.focus_force()

    def pesquisar(self):
        self.Informacoes["text"]= "coming soon"

class Cadastro_de_Produtos():
    def __init__(self,topolevel):
        self.frame = topolevel
        
        img = PhotoImage(file="Imagens/produtos.png")
        Logo = Label(self.frame, image= img)
        Logo.image = img
        Logo.place(x=10,y=50)
        
        self.id = 0
        self.Ja_Existe = False
        fonte=("Times New Roman","15")
        fontePequena=("Times New Roman","12")

        

        validaCodigo= (self.frame.register(self.ValidaCodigo),'%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')
        Label(self.frame,text='Codigo: ',font = fonte).place(x=300, y= 30)
        self.codigo = Entry(self.frame,font=fonte,width=18,validate = 'key', validatecommand = validaCodigo)
        self.codigo.bind('<FocusOut>',self.FocusOut_Codigo)
        self.codigo.place(x=370 , y= 30 )
        

          
        Label(self.frame,text='Referencia: ',font = fonte).place(x=590, y= 30)
        self.referencia = Entry(self.frame,font=fonte,width=18)
        self.referencia.bind('<Any-KeyPress>',self.ChecaReferencia)
        self.referencia.place(x=690 , y= 30 )

        Label(self.frame,text='Descriçao: ',font = fonte).place(x=300, y= 70)
        self.descricao = Entry(self.frame,font=fonte,width=47)
        self.descricao.place(x=400 , y= 70 )

        
        self.ComboGrupo = []
        self.ComboSubgrupo =[] 
        self.ComboMarca =[]
        self.ComboDepartamento =[]
        self.ComboTributacao =[]
        self.ComboUnidade = []
        self.PreencheComboBox()

        print(self.ComboGrupo, self.ComboSubgrupo,self.ComboMarca,self.ComboDepartamento,self.ComboTributacao,self.ComboUnidade)
        Label(self.frame,text='Grupo: ',font = fonte).place(x=300, y= 110)
        self.grupo = StringVar()
        self.grupo = ttk.Combobox(self.frame,font=fontePequena,width=20,state='readonly',textvariable=self.grupo)
        self.grupo['values'] = self.ComboGrupo
        self.grupo.place(x=370 , y= 110)

        Label(self.frame,text='Subgrupo: ',font = fonte).place(x=595, y= 110)
        self.subgrupo = StringVar()
        self.subgrupo = ttk.Combobox(self.frame,font=fontePequena,width=20,state='readonly',textvariable=self.subgrupo)
        self.subgrupo['values'] = self.ComboSubgrupo
        self.subgrupo.place(x=690 , y= 110)

        Label(self.frame,text='Marca: ',font = fonte).place(x=300, y= 150)
        self.marca = StringVar()
        self.marca = ttk.Combobox(self.frame,font=fontePequena,width=20,state='readonly',textvariable=self.marca)
        self.marca['values'] = self.ComboMarca
        self.marca.place(x=370 , y= 150)

        Label(self.frame,text='Departamento: ',font = fonte).place(x=560, y= 150)
        self.departamento = StringVar()
        self.departamento = ttk.Combobox(self.frame,font=fontePequena,width=20,state='readonly',textvariable=self.departamento)
        self.departamento['values'] = self.ComboDepartamento
        self.departamento.place(x=690 , y= 150)

        Label(self.frame,text='Tributaçao: ',font = fonte).place(x=300, y= 190)
        self.tributacao = StringVar()
        self.tributacao = ttk.Combobox(self.frame,font=fontePequena,width=20,state='readonly',textvariable=self.tributacao)
        self.tributacao['values'] = self.ComboTributacao
        self.tributacao.place(x=400 , y= 190 )

        Label(self.frame,text='Unidade: ',font = fonte).place(x=300, y= 230)
        self.unidade = StringVar()
        self.unidade = ttk.Combobox(self.frame,font=fontePequena,width=5,state='readonly',textvariable=self.unidade)
        self.unidade['values'] = self.ComboUnidade
        self.unidade.place(x=380 , y= 230)

        validaNumerico= (self.frame.register(self.ValidaNumerico),'%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')
        
        Label(self.frame,text='NCM: ',font = fonte).place(x=625, y= 190)
        self.ncm = Entry(self.frame,font=fonte,width=18,validate = 'key', validatecommand = validaNumerico)
        self.ncm.place(x=690 , y= 190 )

        Label(self.frame,text='CEST: ',font = fonte).place(x=620, y= 230)
        self.cest = Entry(self.frame,font=fonte,width=18,validate = 'key', validatecommand = validaNumerico)
        self.cest.place(x=690 , y= 230 )

        validaValores = (self.frame.register(self.ValidaValores),'%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')
         
        Label(self.frame,text='Preço Custo: ',font = fonte).place(x=10, y= 300)
        self.custo = Entry(self.frame,font=fonte,width=10,validate = 'key', validatecommand = validaValores,justify='right')
        self.custo.place(x= 120 , y= 300 )
        
        Label(self.frame,text='Preço Varejo: ',font = fonte).place(x=240, y= 300)
        self.varejo = Entry(self.frame,font=fonte,width=10,validate = 'key', validatecommand = validaValores,justify='right')
        self.varejo.place(x=360 , y= 300 )

        Label(self.frame,text='Preço Atacado: ',font = fonte).place(x=480, y= 300)
        self.atacado = Entry(self.frame,font=fonte,width=10,validate = 'key', validatecommand = validaValores,justify='right')
        self.atacado.place(x=610 , y= 300 )

        Label(self.frame,text='% Lucro Varejo: ',font = fonte).place(x=240, y= 340)
        self.lucro_varejo = Entry(self.frame,font=fonte,width=8,validate = 'key', validatecommand = validaValores,justify='right')
        self.lucro_varejo.place(x=380 , y= 340 )

        Label(self.frame,text='% Lucro Atacado: ',font = fonte).place(x=480, y= 340)
        self.lucro_atacado = Entry(self.frame,font=fonte,width=8,validate = 'key', validatecommand = validaValores,justify='right')
        self.lucro_atacado.place(x=630 , y= 340 )

        Label(self.frame,text='Estoque: ',font = fonte).place(x=725, y= 300)
        self.estoque = Entry(self.frame,font=fonte,width=7,validate = 'key', validatecommand = validaValores,justify='right')
        self.estoque.place(x=800 , y= 300 )
        

        self.Salvar = Button(self.frame,text= 'F4 - Salvar',font = fonte, width=12,command = self.Botao_Salvar)
        self.Salvar.place(x=900 , y= 30 )

        self.Salvar = Button(self.frame,text= 'F5 - Deletar',font = fonte, width=12)
        self.Salvar.place(x=900 , y= 70 )

        self.Informacoes = Label(self.frame, text='',font = fonte)
        self.Informacoes.place(x=550, y= 400)

    def PreencheComboBox(self):
        status,conexao = BancoDeDados()
        if status:
            cursor = conexao.cursor()
            
            cursor.execute('SELECT GRUPO FROM GRUPO ORDER BY ID')
            for item in cursor.fetchall():
                self.ComboGrupo.append(item[0]) 
           

            cursor.execute('SELECT SUBGRUPO FROM SUBGRUPO ORDER BY ID')
            for item in cursor.fetchall():
                self.ComboSubgrupo.append(item[0])

            cursor.execute('SELECT MARCA FROM MARCA ORDER BY ID')
            for item in cursor.fetchall():
                self.ComboMarca.append(item[0])

            cursor.execute('SELECT DEPARTAMENTO FROM DEPARTAMENTO ORDER BY ID')
            for item in cursor.fetchall():
                self.ComboDepartamento.append(item[0])

            cursor.execute('SELECT TRIBUTACAO FROM TRIBUTACAO ORDER BY ID')
            for item in cursor.fetchall():
                self.ComboTributacao.append(item[0])

            cursor.execute('SELECT UNIDADE FROM UNIDADE ORDER BY ID')
            for item in cursor.fetchall():
                self.ComboUnidade.append(item[0])

            conexao.close()
        

        
    def ValidaValores(self, porque, index, value_if_allowed, prior_value, text, validation_type, trigger_type, widget_name):
        if text.replace(',','0',1).isnumeric():
            #print('Porque: ',porque, '# indice: ' ,index, '# Valor se true :', value_if_allowed,'# Valor anterior :', prior_value,'# Texto: ' ,text, '# Tipo de validacao: ', validation_type,'# tipo de Gatilho: ', trigger_type,'# Nome do Widget: ', widget_name)
            return True
        else:
            return False

    def ValidaNumerico(self, porque, index, value_if_allowed, prior_value, text, validation_type, trigger_type, widget_name):
           
        if text.isnumeric() and int(index) < 8:
            return True
        else:
            return False

    def ValidaCodigo(self, porque, index, value_if_allowed, prior_value, text, validation_type, trigger_type, widget_name):

        if int(index) < 14:
            value_if_allowed = text.upper()
            text = text.upper()
            prior_value = prior_value.upper()
            print('Porque: ',porque, '# indice: ' ,index, '# Valor se true :', value_if_allowed,'# Valor anterior :', prior_value,'# Texto: ' ,text, '# Tipo de validacao: ', validation_type,'# tipo de Gatilho: ', trigger_type,'# Nome do Widget: ', widget_name)
            return True
        else:
            return False
        
        
    def Botao_Salvar(self):
        if self.Ja_Existe:
            print("Tinha um update sem nd aqui")
        elif self.Ja_Existe==False:
            status,conexao = BancoDeDados()
            
            conexao.cursor()
            cursor = conexao.cursor()

            Codigo = self.codigo.get()
            Referencia = self.referencia.get()
            Descricao = self.descricao.get()
            Grupo = self.grupo.current() +1
            Subgrupo = self.subgrupo.current() +1
            Marca = self.marca.current() +1
            Departamento= self.departamento.current() +1
            Tributacao = self.tributacao.current() +1
            Unidade = self.unidade.current() +1
            Ncm = self.ncm.get()
            Cest = self.cest.get()
            Custo = self.custo.get()
            Varejo = self.varejo.get()
            Atacado = self.atacado.get()
            Lucro_Varejo =self.lucro_varejo.get()
            Lucro_Atacado =self.lucro_atacado.get()
            Estoque = self.estoque.get()
            

            print(Grupo)
            
            
            sql="INSERT INTO PRODUTOS (ID, CODIGO, REFERENCIA, DESCRICAO, GRUPO, SUBGRUPO, MARCA, DEPARTAMENTO, TRIBUTACAO, UNIDADE, NCM, CEST, PRECO_CUSTO, PRECO_VAREJO, PRECO_ATACADO, LUCRO_VAREJO, LUCRO_ATACADO, ESTOQUE) VALUES (null, '%s', '%s', '%s', %d, %d, %d, %d, %d, %d, '%s', '%s', %d, %d, %d, %d, %d, %d)"\
            %(Codigo,Referencia,Descricao,Grupo,Subgrupo,Marca,Departamento,Tributacao,Unidade,Ncm,Cest,float((Custo.replace(',','.'))),float((Varejo.replace(',','.'))),float((Atacado,Lucro_Varejo.replace(',','.'))),float((Lucro_Atacado.replace(',','.'))),float((Estoque.replace(',','.'))))
 
            cursor.execute(sql)
            conexao.commit()
            conexao.close()
            print('ok')
            
        
        
        
        
    def FocusOut_Codigo(self,evento):
        codigo = self.codigo.get()
        status,conexao = BancoDeDados()

        if not status:
            self.informacoes['text'] = 'Desculpe, nao consegui conectar ao banco de dados no momento'
        elif status:
            
            if len(codigo) < 1:
                conexao.cursor()
                cursor = conexao.cursor()
                sql = "SELECT GEN_ID(PROXIMO_CODIGO_PRODUTO, 0) FROM RDB$DATABASE"
                cursor.execute(sql)
                resultSet= cursor.fetchall()
                conexao.close()
                
                self.codigo.insert(0,resultSet[0])
                self.limpaCampos()
                self.Ja_Existe = False
                self.referencia.focus_force()
            elif len(codigo) > 1:
                
                conexao.cursor()
                cursor = conexao.cursor()
                sql="SELECT ID FROM PRODUTOS WHERE CODIGO LIKE '%s' " %codigo 
                cursor.execute(sql)
                resultSet= cursor.fetchall()
                conexao.close()
                                
                try:
                    self.id = resultSet[0][0]
                    self.Ja_Existe = True
                    self.PreencheDados()
                    
                except IndexError:
                    self.Ja_Existe = False
                    self.limpaCampos()
                    self.referencia.focus_force()
                
                    
        else:
            self.informacoes['text'] = 'Desculpe, ocorreu um erro inesperado'

    def limpaCampos(self):
        self.referencia.delete(0,END)
        self.descricao.delete(0,END)
        self.grupo.set('')
        self.subgrupo.set('')
        self.marca.set('')
        self.departamento.set('')
        self.tributacao.set('')
        self.unidade.set('')
        self.ncm.delete(0,END)
        self.cest.delete(0,END)
        self.custo.delete(0,END)                 
        self.varejo.delete(0,END)
        self.atacado.delete(0,END)
        self.lucro_varejo.delete(0,END)
        self.lucro_atacado.delete(0,END)
        self.estoque.delete(0,END)

        
    def PreencheDados(self):
        
        status,conexao = BancoDeDados()
        conexao.cursor()
        cursor = conexao.cursor()
        sql="SELECT * FROM PRODUTOS WHERE ID = '%s' " %self.id  
        cursor.execute(sql)
        resultSet= cursor.fetchall()
        conexao.close()
        self.referencia.delete(0,END)
        self.referencia.insert(0,resultSet[0][2])
        self.descricao.delete(0,END)
        self.descricao.insert(0,resultSet[0][3])
        
        self.grupo.current(resultSet[0][4] -1)
        self.subgrupo.current(resultSet[0][5] -1)
        self.marca.current(resultSet[0][6] -1)
        self.departamento.current(resultSet[0][7] -1)
        self.tributacao.current(resultSet[0][8] -1)
        self.unidade.current(resultSet[0][4] -1)
        
        self.ncm.delete(0,END)
        self.ncm.insert(0,resultSet[0][10])
        self.cest.delete(0,END)
        self.cest.insert(0,resultSet[0][11])

        self.custo.delete(0,END)                 
        custo = '%5.2f' %resultSet[0][12]
        self.custo.insert(0,str(custo).replace('.',','))

        self.varejo.delete(0,END)
        varejo ='%5.2f' %resultSet[0][13]
        self.varejo.insert(0,str(varejo).replace('.',','))

        self.atacado.delete(0,END)
        atacado ='%5.2f' %resultSet[0][14]
        self.atacado.insert(0,str(atacado).replace('.',','))

        self.lucro_varejo.delete(0,END)
        lucro_varejo = '%5.2f' %resultSet[0][15]
        self.lucro_varejo.insert(0,str(lucro_varejo).replace('.',','))

        self.lucro_atacado.delete(0,END)
        lucro_atacado = '%5.2f' %resultSet[0][16]
        self.lucro_atacado.insert(0,str(lucro_atacado).replace('.',','))

        self.estoque.delete(0,END)
        estoque = '%5.2f' %resultSet[0][17]
        self.estoque.insert(0,str(estoque).replace('.',','))                 

        self.referencia.focus_force()
    
    
    def ChecaReferencia(self,evento):
        if len(self.referencia.get()) > 16:
            referencia = self.referencia.get()
            self.referencia.delete(0,END)
            self.referencia.insert(0,referencia[0:-1])

        
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
IniciaMenuPrincipal()
 











