from MyModyl import *

while True:
    sleep(1)
    print("Tere, see on oma ruudu arvutus Pythagorase meetodil!\nKas sa tahad teada oma pythagorase ruutu(0) või leida nime(1)?\n")
    vastus = int(VariableCheck("Mida te tahate? ", "Vale vastus!", AnswerConvert, while_condition=None))
    if vastus == 0:
        nimi = VariableCheck("Mis sinu nimi on? ", "See nimi oli juba!", FindNameInLocalData)
        print(nimi)
        aastat = VariableCheck("Mis on sinu sünniaasta? ", "Vale sünniaasta, proovi uuesti", YearVerification, while_condition=False)
        kuu = VariableCheck("Milline on sinu sünnikuu? ", "Vale sünniakuu, proovi uuesti", MonthVerification, while_condition=False)
        paev = VariableCheck("Mis on su sünnipäev? ", "Vale sünniapaev, proovi uuesti", DayVerification, while_condition=False)

        esimene_ja_teine_numbrid = BirthdayCalculation(int(aastat), int(kuu), int(paev))

        SaveToUsersData(DataFormatting(nimi, f"{paev}.{kuu}.{aastat}", esimene_ja_teine_numbrid))

        information = CheckSameNumbersInMatrics(FindSameNumbers(esimene_ja_teine_numbrid))
        InformationDisplay(information)

        warning("Teie andmed on salvestatud meie kasutajate andmebaasi!")
        sleep(1)

    elif vastus == 1:
        if len(temp_users_data):
            nimi = VariableCheck("Mis sinu nimi on? ", "See nimi ei ole!", FindNameInLocalData, while_condition=False)
            numbrid = FindDataByValue(nimi, "numbrid", temp_users_data)

            information = CheckSameNumbersInMatrics(FindSameNumbers(numbrid))
            InformationDisplay(information)

    sleep(0.5)
    print("Programm on lõpetatud. \n")
