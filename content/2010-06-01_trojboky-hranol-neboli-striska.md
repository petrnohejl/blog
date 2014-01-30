Title: Trojboký hranol neboli stříška
Category: Vaření

Několik měsíců zpátky jsem přišel opilý domů (z informatické pitky) a v
opilosti jsem Janie slíbil, že jí vyrobim dort. Aspoň to mi druhý den
tvrdila. Jestli to tak opravdu bylo jsem si druhý den vážně nepamatoval,
ale důležité je, že jsem svůj slib splnil (sic několik týdnů/měsíců
poté). Jednoho dne jsem se rozhodl Janie překvapit a zkonstruoval jsem
sladké trojboké hranoly, neboli stříšky. Jako obvykle přicházím s
receptem na tento velmi jednoduchý a přitom velice lahodný zákusek,
chcete-li dortík.

Potřebovat budeme tyto přísady:

- sušenky BeBe cereální (světlé)
- sušenky BeBe kakaové (tmavé)
- 500 g měkkého tvarohu (obvykle tedy 2 vaničky)
- 2 banány
- cukr
- alobal

Na pekáč nebo nějaké velké prkno natáhneme alobal. Výška prkna musí být
větší nebo rovna trojnásobku velikosti té delší strany BeBe sušenky.
Minimální šířka prkna je potom dána velikostí kratší strany BeBe
sušenky, násobenou koeficientem `k`, pro které platí podmínka: `k >= 1
and k <= (celkový_počet_sušenek / 6)`, kde `k` značí počet
požadovaných trojbokých hranolů, tedy jednotlivých zákusků. V dalším
kroku vytvoříme z BeBe sušenek dvojrozměrné pole neboli matici, která
bude mít 3 řádky a `k` sloupců, přičemž hodnoty (světlé a tmavé BeBe
sušenky) jsou v matici uspořádány střídavě z hlediska řádků i sloupců.
Sušenky uspořádáváme v řádku matice vedle sebe tou delší stranou
sušenky. Vše je dobře vidět na ukázkové fotce.

Nyní si do misky vložíme tvaroh a spolu s cukrem rozmícháme. Množství
cukru uvážíme dle chuti. Vznikne nám krém, kterým budeme potírat pomocí
nože nebo stěrky vytvořenou matici sušenek. Při potírání krémem se
sušenky hýbou, posouvají a ruší tak pravidelně uspořádanou strukturu
(pole sušenek). Proto je dobré si okraje matice zaaretovat, např. pomocí
dalšího prkénka, nebo čehokoliv (viz fotka). Hlavně aby se to
neposouvalo a dobře se to mazalo. Na první nátěr použijeme polovinu
celkového množství krému, protože nátěry budou celkem dva.

![Sušenky, krém a banán]({filename}images/trojboky-hranol-neboli-striska-01.jpg)

Poté co jsme řádně a rovnoměrně rozetřeli krém, vytvoříme druhou vrstvu
sušenek, tzn. další matici. Vzniká nám tedy trojrozměrné pole, neboli
pole matic. Druhou vrstvu sušenek skládáme uplně stejně jako první,
akorát do druhé matice na stejné pozice vkládáme inverzní hodnotu z
první matice. Pokud tedy byla na dané pozici v první vrstvě světlá
sušenka, přiložíme na ní do druhé vrstvy tmavou sušenku a naopak. Poté
co máme i druhou vrstvu pokrytou, potřeme ji rovnoměrně zbytkem krému.

Nakonec nakrájíme zkroucený banán na menší části a pokládáme navrch
vytvořené struktury v horizontálním směru (viz fotka). Separací banánu
na menší fragmenty eliminujeme nežádoucí vlastnost kroucení banánu. Na
závěr je potřeba z rovinného objektu vytvořit trojboký hranol. To
uděláme velice efektivně pomocí podloženého alobalu. Uchopíme tedy dva
opačné konce alobalu na krajích přibližně v místě prostředku řádku a
tyto konce opatrně přiklopíme k sobě tak, aby se krajní řádky objektu
zvedly a spojily se do hranolu. Vše opět znázorňuje fotka.

![Trojboký hranol]({filename}images/trojboky-hranol-neboli-striska-02.jpg)

Výsledkem je jeden velký trojboký hranol, který se posléze nožem nakrájí
na `k` zákusků, podle sloupců matice. Hranol je dobré uchovávat v chladu
a nechat jej před konzumací několik hodin rozležet, aby se sušenky
nasákly krémem a změkly. Hranol je dále možné vylepšovat, např.
čokoládovou polevou apod. Doufám, že je tento poněkud matematický recept
pochopitelný :) Přeji dobrou chuť.

![Zákusek]({filename}images/trojboky-hranol-neboli-striska-03.jpg)
