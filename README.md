# Tietoa lammotv2.py ohjelmasta

lammotv2.py tiedosto tuottaa tällä hetkellä satunnaista tietoa (esim. cpu muuttuja = cpu lämpö -> 80 - 85 välillä) ja sen pitää olla päällä
että "/chart" html-sivu näyttää taulukon.

lammotv2.py tiedostosta vaihtamalla muuttujat cpu, cpupros, rampros saataisiin raspberrystä nämä tiedot seuraavasti (tarvitaan myös 'import psutil') :

- cpu = CPUTemperature ()
- cpupros = psutil.cpu_percent(interval=1) # yhden sekunnin välein
- rampros = psutil.virtual_memory().percent

jos haluaa vielä että raspberry lähettää jatkuvasti niin lammotv2.py while lauseke voidaan muuttaa 'while alfa < 100:' -> 'while (True):'
+ samalla poistaa muuttujat esim. alfa joka laskee "testi" kerrat.


***Lammot.py tiedosto sisältää python koodin jota olemme jo aiemmin käyttänyt raspberrypi:n kanssa, mutta tämä versio lähettää mqtt:n  avulla Thingspeak kanavallemme tietoa.***

**Tekijät:** Joona Säntti, Riku Tomann
