def Par_o_impar():
    numero=input("Dime un numero: ")
    for cont in range(1,numero+1):
        if(cont%2==0):
            print(str(cont)+ " PAR")
        else:
            print(str(cont)+ " IMPAR")

Par_o_impar()
