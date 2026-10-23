# idade = int(input("Digite a sua idade: "))

# if idade >= 18:
#     print("Maior de idade")
# else:
#     print("Menor de idade")


while True:
    try:
        valor = float(input("digite um núemro"))
        if valor >= 0:
            print(f"{valor} é positivo")
            break
        else:
            print(f"{valor} é negativo")
            break
    except ValueError:
        print("difgite apenas um valor")
    break