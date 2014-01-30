Title: Projekt Mimikry - rozšířená realita
Date: 2011-01-04 14:20
Author: peno
Category: Informační technologie
Tags: aplikace, ARToolKit, augmented reality, programování, projekt, výstava
Slug: projekt-mimikry

V tomto článku bych chtěl stručně popsat projekt Mimikry, na kterém jsem
se podílel v zimním semestru 2010. Článek je upravenou částí
dokumentace, kterou jsem odevzdával v rámci školního projektu pro
předmět <abbr title="Počítačové vidění">POV</abbr>. K projektu jsem se
dostal víceméně náhodou přes mého vedoucího diplomové práce, kterého
kontaktovali studenti Akademie výtvarných umění v Praze, že by
potřebovali programátora pro svůj projekt. Další informace lze nalézt na
[stránkách studentů][].

Úvod
====

Cílem práce bylo nastudovat možnosti knihovny [ARToolKit][] a vytvořit
aplikaci pro rozšířenou realitu využívající tuto knihovnu. Výsledná
aplikace byla určena pro projekt Mimikry, který se prezentoval na
výstavě Designblok 2010. Výstava se konala 5. - 10. 10. 2010 v Praze.
Projekt jsem vypracovával samostatně ve spolupráci se studenty Akademie
výtvarných umění v Praze pod vedením Ing. Aleše Láníka.

Projekt byl experimentální. Hlavním úkolem bylo vytvořit aplikaci
rozšířené reality, která vykresluje 3D model kudlanky, mapovaný pomocí
multipatterns (více trasovacích značek) na reálný model orchideje
(plastika z tvrdého papíru o rozměrech cca 2m) a následně vytvořit
určitou interakci s tímto modelem. Účelem práce bylo živě demonstrovat
mimézi pomocí výpočetní techniky s využitím počítačového vidění. Miméze
je souborný pojem pro morfologické, fyziologické i etologické jevy,
které živočichovi umožňují skrýt se, zamaskovat nebo uniknout
pozornosti. Konkrétně se jednalo o fytomimezi, tj. napodobování rostlin
(např. pakobylky a strašilky napodobují větvičky nebo listy rostlin). V
naší performanci si divák prohlédl živý model orchideje, která se pomocí
rozšířené reality "proměnila" v maskovanou kudlanku.

Základní princip
================

V této kapitole si popíšeme, jak celý experiment funguje a co dělá.
Projekt byl předváděn v zatemněné místnosti, kde se nacházela papírová
plastika orchideje, podepřená pevným stojanem. S papírovým modelem bylo
možné otáčet zleva doprava. Na této plastice bylo nalepeno 7 trasovacích
značek ARToolKit, vytisknutých na tvrdém papíru. Bylo použito více
značek proto, aby bylo možné model prohlížet z více stran a z blízka,
protože při snímání obrazu kamerou musí být viditelná vždy minimálně
jedna značka. Značky byly rozmístěny tak, aby bylo možné prohlížet model
pomocí kamery i z velmi krátké vzdálenosti. Trasovací značky měly více
velikostí (20 cm a 15 cm).

[caption id="attachment\_223" align="alignnone" width="300"
caption="Prezentace projektu na výstavě Designblok 2010"][![Prezentace
projektu na výstavě Designblok 2010][]][][/caption]

Celá plastika byla osvícena projektorem, který promítal jednoduchou
texturu (bílá barva s růžovým nádechem). Textura měla připomínat, že se
jedná o květ orchideje. Texturu bylo potřeba vytvořit tak, aby se bílá
barva promítala přesně na celý model v místech, kde dopadá světlo
projektoru na model. Do míst, kde dopadá světlo mimo model byla
promítána černá barva. Osvícení projektorem zajistilo, že plastika byla
více výrazná a zárověň tím byly zajištěny světelné podmínky pro
rozpoznávání značek ARToolKit.

V místnosti byl dále umístěn počítač, na kterém běžela aplikace pro
rozšířenou realitu. Do počítače byla připojena webkamera Logitech
QuickCam Pro 9000 o vysokém rozlišení (1600 x 1200 px), pomocí které se
snímal obraz. Výsledný obraz rozšířené reality se promítal na velkou
plazma obrazovku umístěnou na stěně. Uprostřed místnosti byl umístěn
dřevěný podstavec, na kterém byla položena kamera, se kterou mohli
návštěvníci výstavy hýbat a vyzkoušet si tak aplikaci na vlastní kůži.

