import datetime
from operator import neg
from Repositories.RepositoryJson import RepositoryJson

accountBalance = float(input("Digite o valor hoje em conta: "))
monthStart = int(input("Digite o mês inicio: "))
currentMonth = datetime.datetime.now().month
totalExpenses = 0

repository = RepositoryJson("expenses.json")
result = repository.GetAll()

# Verifica se o resultado da leitura é válido
if(result["isValid"]):

    # caso válido carrega os dados da despesa
    expenses = result["data"]

    someExpenseWasAdded = False

    # Inicio trecho adicionar nova despesa
    while True:
        addExpenseYesNo = input("Deseja adicionar despesa? [S]im ou [N]ão: ")
        if(addExpenseYesNo.lower() == "s"):

            # Adiciona a nova despesa
            expenses.append({
                "Name" : input("Digite o nome da despesa: "),
                "Amount" : float(input("Digite o valor da despesa: ")),
                "NumerInstallments" : int(input("Digite a quantidade de parcelas: "))
            })
            someExpenseWasAdded = True
        else:
            # verifica se alguma nova despesa foi adicionada
            if(someExpenseWasAdded):
                resultadoSobreescrita = repository.Overwrite(expenses)
                if(not resultadoSobreescrita["isValid"]):
                    print(resultadoSobreescrita["error"])
            break             

    # Inicio calculo das parcelas e despesas
    for expense in expenses:
        expense["NumerInstallments"] = expense["NumerInstallments"] - (currentMonth - monthStart)
        totalExpenses += expense["NumerInstallments"] * expense["Amount"]

    # Inicio relatório
    print("") 
    print("Relatório:")
    print("") 
    for expense in expenses:
        print(f"Despesa: {expense['Name']} | Numero de Parcelas: {expense['NumerInstallments']} | Valor: R$ {expense['Amount']} | Valor total: {expense['NumerInstallments'] * expense['Amount']}")
        
    print("")
    print(f"Total das despesas: R$ {totalExpenses}")
    print(f"Saldo original: R$ {accountBalance}")

    finalAmountOnAccount = accountBalance - totalExpenses

    if(finalAmountOnAccount < 0):
        print(f"Saldo menos depesas: R$ {finalAmountOnAccount}")
        print(f"Você precisa ganhar R$ {neg(finalAmountOnAccount)} para não ficar endividado.")
    else:
        print(f"Saldo menos depesas: R$ {finalAmountOnAccount}")
else:
    print(result["error"])