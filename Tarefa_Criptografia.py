class Criptografia ():

    def __init__(self, info):
        self.info = info

    def geraHash(self):
        resultado = 0
        for letra in self.info:
            resultado = resultado + ord(letra)
        return resultado

    def geraSegredo (self, deslocamento):
        segredo = ''
        for letra in self.info:
            codigo = ord(letra)
            novo_codigo = codigo * deslocamento
            nova_letra = chr(novo_codigo)
            segredo = segredo + nova_letra
        return segredo


#Inicio do programa


crip = Criptografia ("aula")


print(crip.info)
print(crip.geraHash())
print(crip.geraSegredo(2))

input()