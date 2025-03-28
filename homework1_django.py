"""
Valósítsuk meg a könyvtárprogramot weboldal formájában!

Első lépések:

1) Hozz létre egy új django projektet! Indítsd el a szervert, és nézd meg, működik-e a kezdőoldal!
2) Futtasd a migrate parancsot, hogy létrejöjjenek a kezdeti táblák!
3) Hozz létre egy superuser-t, amivel be tudsz lépni az adminra!
4) Hozd létre a könyvekhez tartozó modellt az alábbi adatokkal: isbn, cím, szerző, kiadás éve, oldalszám
5) Regisztráld a modellt az adminba! Állítsd be az alábbiakat:
    - list_display: cím, szerző, kiadás éve
    - ordering: cím, kiadás éve
    - filterek: kiadás éve, szerző
6) Készíts egy view-t, amely kilistázza az összes könyvet!
   Legyen keresési lehetőség is cím és szerző szerint!
7) Készíts egy view-t, ami az egyes könyvek adatait mutatja az url-ben lévő id alapján!
"""