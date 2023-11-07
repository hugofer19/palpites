import random
x = random.randint(1,10)
print(x)
palpite = input("Qual o teu palpite: ")

if int(palpite) == x:
    print("Acertaste")
    quit()
while int(palpite != x):
    if int(palpite) > x:
        print("O número é menor, tenta novamente")
        palpite = input("Qual o teu palpite: ")
        if int(palpite) == x:
            print("Acertaste")
            break
    elif int(palpite) < x:
        print("O número é maior, tenta novamente")
        palpite = input("Qual o teu palpite: ")
        if int(palpite) == x:
            print("Acertaste")
            break
else: print("Acertaste no número sorteado!")


