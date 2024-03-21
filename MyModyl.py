
# +====================================================================================================+
# | 1.Ma ei pruugi ülesandest õigesti aru saada, aga ma olen midagi teinud ja see justkui töötab.      |
# +----------------------------------------------------------------------------------------------------+

from customInterface import warning # minu isiklik moodul, kus hoitakse erinevate raamidega informatsiooni väljundi funktsioone jne
from Pythagorase_ruut import data
from time import sleep
import re  # regulaaravaldiste moodul, väga ammu uurinud ja otsustanud, et nüüd saab seda rakendada, et töötada ridade ja andmete paigutusega

# +-----------------------------------------------------------------------------------+
# |                             SAVE AND LOAD USERS DATA                              |
# +-----------------------------------------------------------------------------------+

data_file = "users_data.txt"  # Fail, kus hoitakse kasutajate andmeid
user_find_pattern = r"(?P<name>\w+): (?P<synniaeg>.*);(?P<numbrid>\w+)"  # "match()" meetodi kasutamisel grupeeritakse andmed selle järgi

temp_users_data = list()  # kõigi andmete säilitamine lokaalselt töö lihtsustamiseks


def DataFormatting(nimi: str, aeg: str, numbrid: str) -> str:
    """Ridade vormindamise funktsioon antud argumentidest on määratud funktsiooniga

    :param nimi:
    :param aeg:
    :param numbrid:
    :rtype: str
    """
    return f"{nimi}: {aeg};{numbrid}\n"


def SaveToUsersData(data: str):
    """Funktsioon, mis avab küsitletud kasutajate faili ja salvestab sinna uue kasutaja

    :param data:
    :return:
    """
    with open(file=data_file, mode="a", encoding="utf-8") as f:
        f.write(data)


def LoadFromUsersData():
    """Funktsioon, mis laadib failist üles kõik kasutajad ja laadib need üles kohalikku nimekirja, et lihtsustada nende kasutamist

    :return:
    """
    temp_users_data.clear()
    with open(file=data_file, mode="r", encoding="utf-8") as f:
        lines = f.readlines()
        for line in lines:
            match = re.match(user_find_pattern, line.strip())
            if match:
                temp_users_data.append(match.groupdict())


LoadFromUsersData()
warning("Kasutajate andmed laaditi üles lokaalselt.", after="")


# +-----------------------------------------------------------------------------------+
# | Huvitav fakt on see, et töö andmebaasiga algas esmakordselt alates 1955. aastast. |
# +-----------------------------------------------------------------------------------+


def FindSameNumbers(temp_esimene_ja_teine_arved:str) -> list:
    """Funktsioon, kus me otsime samu numbreid edastatavast reaargumendist ja tagastame kõik lehe sissevaated

    :param temp_esimene_ja_teine_arved:str
    :return:
    """
    temp_lst = list(temp_esimene_ja_teine_arved)
    esimene_arved_jarjend = [[str(i) for i in range(1, 10)], [0 for _ in range(1, 10)]]
    for index, arv in enumerate(temp_lst):
        temp_arv = str(arv)
        for indeks, i in enumerate(esimene_arved_jarjend[0]):
            if str(temp_arv) == str(i):
                esimene_arved_jarjend[1][indeks] += 1
    return_list = list()
    for index, i in enumerate(esimene_arved_jarjend[0]):
        return_list.append(0 if esimene_arved_jarjend[1][index] == 0 else i * esimene_arved_jarjend[1][index])
    return return_list


def CheckSameNumbersInMatrics(user_numbers: list) -> list:
    """Funktsioon kasutab sõnaraamatut moodulis "Pythaorase_ruut.py" koos edastatavate argumentidega loendi vaates

    :param user_numbers: list
    :return:
    """
    characther = list()
    for key_dict, element_dict in data.items():
        for key, element in element_dict.items():
            if int(user_numbers[key_dict - 1]) == key:
                (characther.append(element) if element != "" else None)
    return characther


def BirthdayCalculation(aastat: int, kuu: int, paev: int) -> str:
    """Funktsioon, mis arvutab su sünnipäeva ja annab Pythagorase meetodi järgi välja kammimise tulemuse

    :param aastat:
    :param kuu:
    :param paev:
    :return:
    """
    sunniaeg = f"{paev}.{kuu}.{aastat}"
    summa1 = int(str(paev)[0]) + (int(str(paev)[1]) if len(str(paev)) > 1 else 0) + int(str(kuu)[0]) + (int(str(kuu)[1]) if len(str(kuu)) > 1 else 0)
    aastat_summa = 0

    for arv in str(aastat):
        aastat_summa += int(arv)

    summa1 += aastat_summa

    summa2 = 0
    for arv in str(summa1):
        summa2 += int(arv)

    summa3 = summa1 - 2 * int(sunniaeg[0])
    summa4 = 0
    for i in str(summa3):
        summa4 += int(i)

    esimene_arved = str(summa1) + str(summa2) + str(summa3) + str(summa4)
    teine_arved = str(paev) + str(kuu) + str(aastat)

    return esimene_arved + teine_arved


