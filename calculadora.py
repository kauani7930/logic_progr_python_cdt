##MVC
#model
###entrada dos números e funções.

#view
###vai exibir os resultados na tela.

#controller
###Organização dos operados e interação.



def mostra_menu():
print("/n---calculador---")
print("1. adição")
print("2. subtração")
print("5. sair")
print("-----------------")

def obter_número():
    white true:
    try:
        num1 =float(input("digite o primeiro número:"))
        num2 =float(input("digite o segundo número:"))
        return num1, num2
        execept  ValueError
        print("entradada inválida. por favor,"/"digite número válidade.")