[caption id="attachment\_224" align="alignnone" width="300"
caption="Instrukce pro návštěvníka výstavy"][![Instrukce pro návštěvníka
výstavy][]][][/caption]

Aplikace rovněž umožnila určitou míru interakce uživatele s modelem. Z
větší dálky se vykreslovaly 3D modely více podobné květu orchideje. Z
blízka se potom vykreslovaly modely kudlanky s většími detaily.

[caption id="attachment\_225" align="alignnone" width="300"
caption="Papírový model květu orchideje"][![Papírový model květu
orchideje][]][][/caption]

[caption id="attachment\_226" align="alignnone" width="300" caption="3D
model kudlanky"][![3D model kudlanky][]][][/caption]

Implementace aplikace
=====================

Aplikace je implementována v jazyce C/C++, ve vývojovém prostředí
Microsoft Visual Studio 2008 s využitím knihovny [ARToolKit][]. Pro
vykreslování 3D modelů potom byly použity knihovny OpenGL a OpenVRML.

Parametry trasovacích značek (název, datový soubor, fyzické rozměry v
mm, střed značky) a seznam VRML modelů jsou uloženy v konfiguračních
souborech. Nastavení kalibrace kamery je rovněž uloženo v souboru. V
projektu byly použity standardní trasovací značky ARToolKit: patt.hiro,
patt.kanji, patt.sample1, patt.sample2, patt.a, patt.c, patt.f.

Kostra zdrojového kódu aplikace:

-   Inicializace, nastavení videokamery, zpracování konfiguračního
    souboru značek a načtení modelů VRML.
-   Hlavní smyčka:
    -   Načtení snímku z videokamery.
    -   Detekce trasovacích značek a rozpoznání vzorů.
    -   Výpočet pozice a rotace kamery vzhledem k rozpoznaným značkám.
    -   Vykreslení snímku a virtuálních objektů.
-   Ukončení snímání videokamery.

Funkce aplikace
===============

-   Rozšířená realita využívající knihovnu ARToolKit.
-   Interakce modelu s uživatelem v podobě použití LOD objektů.
-   Trasování 3D objektu pomocí multipatterns.
-   Použití 7 trasovacích značek o různých fyzických rozměrech.
-   Funkce pro snadnější výpočet transformačních matic multipatterns
    (ruční polohování objektu).
-   Využití stabilizace trasování objektu pomocí funkce historie.
-   Využití knihovny OpenVRML pro vykreslování 3D modelů.
-   Možnost vykreslování objektu z poslední známé pozice v případě
    nerozpoznání značek (použitelné pro statickou kameru).
-   Přizpůsobení prahu světelným podmínkám (ruční nastavení).
-   Debug mode zobrazující prahovaný obraz.
-   Fullscreen mode.
-   Možnost vypnutí zobrazení videa.

Příprava projektu a zkušenosti
==============================

Instalace projektu probíhala přímo na místě konání výstavy, v
Superstudiu Designbloku Bubenská 1 v Praze. Při instalaci bylo potřeba
nalepit trasovací značky na plastiku a vypočítat transformační matice,
udávající vzájemné polohy značek. Výpočet transformačních matic je
náročný, a proto byla pro jejich zjištění do aplikace implementována
funkce, která umožnila jednoduše umístit do scény 3D model kudlanky tak,
aby přesně odpovídal pozici papírového modelu. Pomocí tlačítek pro posun
a rotaci byl model umístěn přesně na místo kam patří a program vrátil
informace o pozici a rotaci modelu. Tento postup se opakoval pro všechny
trasovací značky. Tímto jsme získali transformační matice, potřebné pro
použití multipatterns.

[caption id="attachment\_227" align="alignnone" width="300"
caption="Ukázka plastiky s trasovacími značkami"][![Ukázka plastiky s
trasovacími značkami][]][][/caption]

Dále bylo během instalace nutné provést kalibraci kamery a vhodně
nastavit nasvícení plastiky projektorem.

Během práce na projektu jsme se setkali s několika problémy. Původně
bylo zamýšleno použít vlastní vzory trasovacích značek. Vlastní značky
jsme navrhli a vytiskli. Provedli jsme trénování vzorů a posléze se
ukázalo, že je nelze použít, protože je ARToolKit vzájemně zaměňuje.
Příčinou bylo to, že symboly značek byly podobné. Při detekci značek
dochází k normalizaci a změně rozlišení. ARToolKit pak detekoval dvě
podobné značky jako jednu stejnou. Dalším problémem, se kterým jsme se
setkali byla délka USB kabelu pro připojení webkamery. Nemohli jsme
použít delší prodlužovací kabel než 3m, protože u delších kabelů
docházelo k velkým ztrátám a přenos videa byl nestabilní. V projektu
jsme také chtěli použít VRML model s animací, ale kvůli velkým
hardwarovým nárokům to nebylo možné. Rovněž jsme se pokusili použít v
aplikaci 3D virtuální brýle Z800 3D Visor, ale použitá grafická karta je
nepodporovala.

Na projektu se podíleli:

-   Jan Poupě, Tadeáš Podracký, Jan Novák, Eliška Vojtková - autoři
    projektu, papírová plastika, zajištění vybavení, organizace výstavy
-   Petr Nohejl - vývoj software, pomoc s instalací
-   Michal Slyusar - 3D modely

Závěr
=====

Aplikaci se povedlo naprogramovat dle požadavků, nainstalovat pro daný
fyzický model a úspěšně prezentovat na výstavě, pro kterou byla určena.
Kvůli jistým omezením a nedostatku času pro instalaci se občas vyskytly
chyby v pozicování virtuálního modelu. Dalším problémem bylo občasné
nepochopení celého experimentu ze strany návštěvníků výstavy, a proto
bylo nutné později vytvořit informační plakát, popisující účel projektu.
Práce na experimentu byla pro mě velmi zajímavá a přínosná. Získal jsem
mnoho nových zkušenosti a seznámil se s principy rozšířené reality.
Spolupráce se studenty Akademie výtvarných umění byla rovněž velkou
zkušeností. Zajímavé byly názory lidí z ne-informatických oborů, kteří
nahlíželi na problematiku rozšířené reality z trochu jiného pohledu než
samotný programátor.

Zdrojové soubory projektu na [github.com][].

Na závěr ještě přikládám několik fotografií...

[caption id="attachment\_228" align="alignnone" width="300"
caption="Vystřihování trasovacích značek, které se stejně
nepoužily"][![Vystřihování trasovacích značek, které se stejně
nepoužily][]][][/caption]

