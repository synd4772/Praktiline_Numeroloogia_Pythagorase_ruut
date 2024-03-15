
from Pythagorase_ruut import data


synnipaev =  "5.12.1979"
formated_synnipaev = synnipaev.split(".")
paev = int(formated_synnipaev[0])
kuu = int(formated_synnipaev[1])
aastat = int(formated_synnipaev[2])

summa1 = paev + int(str(kuu)[0]) + int(str(kuu)[1])
aastat_summa = 0
for arv in str(aastat):
    aastat_summa += int(arv)

summa1 += aastat_summa
summa2 = 0
for arv in str(summa1):
    summa2 += int(arv)
print(int(str(aastat)[0]))
summa3 = summa1 - 2 * int(str(synnipaev)[0])

summa4 = int(str(summa3)[0]) + int(str(summa3)[1])

esimene_arved = str(summa1) + str(summa2) + str(summa3) + str(summa4)
teine_arved = str(paev) + str(kuu) + str(aastat)

temp_esimene_ja_teine_arved = esimene_arved + teine_arved
var_continue = True

def FindSameNumbers(lst): 
    temp_lst = list(lst)
    esimene_arved_jarjend = [[],[]]
    for index, arv in enumerate(temp_lst):
        if lst.count(arv) > 1:
            var_continue = True
            temp_arv = str(arv)
            temp_lst[index] = None

            if len(esimene_arved_jarjend[0]) == 0:
                esimene_arved_jarjend[0].append(temp_arv)
                esimene_arved_jarjend[1].append(1)
                continue
            for indeks, i in enumerate(esimene_arved_jarjend[0]):
                if str(temp_arv) == str(i):
                    esimene_arved_jarjend[1][indeks] += 1
                    var_continue = False
                    continue
            if var_continue is True:
                esimene_arved_jarjend[0].append(temp_arv)
                esimene_arved_jarjend[1].append(1)
        else:
            esimene_arved_jarjend[0].append(arv)
            esimene_arved_jarjend[1].append(1)

    return esimene_arved_jarjend

formatted_user_numbers = FindSameNumbers(temp_esimene_ja_teine_arved)
lst = list()
for indeks, y in enumerate(formatted_user_numbers[0]):
    lst.append(y * formatted_user_numbers[1][indeks])


print(lst)
def CheckSameNumbersInMatrics():
    characther = list()
    for indeks, i in enumerate(lst):
        for dict_indeks in data.keys():
            if int(i[0]) == dict_indeks:
                for dict_element in data[dict_indeks].keys():
                    if dict_element == int(i):
                        characther.append(data[dict_indeks].get(dict_element))
            else:
                print(dict_indeks, "ggg")
    return characther
        
print(CheckSameNumbersInMatrics())