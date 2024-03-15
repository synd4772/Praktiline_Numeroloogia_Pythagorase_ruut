from MyModyl import *

while True:
    sleep(1)
    print("Tere, see on oma ruudu arvutus Pythagorase meetodil!\nKas sa tahad teada oma pythagorase ruutu(0) või leida nime(1)?\n")
    vastus = int(VariableCheck("Mida te tahate? ", "Vale vastus!", AnswerConvert))
    if vastus == 0:
        nimi = VariableCheck("Mis sinu nimi on? ", "See nimi oli juba!", FindNameInLocalData, while_is_None = False)

        aastat = VariableCheck("Mis on sinu sünniaasta? ", "Vale sünniaasta, proovi uuesti", YearVerification)
        kuu = VariableCheck("Milline on sinu sünnikuu? ", "Vale sünniakuu, proovi uuesti", MonthVerification)
        paev = VariableCheck("Mis on su sünnipäev? ", "Vale sünniapaev, proovi uuesti", DayVerification)

        esimene_ja_teine_numbrid = BirthdayCalculation(aastat, kuu, paev)

        SaveToUsersData(DataFormatting(nimi, f"{paev}.{kuu}.{aastat}", esimene_ja_teine_numbrid))

        information = CheckSameNumbersInMatrics(FindSameNumbers(esimene_ja_teine_numbrid))
        InformationDisplay(information)

        sleep(1)
        print("Teie andmed on salvestatud meie kasutajate andmebaasi!")
    elif vastus == 1:
        if len(temp_users_data):
            nimi = VariableCheck("Mis sinu nimi on? ", "See nimi ei ole!", FindNameInLocalData)
            numbrid = FindDataByValue(nimi, "numbrid", temp_users_data)

            information = CheckSameNumbersInMatrics(FindSameNumbers(numbrid))
            InformationDisplay(information)

    sleep(0.5)
    print("Programm on lõpetatud. \n")
