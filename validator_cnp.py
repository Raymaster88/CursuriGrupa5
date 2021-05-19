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
            # if sex in [1, 3, 5, 7]:
                # print("Sex barbatesc")
            else:
                print("Sex femeiesc")
        except ValueError:
            print("Ziua nu este valida")
else:
    print("CNP incomplet")