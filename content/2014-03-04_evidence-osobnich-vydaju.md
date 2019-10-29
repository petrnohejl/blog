Title: Evidence osobních výdajů
Category: Informační technologie

Už nějakou dobu plánuju, že si začnu evidovat osobní výdaje. Je dobré mít základní přehled, kolik člověk utratí za jídlo, bydlení, dopravu atd. Existuje hromada mobilních aplikací na evidenci výdajů, ale používání takové aplikace je vcelku otravné - ťukat si do mobilu každý výdaj by mě fakt nebavilo. Navíc bych na to určitě i často zapomínal.

Chci nějaký základní přehled výdajů za jednotlivé měsíce v roce. Položky by měly být kategorizované (jídlo, doprava, dovolená apod.). Výstupem by měla být tabulka a nějaké grafy. Evidence příjmů mě nezajímá - na to mám zase jiné [nástroje](https://fakturoid.cz). Navíc příjmy z podnikání mi tečou na podnikatelský účet, nikoliv osobní. Přemýšlel jsem, jak nejsnáze celý tento problém řešit a dospěl jsem k následujícímu.

## Expenses.py

Vzhledem k tomu, že téměř všechno platím přes banku kartou nebo převodem (výjimkou jsou restaurace), využiju export transakcí z internetového bankovnictví. Fio banka podporuje CSV export, který půjde pro mé potřeby krásně použít. Mohl bych také použít [Fio API](https://www.fio.cz/bankovni-sluzby/api-bankovnictvi) pro vývojáře a naprogramovat si na to nějakou vlastní aplikaci, ale nepotřebuju mít evidenci výdajů automatizovanou. Stačí mi statistiku udělat max. jednou za kvartál a sledovat, jak se vyvíjí trendy. Stáhnout 4x za rok CSV soubor z bankovnictví není pro mě přítěž. Preferuji jednoduché řešení, takže jsem Fio API prozatím zavrhl.

Data bych tedy měl - CSV soubor z Fio bankingu. Nyní potřebuju data upravit a zobrazit v čitelné podobě. Napsal jsem si jednoduchý Python skript [expenses.py](https://github.com/petrnohejl/Expenses), který ten CSV soubor upraví a provede automatickou kategorizaci. Skript provede celkem 3 modifikace:

- Invertuje znaménko u peněžních částek, takže výdaje jsou kladné a příjmy záporné. Je to kvůli koláčovému grafu (na grafu nelze zobrazit záporné hodnoty).
- Přidá sloupeček s měsícem. V CSV tabulce je sice datum, ale to neumí kontingenční tabulka zpracovat. K měsíci navíc přidá prefix s číslem, protože v Google Doc se sloupečky řadí podle abecedy a nepřišel jsem na to, jak to řadit podle pořadí v tom původním CSV. Např. pro platbu uskutečněnou v březnu přidá skript popisek _"03 březen"_.
- Přidá sloupeček s kategorií. Ty jsou detekovány automaticky pomocí regulárních výrazů.

Upravené CSV následně importuji do Google Doc a vytvořím [kontingenční tabulku](https://cs.wikipedia.org/wiki/Kontingen%C4%8Dn%C3%AD_tabulka). Z kontingenční tabulky si dále vygeneruji grafy. Výsledkem jsou pěkné statistiky, kde mám všechny důležité údaje, které mě zajímají. Samozřejmě tam budou nějaké nepřesnosti, ale pro základní přehled výdajů to stačí.

## Jak si za 10 minut vyrobit přehled výdajů za celý rok

Zde uvádím podrobný návod, jak si pomocí mého skriptu rychle vytvořit pěknou evidenci výdajů.

 1. Stáhneme si CSV soubor z Fio banky: _Přehledy -> Pohyby -> Exportovat data jako CSV formát_ (ikonka v horní liště). Nezapomeneme nastavit období, za které budeme statistiku tvořit.
 2. CSV soubor proženeme Python skriptem [expenses.py](https://github.com/petrnohejl/Expenses). Skript se spustí příkazem `python expenses.py mydata.csv`. Výstupem je nový CSV soubor _mydata\_categorized.csv_.
 3. V Google Doc si vytvoříme novou tabulku a importujeme upravené CSV: _Soubor -> Importovat_. Akce importu: _Nahradit aktuální list_. Znak oddělovače: _Vlastní: středník_.
 4. Odstraníme metadata v tabulce: _Označit řádky -> Smazat řádky 1-n_. Fio na začátek a konec CSV přidává nějaký balast navíc (info o účtu, období, stav účtu atd.).
 5. Nastavíme si automatickou šířku sloupců: _Označit sloupce -> Změnit velikost sloupců A-N -> Přizpůsobit datům_.
 6. U sloupce _měsíc_ nastavíme typ dat jako text: _Formát -> Číslo -> Prostý text_. Je to proto, abychom předešli automatickému přepsání _"09 září"_ na _"9.9.2014"_, což se mi právě stalo.
 7. Nyní ručně zkontrolujeme kategorie, zda jsou správně přiřazeny. Hlavně je potřeba zkontrolovat kategorii _Dary_, jelikož se těžko detekuje. Doplníme kategorie tam, kde chybí. V mém případě skript detekoval kategorii u cca 80% transakcí, ale před kategorizací jsem samozřejmě upravil regulární výrazy v [expenses.py](https://github.com/petrnohejl/Expenses) tak, aby pokryly co nejvíce položek.
 8. Vytvoříme kontingenční tabulku: _Data -> Přehled kontingenčních tabulek_.
 9. Nakonfigurujeme kontingenční tabulku. Řádky: _Kategorie_. Sloupce: _Měsíc_. Hodnoty: _Objem_ jako _SUM_.
10. Nastavíme filtr: _Kategorie_. Odfiltrujeme kategorii _Interní transakce_, protože tato kategorie zahrnuje tok peněz mezi mými účty (osobní, podnikatelský, spořící). Tím se odfiltrují i hlavní příjmy, které mě nezajímají a v grafech by navíc mohly dělat neplechu kvůli záporným hodnotám.
11. Vytvoříme si tři grafy (sloupcový, skládaný pruhový, výsečový): _Vložit -> Graf_. U všech grafů využijeme v nastavení (záložka _Přizpůsobit_) funkci _Maximalizovat_, aby byl graf zvětšený na celou obrazovku. Po vytvoření grafu aplikujeme funkci _Přesunout do vlastního listu_, aby byl každý graf ve zvlášť záložce.

Výsledný dokument má 5 listů: CSV data, kontingenční tabulka a 3 grafy. Následuje ukázka výstupů. Použitá data jsou smyšlená.

![CSV data]({filename}images/evidence-osobnich-vydaju-01.png)

![Kontingenční tabulka]({filename}images/evidence-osobnich-vydaju-02.png)

![Sloupcový graf]({filename}images/evidence-osobnich-vydaju-03.png)

![Skládaný pruhový graf]({filename}images/evidence-osobnich-vydaju-04.png)

![Výsečový graf]({filename}images/evidence-osobnich-vydaju-05.png)

## Jiné alternativy

Na závěr bych rád zmínil nějaké alternativy k mému řešení evidence výdajů pomocí expenses.py. Zajímavý je [skript od Filipa Hráčka](https://plus.google.com/u/0/111783114889748547827/posts/BZnsgkYdkA4), který využívá [Fio API](https://www.fio.cz/bankovni-sluzby/api-bankovnictvi) a technologii [Google Apps Script](https://www.google.com/script/start/). Ačkoliv uvedené video sklidilo ostrou [kritiku](https://www.lupa.cz/clanky/google-vam-zadarmo-zkontroluje-bankovni-vypis-je-o-co-stat/) kvůli bezpečnostním problémům, příjde mi to jako vcelku zajímavé řešení.

Další možností pro evidenci výdajů je skript [finances.py](https://github.com/honzajavorek/finances), který napsal kamarád Honza Javorek. Tenhle skript opět využívá Fio API a transakce ukládá do tabulky v Google Doc. Ze získaných dat lze poté vytvářet kontingenční tabulky a grafy.

Jako poslední alternativu bych chtěl zmínit nové [internetové bankovnictví od mBank](https://www.mbank.cz/osobni/sluzby/internetove-bankovnictvi/spravce-financi/index.html). Zde se objevila funkce, která umožňuje zařazovat jednotlivé peněžní operace do kategorií a třídit podle tagů. Následně lze zobrazit různé přehledy příjmů/výdajů a grafy.

A jak si evidujete své osobní výdaje vy? Napište do diskuse!
