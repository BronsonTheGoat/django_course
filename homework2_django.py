"""
1) Készíts egy külön modellt a szerzőknek az alábbi mezőkkel:
    - név, születési dátum és hely, nemzetiség, halálozás dátuma és helye (utóbbi 2 lehet üres)

2) Kapcsold össze a szerzők modellt a könyvekkel, lecserélve a korábbi szerző mezőt!
   Egy szerzőnek több könyve is lehet, de egyelőre egy könyvnek csak egy szerzője (ForeignKey).

3) Regisztráld a szerzők modelljét is az adminba, és állítsd be az alábbiakat:
    - list_display, search_fields, ordering
    - filterek: nemzetiség
    - könyvek inline

4) Készíts egy view-t, amely kilistázza az összes szerzőt!
5) Készíts egy view-t, ami az egyes szerzők adatait mutatja az url-ben lévő id alapján!
   Ezen az oldalon listázd ki az adott szerző könyveit is!

6) Adatok importálása
    a) Készíts egy management command-ot, amely beolvas egy csv fájlt és feltölti a megfelelő
    adatokat az Author táblába!
    b) Készíts egy management command-ot, amely beolvas egy csv fájlt és feltölti a megfelelő
    adatokat a Book táblába!
    Kezeld azt az esetet is, ha a megadott szerző még nem szerepel az adatbázisban:
    hagyd ki az adott sort, és írj ki hibaüzenetet!
"""