from datetime import datetime

# Uzvārds, klase

"""Dotam gadskaitlim
atgriež True, ja garais gads
vai False, ja nav garais gads
"""
def vaiGaraisGads(gads):
    # TODO: tavs algoritms
    pass  


""" Dotam mēnesim atgriež dienu skaitu """
def dienuSkaits(menesis, garaisGads = False):
    # TODO: tavs algoritms
    pass


""" Pārbauda, vai ievaddati derīgi """
def ievaddatuParbaude(datums):
    # TODO: tavs algoritms
    pass


""" Drukā kalendāru """
def kalendars(dienuSkaits, menesis, gads):
    print("Pr Ot Tr Ce Pk Se Sv")  # dienu nosaukumi
    pirmaMenesaDiena = int(datetime(int(gads), int(menesis), 1).weekday() + 1)  # mēneša pirmā diena
    diena = 1  # iestata skaitītāju dienām
    nedelasDiena = 1  # iestata skaitītāju nedēļas dienām

    print("   " * (pirmaMenesaDiena - 1), end="")  # izdrukā tukšās dienas mēneša sākumā
    nedelasDiena += pirmaMenesaDiena  # uzsāk skaitīt pirmās nedēļas dienas
        
    while diena <= dienuSkaits:  # kamēr nav izvadītas visas mēneša dienas
        rindas_beigas = ""

        if nedelasDiena % 7 == 1:  # ja beigusies nedēļa
            rindas_beigas = "\n"
            nedelasDiena = 1  # atiestata nedēļas dienu skaitītāju

        if diena < 10:
            print(f"{diena}  ", end=rindas_beigas)  # drukā viencipara skaitli
        else:
            print(f"{diena} ", end=rindas_beigas)  # drukā divciparu skaitli

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