[caption id="attachment\_229" align="alignnone" width="225"
caption="Instalace nesprávných značek"][![Instalace nesprávných
značek][]][][/caption]

[caption id="attachment\_230" align="alignnone" width="300"
caption="Testování"][![Testování][]][][/caption]

[caption id="attachment\_231" align="alignnone" width="225"
caption="Úklid a úprava ateliéru"][![Úklid a úprava
ateliéru][]][][/caption]

[caption id="attachment\_232" align="alignnone" width="300"
caption="Prezentace projektu na výstavě"][![Prezentace projektu na
výstavě][]][][/caption]

[caption id="attachment\_233" align="alignnone" width="300"
caption="Prezentace projektu na výstavě"][![Prezentace projektu na
výstavě][1]][][/caption]

[caption id="attachment\_234" align="alignnone" width="225"
caption="Plakát"][![Plakát][]][][/caption]

[caption id="attachment\_235" align="alignnone" width="300"
caption="Prezentace projektu na výstavě"][![Prezentace projektu na
výstavě][2]][][/caption]

[caption id="attachment\_236" align="alignnone" width="300"
caption="Prezentace projektu na výstavě"][![Prezentace projektu na
výstavě][3]][][/caption]

[caption id="attachment\_237" align="alignnone" width="300"
caption="Prezentace projektu na výstavě"][![Prezentace projektu na
výstavě][4]][][/caption]

  [stránkách studentů]: http://www.projectmodul.com/
  [ARToolKit]: http://blog.jestrab.net/artoolkit/
  [Prezentace projektu na výstavě Designblok 2010]: http://blog.jestrab.net/wp-content/uploads/projekt-mimikry-01-300x225.jpg
    "Prezentace projektu na výstavě Designblok 2010"
  [![Prezentace projektu na výstavě Designblok 2010][]]: http://blog.jestrab.net/wp-content/uploads/projekt-mimikry-01.jpg
    "Prezentace projektu na výstavě Designblok 2010"
  [Instrukce pro návštěvníka výstavy]: http://blog.jestrab.net/wp-content/uploads/projekt-mimikry-02-300x210.jpg
    "Instrukce pro návštěvníka výstavy"
  [![Instrukce pro návštěvníka výstavy][]]: http://blog.jestrab.net/wp-content/uploads/projekt-mimikry-02.jpg
    "Instrukce pro návštěvníka výstavy"
  [Papírový model květu orchideje]: http://blog.jestrab.net/wp-content/uploads/projekt-mimikry-03-300x300.jpg
    "Papírový model květu orchideje"
  [![Papírový model květu orchideje][]]: http://blog.jestrab.net/wp-content/uploads/projekt-mimikry-03.jpg
    "Papírový model květu orchideje"
  [3D model kudlanky]: http://blog.jestrab.net/wp-content/uploads/projekt-mimikry-04-300x300.jpg
    "3D model kudlanky"
  [![3D model kudlanky][]]: http://blog.jestrab.net/wp-content/uploads/projekt-mimikry-04.jpg
    "3D model kudlanky"
  [Ukázka plastiky s trasovacími značkami]: http://blog.jestrab.net/wp-content/uploads/projekt-mimikry-05-300x225.jpg
    "Ukázka plastiky s trasovacími značkami"
  [![Ukázka plastiky s trasovacími značkami][]]: http://blog.jestrab.net/wp-content/uploads/projekt-mimikry-05.jpg
    "Ukázka plastiky s trasovacími značkami"
  [github.com]: https://github.com/petrnohejl/Mimesis
  [Vystřihování trasovacích značek, které se stejně nepoužily]: http://blog.jestrab.net/wp-content/uploads/projekt-mimikry-06-300x225.jpg
    "Vystřihování trasovacích značek, které se stejně nepoužily"
  [![Vystřihování trasovacích značek, které se stejně nepoužily][]]: http://blog.jestrab.net/wp-content/uploads/projekt-mimikry-06.jpg
    "Vystřihování trasovacích značek, které se stejně nepoužily"
  [Instalace nesprávných značek]: http://blog.jestrab.net/wp-content/uploads/projekt-mimikry-07-225x300.jpg
    "Instalace nesprávných značek"
  [![Instalace nesprávných značek][]]: http://blog.jestrab.net/wp-content/uploads/projekt-mimikry-07.jpg
    "Instalace nesprávných značek"
  [Testování]: http://blog.jestrab.net/wp-content/uploads/projekt-mimikry-08-300x225.jpg
    "Testování"
  [![Testování][]]: http://blog.jestrab.net/wp-content/uploads/projekt-mimikry-08.jpg
    "Testování"
  [Úklid a úprava ateliéru]: http://blog.jestrab.net/wp-content/uploads/projekt-mimikry-09-225x300.jpg
    "Úklid a úprava ateliéru"
  [![Úklid a úprava ateliéru][]]: http://blog.jestrab.net/wp-content/uploads/projekt-mimikry-09.jpg
    "Úklid a úprava ateliéru"
  [Prezentace projektu na výstavě]: http://blog.jestrab.net/wp-content/uploads/projekt-mimikry-10-300x225.jpg
    "Prezentace projektu na výstavě"
  [![Prezentace projektu na výstavě][]]: http://blog.jestrab.net/wp-content/uploads/projekt-mimikry-10.jpg
    "Prezentace projektu na výstavě"
  [1]: http://blog.jestrab.net/wp-content/uploads/projekt-mimikry-11-300x225.jpg
    "Prezentace projektu na výstavě"
  [![Prezentace projektu na výstavě][1]]: http://blog.jestrab.net/wp-content/uploads/projekt-mimikry-11.jpg
    "Prezentace projektu na výstavě"
  [Plakát]: http://blog.jestrab.net/wp-content/uploads/projekt-mimikry-12-225x300.jpg
    "Plakát"
  [![Plakát][]]: http://blog.jestrab.net/wp-content/uploads/projekt-mimikry-12.jpg
    "Plakát"
  [2]: http://blog.jestrab.net/wp-content/uploads/projekt-mimikry-13-300x225.jpg
    "Prezentace projektu na výstavě"
  [![Prezentace projektu na výstavě][2]]: http://blog.jestrab.net/wp-content/uploads/projekt-mimikry-13.jpg
    "Prezentace projektu na výstavě"
  [3]: http://blog.jestrab.net/wp-content/uploads/projekt-mimikry-14-300x225.jpg
    "Prezentace projektu na výstavě"
  [![Prezentace projektu na výstavě][3]]: http://blog.jestrab.net/wp-content/uploads/projekt-mimikry-14.jpg
    "Prezentace projektu na výstavě"
  [4]: http://blog.jestrab.net/wp-content/uploads/projekt-mimikry-15-300x225.jpg
    "Prezentace projektu na výstavě"
  [![Prezentace projektu na výstavě][4]]: http://blog.jestrab.net/wp-content/uploads/projekt-mimikry-15.jpg
    "Prezentace projektu na výstavě"
