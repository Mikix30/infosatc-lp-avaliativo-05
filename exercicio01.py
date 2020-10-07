for i in range(0,4):  
   
    name = input("Qual o nome desejado? Ele deve possuir no minimo três letras. ")
   

    while(len(name)<3):
   
        print("O nome qual você colocou possui menos de três letras.")
   
        name = input("Qual o nome desejado? Ele deve possuir no minimo três letras.")
   
    middlename = input("Qual o sobrenome? Ele deve possuir no minimo três letras. ")
   

    while(len(middlename)<3):
   
        print("O sobrenome escolhido tem menos de três letras, por favor, tente novamente.")
   
        middlename = input("Qual o sobrenome? Ele deve possuir no minimo três letras.")
    

    password = input("password:")
    
    location = input("Local: ")

   
    while ((len(password)<5) or (password.isalnum()==True or password.isalpha()==True)):
   
             password = input("A sua senha necessita estar dentro dos requisitos.")
   
    email = input("Qual o seu email? ")
   
    for i in email:
   
        if("@" in email):
   
            break
   
    else:
   
        email = input ("O seu email tem que possuir @, por favor, tente novamente.")
   
    person = {"name:{}" .format(name+" "+middlename),"Local:{}".format(location),"password:{}".format(password),"Email:{}".format(email)}
   
    print(person)
   
    total = 0
   
    total = total + 1
   
    if (total == 1):
   
        accont1 = { }
   
        accont1 = person.copy()
   
        print("A sua conta foi redefinida com o nome de accont1")
   
    elif (total == 2):
   
        accont2 = person.copy()
   
        del person
   
        print("A sua conta foi redefinida com o nome de accont2")
   
    if (total == 3):
   
        accont3 = person.copy()
   
        print("A sua conta foi redefinida com o nome de accont3")
   
    elif (total == 4):
   
        accont4 = person.copy()
   
        print("A sua conta foi redefinida com o nome de accont4")
   
    cash = 0
   
    deposit = 0
   
    take = 0
   
    def endcodeaccont():
   
        if(total == 1):           
   
           print(accont1)
   
           accont1.clear()
   
        elif(total == 2):
   
           print(accont2)
   
           accont2.clear()
   
        if(total == 3):
   
           accont3.clear()
   
           print(accont3)
   
        elif(total == 4):
   
           accont4.clear()
   
           print(accont4)
   
    endcodeaccont()



    def menu():  

        cash = 0

        for i in range(0,4):                       

            menu = int(input("Ações avaliaveis: \n1-Faça um deposito \n2-Saque dinheiro \n3-Confira seu saldo \n4-Transfira seu dinheiro \n5-SAIR")) 

            if(menu == 1):

                deposit = float(input("Qual a quantia a ser depositada? "))

                cash = cash + deposit

                print("Saldo:",cash)

                while(deposit<0):

                     deposit = float(input("Por favor, tente novamente com um saldo positivo."))

                     if(deposit >= 0):

                        cash = cash + deposit

                        print("O seu saldo é de:",cash)

                     else:

                         pass

            elif (menu == 2):

                take = float(input("Saque dinheiro: "))

                cash = cash - take

                while (take > cash):

                      take = float(input("Sinto muito, parece que seu saldo não é o suficiente para realizar essa ação, verifique se o valor desejado está disponível na sua conta, caso ele esteja, tente novamente e não esqueça de verificar todos os números estão corretos. Obrigada pela atenção."))

                      cash = cash - take

            elif (menu == 3):

                       print("O seu saldo é de:",cash)

            elif(menu == 4):

                    transfer = float(input("Faça uma transferência"))

                    cash = cash - transfer

                    print("O seu saldo é de:",cash)


            elif(menu == 5):


                     endcode = input("Deseja encerrar a sessão? (y/sim)")

                     if (endcode == "y"):

                         endcodeaccont()

                     else:

                         pass

            else:

                 pass


    menu()
