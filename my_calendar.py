from datetime import datetime

"""Dotam gadskaitlim
atgriež True, ja garais gads
vai False, ja nav garaisa gads
"""
def vaiGaraisGads(gads):
    if gads % 4 == 0:
        if gads % 100 == 0:
            if gads % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

""" Dotam mēnesim atgriež dienu skaitu """
def dienuSkaits(menesis, garaisGads = False):
    if int(menesis) == 2:
        if garaisGads is True:
            return 29
        else:
            return 28
    elif int(menesis) in [4, 6, 9, 11]:
        return 30
    else:
        return 31

""" Pārbauda, vai ievaddati derīgi """
def ievaddatuParbaude(datums):
    if len(datums) == 7:
        if datums[2] == "/":
            if datums[:2].isdigit() and datums[3:].isdigit():
                return True
    return False

""" Drukā kalendāru """
def kalendars(dienuSkaits, menesis, gads):
    print("Pr Ot Tr Ce Pk Se Sv")  # dienu nosaukumi
    pirmaMenesaDiena = int(datetime(int(gads), int(menesis), 1).weekday() + 1)  # mēneša pirmā diena
    diena = 1  # iestata skaitītāju dienām
    nedelasDiena = 1  # iestata skaitītāju nedēļas dienām

    print("   " * (pirmaMenesaDiena - 1), end="")  # izdrukā tukšās dienas mēneša sākumā
    nedelasDiena += pirmaMenesaDiena - 1  # uzsāk skaitīt pirmās nedēļas dienas
        
    while diena <= dienuSkaits:  # kamēr nav izvadītas visas mēneša dienas
        if nedelasDiena % 7 == 1:  # ja beigusies nedēļa
            print("")  # pāriet jaunā rindā
            nedelasDiena = 1  # atiestata nedēļas dienu skaitītāju
        
        if diena < 10:
            print(f"{diena}  ", end="")  # drukā viencipara skaitli
        else:
            print(f"{diena} ", end="")  # drukā divciparu skaitli

        diena += 1  # skaita dienas
        nedelasDiena += 1  # skaita nedēļas dienas

""" Ievads """
datums = input("Datums (mm/gggg): ")

if ievaddatuParbaude(datums) is True:
    menesis = int(datums[:2])  # atdala mēnesi
    gads = int(datums[3:])  # atdala gadu

    dienas = dienuSkaits(menesis, vaiGaraisGads(gads))  # nosaka dienu skaitu
    kalendars(dienas, menesis, gads)  # drukā kalendāru
else:
    print("Ievaddati nederīgi!")
    
