from tkinter import *
from tkinter import ttk
import MySQLdb  #My Sql
import sqlite3  #sqlite 3
import fdb      #firebird

#TecnologiaDeDados ="MySql"
#TecnologiaDeDados = "SqLite"
TecnologiaDeDados="Firebird"


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
            print('bizarro')
            status=False
            return status,False


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
            update
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
            
            
            sql="INSERT INTO PRODUTOS (ID, CODIGO, REFERENCIA, DESCRICAO, GRUPO, SUBGRUPO, MARCA, DEPARTAMENTO, TRIBUTACAO, UNIDADE, NCM, CEST, PRECO_CUSTO, PRECO_VAREJO, PRECO_ATACADO, LUCRO_VAREJO, LUCRO_ATACADO, ESTOQUE) VALUES (1, '7894561237894', '123456', 'TESLA ROADSTER ELETRICO 1000 KM/CARGA', 2, 2, 2, 2, 2, '1', '123456789', '321654987', 150000.75, 250000.25, 200000.75, 10, 15, 25)"\
            %(Codigo,Referencia,Descricao,Grupo,Subgrupo,Marca,Departamento,Tributacao,Unidade,Ncm,Cest,Custo,Varejo,Atacado,Lucro_Varejo,Lucro_Atacado,Estoque)
 
            #cursor.execute(sql)
            
            #conexao.close()
            
        
        
        
        
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

    

def ChamaCadastroDeProdutos():
    raiz = Tk()
    raiz.geometry("1050x600")
    Cadastro_de_Produtos(raiz)
    raiz.mainloop()
    

ChamaCadastroDeProdutos()

















        
