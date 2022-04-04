from tkinter import *

class Application:
    def __init__(self, master=None):
        #Containers - Inicio
        self.fontePadrao = ("Arial", "10")
        self.primeiroContainer = Frame(master)
        self.primeiroContainer["pady"] = 10
        self.primeiroContainer.pack()

        self.segundoContainer = Frame(master)
        self.segundoContainer["padx"] = 20
        self.segundoContainer.pack()

        self.terceiroContainer = Frame(master)
        self.terceiroContainer["padx"] = 20
        self.terceiroContainer.pack()

        self.quartoContainer = Frame(master)
        self.quartoContainer["padx"] = 20
        self.quartoContainer.pack()

        self.quintoContainer = Frame(master)
        self.quintoContainer["pady"] = 20
        self.quintoContainer.pack()
        
        self.sextoContainer = Frame(master)
        self.sextoContainer["pady"] = 10
        self.sextoContainer.pack()
        #Containers - Final

        #Definindo o conteúdo dos containers
        self.titulo = Label(self.primeiroContainer, text="Calculadora IMC")
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo.pack()
        
        self.alturaLabel = Label(self.segundoContainer,text="Altura", font=self.fontePadrao)
        self.alturaLabel.pack(side=LEFT)

        self.altura = Entry(self.segundoContainer)
        self.altura["width"] = 8
        self.altura["font"] = self.fontePadrao
        self.altura.pack(side=LEFT)

        self.pesoLabel = Label(self.terceiroContainer, text="Peso", font=self.fontePadrao)
        self.pesoLabel.pack(side=LEFT)

        self.peso = Entry(self.terceiroContainer)
        self.peso["width"] = 8
        self.peso["font"] = self.fontePadrao
        self.peso.pack(side=LEFT)

        self.generoLabel = Label(self.quartoContainer, text="Gênero", font=self.fontePadrao)
        self.generoLabel.pack(side=LEFT)

        self.genero = Entry(self.quartoContainer)
        self.genero["width"] = 8
        self.genero["font"] = self.fontePadrao
        self.genero.pack(side=LEFT)

        self.calcular = Button(self.quintoContainer)
        self.calcular["text"] = "Calcular"
        self.calcular["font"] = ("Calibri", "8")
        self.calcular["width"] = 12
        self.calcular["command"] = self.calcularIMC
        self.calcular.pack()

        self.mensagem1 = Label(self.sextoContainer, text="", font=self.fontePadrao)
        self.mensagem1.pack()

        self.mensagem2 = Label(self.sextoContainer, text="", font=self.fontePadrao)
        self.mensagem2.pack()

    def calcularIMC(self):
        #Pegando valores dos inputs dos containeres
        altura = float(self.altura.get())
        peso = int(self.peso.get())
        genero = self.genero.get().lower()

        #Calculo imc
        divisor = altura*altura
        imc = peso/divisor     

        #Tabela - Homem
        if imc < 16 and genero[0] == 'h':
            self.mensagem1["text"] = "Magreza grave"
            self.mensagem2["text"] = imc
        elif imc > 16 and imc < 18.5 and genero[0] == 'h':
            self.mensagem1["text"] = "Magreza leve"
            self.mensagem2["text"] = imc
        elif imc > 18.5 and imc < 25 and genero[0] == 'h':
            self.mensagem1["text"] = "Saúdavel"
            self.mensagem2["text"] = imc
        elif imc > 25 and genero[0] == 'h':
            self.mensagem1["text"] = "Obesidade"
            self.mensagem2["text"] = imc

        #Tabela - Mulher
        elif imc < 17 and genero[0] == 'm':
            self.mensagem1["text"] = "Magreza grave"
            self.mensagem2["text"] = imc
        elif imc > 17 and imc < 18.5 and genero[0] == 'm':
            self.mensagem1["text"] = "Magreza leve"
            self.mensagem2["text"] = imc
        elif imc > 18.5 and imc < 25 and genero[0] == 'm':
            self.mensagem1["text"] = "Saúdavel"
            self.mensagem2["text"] = imc
        elif imc > 25 and genero[0] == 'm':
            self.mensagem1["text"] = "Obesidade"
            self.mensagem2["text"] = imc

#Inicializando container principal(TOP LEVEL)
root = Tk()
root.title("IMC")
Application(root)
root.mainloop()