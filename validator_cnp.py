import datetime

valoare_cnp = input('Introdu cnp-ul: ')

print(valoare_cnp[0])

if len(valoare_cnp) == 13:
    an = int(valoare_cnp[1:3])
    luna = int(valoare_cnp[3:5])
    zi = int(valoare_cnp[5:7])
    sex = int(valoare_cnp[0])
    if sex == 9:
        print('Persoana straina')
    else:
        try:
            data_de_comparat = datetime.datetime(int(f"19{an}"), luna, zi)
            # print(type(data_de_comparat))
            if sex == 1 and datetime.datetime(1900, 1, 1) < data_de_comparat < datetime.datetime(1999, 12, 31):
                print("Sex barbatesc nascut in intervalul 1900 - 1999")
            elif sex == 2 and datetime.datetime(1900, 1, 1) < data_de_comparat < datetime.datetime(1999, 12, 31):
                print("Sex femeiesc nascut in intervalul 1900 - 1999")

            elif sex == 3 and datetime.datetime(1800, 1, 1) < data_de_comparat < datetime.datetime(1899, 12, 31):
                print("Sex barbatesc nascut in intervalul 1800 - 1899")

            elif sex == 4 and datetime.datetime(1800, 1, 1) < data_de_comparat < datetime.datetime(1899, 12, 31):
                print("Sex femeiesc nascut in intervalul 1800 - 1899")

            elif sex == 5 and datetime.datetime(2000, 1, 1) < data_de_comparat < datetime.datetime(2099, 12, 31):
                print("Sex barbatesc nascut in intervalul 2000 - 2099")

            elif sex == 6 and datetime.datetime(1800, 1, 1) < data_de_comparat < datetime.datetime(2099, 12, 31):
                print("Sex femeiesc nascut in intervalul 2000 - 2099")

            elif sex == 7:
                print("Persoane de sex barbatesc, rezidente in Romania")

            elif sex == 8:
                print("Persoane de sex femeiesc, rezidente in Romania")

            # if sex in [1, 3, 5, 7]:
            # print("Sex barbatesc")
            # else:
            #     print("Sex femeiesc")
        except ValueError:
            print("Ziua nu este valida")
else:
    print("CNP incomplet")