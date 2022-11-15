Ieskaites uzdevums. Kalendārs.
---
## Problēmas apraksts:
Kalendārajā gadā ir 12 mēneši. Katram mēnesim ir noteikts dienu skaits. Februārī var būt 28 dienas īsajā gadā vai 29 dienas garajā gadā. Nedēļu skaits mēnešos var būt dažāds.

## Specifikācija:
### Koda 3. rindā komentārā ieraksti uzvārdu un klasi, citādi darbs netiks vērtēts!

Algoritmam jādarbojas sekojoši:

1. :heavy_check_mark: Programma prasa ievadīt datumu kā tekstu
2. Pārbauda, vai datums ir derīgs
3. Nosaka, vai dotais gads ir garais gads
4. Nosaka dienu skaitu dotajam mēnesim un gada garumam
5. :heavy_check_mark: Nosaka mēneša pirmo dienu un izdrukā kalendāru

Papildini doto kodu ar iztrūkstošo algoritma daļu!

### Funkcija ievaddatuParbaude():

Saņem parametru datums, kas ir teksts formātā "mm/yyyy".
Ja ievadītās datuma virknes garums ir 7 un virknes 3. simbols ir "/", un pārējie simboli ir cipari, tad atgriež True.
Citādi atgriež False.

### Funkcija vaiGaraisGads():

![Leap_year](/flowchart.png)

Ja gadskaitlis dalās gan ar 400, gan ar 4, gan ar 100 bez atlikuma, tad tas ir garais gads un atgriež True. Ja gadskaitlis dalās ar 4, bet nedalās ar 100, tad tas ir garais gads, atgriež True. Citos gadījumos tas nav garais gads, atgriež False.

### Funkcija dienuSkaits():

Padoti divi parametri:
* menesis - skaitlis no 1 līdz 12
* garaisGads - True vai False (noklusēti False)

Funkcija atgriež 28 vai 29 vai 30 vai 31 atkarībā no dotajiem parametriem

---
Ja sastādītās funkcijas darbosies korekti, ekrānā ieraudzīsi kalendāru ievadītajam mēnesim un gadam.
