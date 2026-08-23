print("--- Calculadora ---")

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

print("Escolha a operação: +, -, *, /")
operacao = input("Digite o símbolo da operação: ")

if operacao == "+":
    resultado = num1 + num2
    print("O resultado é:", resultado)

elif operacao == "-":
    resultado = num1 - num2
    print("O resultado é:", resultado)

elif operacao == "*":
    resultado = num1 * num2
    print("O resultado é:", resultado)

elif operacao == "/":
   # Tratamento especial: não podemos dividir por zero na matemática!
   if num2 == 0:
    print("Erro: Não é possível dividir por zero!")
   else:
    resultado = num1 / num2
    print("O resultado é:", resultado)

else:
  # Se o usuário digitar uma letra ou símbolo inválido, avisamos o erro.
  print("Operação inválida! Tente novamente.")