def InformationDisplay(information: list):
    """Funktsioon, mis näitab õiges järjekorras 7-9 fakti sinu kohta

    :param information:
    :return:
    """
    print("+------------------Teavet sinu kohta!------------------+")
    for indeks, i in enumerate(information):
        sleep(2)
        print(f"{indeks + 1}. {i}")
    print("+------------------------------------------------------+")


def FindDataByValue(value: any, find_data: str, datas: list) -> any:
    """Funktsioon, mis leiab edastatavast loendist õige loendi ja tagastab loendi väärtuse "find_data"

    :param value:
    :param find_data:
    :param datas:
    :return:
    """
    for dict in datas:
        for _, dict_value in dict.items():
            if value == dict_value:
                return dict.get(find_data)

def AnswerConvert(answer: str):
    """Funktsioon, mis teisendab edastatava argumendi "True" või "False",
     sõltuvalt sellest, mida esimene leiab funktsioonis loetletud loenditest

    :param answer:
    :return:
    """
    true_list = ['1', 'JAH', 'YES', 'ДА']
    false_list = ['0', 'EI', 'NO', 'НЕТ']

    if any(i in answer.upper() for i in true_list):
        return True
    elif any(i in answer.upper() for i in false_list):
        return False
    else:
        return None


# +----------------------------------------------------------------+
# |                     VARIABLE CHECK METHODS                     |
# +----------------------------------------------------------------+

def VariableCheck(kusimus: str, veateade: str, kontroll_funktsioon: any, while_condition=True) -> any:
    """Mõistmiseks üsna raske funktsioon, kuid selle sisuks on küsida kasutajalt küsimust,
    mis edastatakse argumendiga "kusimus" ja seda vastust, mille kasutaja on kirjutanud,
    kontrollitakse argumentides märgitud funktsiooni abil, mis tuleb edastada kindlasti juhul,
    kui ei leita seda, mida "None" peab programmi enda tööks tagastama.
    Juhul, kui argumendis märgitud funktsioon väljutab "None" ja loogika järgi söömine ei leia seda,
    mida vaja, kirjutame kasutajale vea, mis edastatakse argumendis "veateade".
    Funktsiooni "while_None" jaoks on olemas poliisieelne parameeter,
    mis võtab ainult kaks väärtust "True" või "False", kui "True" siis funktsioon kontrollib,
    et EI LI, ja kui "False" siis kontrollib, kas LI on olemas.

    :param kusimus:
    :param veateade:
    :param kontroll_funktsioon:
    :param while_is_None:
    :return:
    """
    x = while_condition
    vastus:any
    while x is while_condition:
        vastus = input(kusimus)
        x = kontroll_funktsioon(vastus)
        if x is while_condition:
            print(veateade)
            sleep(1)
    return vastus


def FindNameInLocalData(nimi: str) -> any:
    """Funktsioon jämedalt öeldes lihtsalt otsib nime küsitletud kasutajate kohalikust baasist.
    Hoiatus: Funktsioon on mõeldud "VariableCheck" abivahendiks, kuid vajadusel saab seda kasutada ka niisama.

    :param nimi:
    :return:
    """
    for dict_ in temp_users_data:
        for _, value in dict_.items():
            if nimi == value:
                print(True)
                return True
    return False


def YearVerification(aastat: str) -> any:
    """Funktsioon aasta kontrollimiseks.
    Hoiatus: Funktsioon on mõeldud "VariableCheck" abivahendiks, kuid vajadusel saab seda kasutada ka niisama.

    :param aastat:
    :return:
    """
    if 4 < len(aastat) or len(aastat) < 4:
        return False
    return True


def MonthVerification(kuu: str) -> any:
    """Funktsioon kuu õigsuse kontrollimiseks.
    Hoiatus: Funktsioon on mõeldud "VariableCheck" abivahendiks, kuid vajadusel saab seda kasutada ka niisama.

    :param kuu:
    :return:
    """
    if 0 < int(kuu) <= 12:
        return True
    return False


def DayVerification(paev: str) -> any:
    """Funktsioon päeva õigsuse kontrollimiseks.
    Hoiatus: Funktsioon on mõeldud "VariableCheck" abivahendiks, kuid vajadusel saab seda kasutada ka niisama.

    :param paev:
    :return:
    """
    if 0 < int(paev) <= 31:
        return True
    return False

