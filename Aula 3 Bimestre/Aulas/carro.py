class Carro:
    marca = ""
    modelo = ""
    ano = 0
    cor = ""

    def desligar(self):
        print("Swoosh")

    def acelerar(self):
        print("Yoooowoowwwnn")

    def freiar(self):
        print("EEEEEERRRRRR...")


    def ligar(self):
        print("PHAM PHAM BRRRRRRRRRRRRRRRRRRRR")

    def buzinar(self):
        print("Bi-bi")

c1 = Carro()
c1.marca = "Nissan"
c1.modelo = "GT3"
c1.ano = 2015
c1.cor = "azul"

print(f"Carro: {c1.marca} - Modelo: {c1.modelo}- Ano: {c1.ano} - Cor: {c1.cor}")


c1.ligar()
c1.buzinar()
c1.acelerar()
c1.freiar()
c1.desligar()