"""
3. Feladat
Írj egy programot, amely a felhasználótól betűket kér be mindaddig, amíg az nem ad meg betűt, csupán egy ENTER-t üt!

A program vizsgálja meg a megadott betűt, és tárolja el egy listában, ha az még nem szerepel benne (a felhasználó korábban még nem adta meg)! 

A program NE különböztesse meg a kis- és nagybetűket egymástól, de olyan formában tárolja el a betűket mindig, ahogy a felhasználó megadta.

Ha a megadott betű már szerepel a listában írja ki, a képernyőre, hogy "Ezt a betűt már rögzítettem."!

Minden egyes adatbekérés után írja ki a már rögzített betűket ábécé sorrendben (elöl a nagybetűk, utána a kisbetűk ábécé sorrendben)!

"""
betuk = []

while True:
    betu = input("Adj meg egy betűt (ENTER = vége): ")

    if betu == "":
        break

    betu = betu[0]

    if betu.lower() in [b.lower() for b in betuk]:
        print("Ezt a betűt már rögzítettem.")
    else:
        betuk.append(betu)

    nagybetuk = sorted([b for b in betuk if b.isupper()])
    kisbetuk = sorted([b for b in betuk if b.islower()])

    print("Rögzített betűk:", nagybetuk + kisbetuk)
