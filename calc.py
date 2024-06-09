while True:
    print("Escolha a operação:")
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Sair")
    
    escolha = input("Digite o número da operação desejada: ")

    if escolha == '5':
        print("Calculadora encerrada.")
        break

    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    if escolha == '1':
        resultado = num1 + num2
    elif escolha == '2':
        resultado = num1 - num2
    elif escolha == '3':
        resultado = num1 * num2
    elif escolha == '4':
        if num2 != 0:
            resultado = num1 / num2
        else:
            print("Não é possivel divisão por 0!")
            continue
    else:
        print("Opção inválida. Por favor, escolha uma operação válida.")
        continue

    print("Resultado:", resultado)