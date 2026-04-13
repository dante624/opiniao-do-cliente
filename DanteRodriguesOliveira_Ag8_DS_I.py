# TudoWeb - Pesquisa de marketing: Opinião do Cliente

excelente = 0
ruim = 0

for i in range(50):
    print(f"Entrevistado {i + 1}")

    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))

    print("Opinião sobre o atendimento:")
    print("1 - EXCELENTE")
    print("2 - BOM")
    print("3 - RUIM")

    opiniao = int(input("Digite a opção (1/2/3): "))

    if opiniao == 1:
        excelente += 1
    elif opiniao == 3:
        ruim += 1
    elif opiniao != 2:
        print("Opção inválida")

print("----------------------")
print("RESULTADOS DA PESQUISA")
print(f"EXCELENTE: {excelente}")
print(f"RUIM: {ruim}")