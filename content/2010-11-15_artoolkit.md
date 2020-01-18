Title: ARToolKit – rozšířená realita
Category: Informační technologie

V tomto článku bych chtěl popsat, co je ARToolKit, jak funguje, co umí,
jak se v něm programuje a jak se instaluje. Obsah článku je převzat z
mého školního projektu do předmětu
<abbr title="Grafická a zvuková rozhraní a normy">GZN</abbr>. Více o
ARToolKit se můžete dozvědět na [oficiálních stránkách projektu](http://www.hitl.washington.edu/artoolkit/).

## Úvod

ARToolKit je knihovna, která umožňuje programovat aplikace s rozšířenou
realitou (augmented reality).  Jedná se o nástroj počítačového vidění,
který snímá v reálném čase obraz pomocí videokamery a dokáže vypočítat
pozici, vzdálenost a rotaci kamery vzhledem k daným objektům, které jsou
označeny speciálními značkami (markers). Výsledkem je reálný obraz
s dokreslenou virtuální (rozšířenou) realitou ve 3D. 3D objekty se
obvykle vykreslují na trasovací značky a překrývají je. Trasovacích
značek může být ve scéně použito více.

Pro lepší představu uvedeme příklad. Na obrázku 1 níže je modrá
virtuální krychle, která stojí na skutečné papírové podložce, na které
je vytištěna speciální trasovací značka s identifikačním symbolem. Obraz
snímá v reálném čase kamera. Když uživatel posune či otočí značku,
krychle se pohne s ní. Když uživatel posune značku mimo zorný úhel
kamery, krychle zmizí.

![Obr. 1: Modrá krychle se v reálném čase vykresluje na trasovací značku ve skutečném obraze.]({static}images/artoolkit-01.jpg)

V následujícím textu se některé uvedené názvy/cesty k souborům ARToolKit
vztahují k ukázkovým příkladům pro OS Windows (Visual Basic).

## Historie

Knihovnu ARToolKit vyvinul Japonec Dr. Hirokazu Kato z Nara Institute of
Science and Technology v roce 1999. Vydána byla jako opensource
Univerzitou ve Washingtonu. Nyní je vývoj pozastaven a poslední dostupná
verze knihovny je z května 2007.

## Co ARToolKit umí?

-   rozpoznávání trasovacích značek
-   trasování pozice a rotace kamery metodami počítačového vidění
-   kalibrace kamery
-   zpracování obrazu v reálném čase
-   knihovna zajišťující zpracování videa
-   ARToolKit je napsán v jazyce C/C++
-   podpora OpenGL, GLUT a VRML (OpenVRML) pro vykreslování virtuálního
    obrazu
-   podpora více OS (Linux, MS Windows, Mac OS X) a mobilních platforem
    (Android, Symbian, iPhone)
-   podpora 3D virtuálních brýlí
-   řada nástrojů a příkladů
-   mnoho mutací (pro Flash, Silverlight, Virtual machines,
    OpenSceneGraph atd.)

## Jak ARToolKit funguje?

### Základní princip

Hlavním problémem při vývoji aplikací s rozšířenou realitou je správně
najít a trasovat zorný úhel pozorovatele (videokamery).  Aplikace
potřebuje znát přesnou pozici videokamery vůči značkám, aby byla schopna
určit zorný bod, ze kterého se bude vykreslovat virtuální obraz. Jakmile
je známa pozice videokamery, která se vypočte podle polohy a natočení
značek, virtuální kamera může být umístěna do stejného bodu jako ta
reálná a poté je možno vykreslit 3D modely přesně na místa značek.
ARToolKit používá pro trasování pozice kamery algoritmy počítačového
vidění, které jsou schopny počítat rychle v reálném čase. Výsledky jsou
však závislé na použitém hardware a videokameře.

### Fáze zpracování obrazu v reálném čase

1.  Videokamera sejme snímek a pošle jej počítači ke zpracování.
2.  Program v počítači zpracuje snímek z videa, převede jej pomocí
    prahování na černo-bílý obraz a najde v něm všechny černé
    čtverhranné tvary, které odpovídají vzorům trasovacích značek.
3.  Pokud jsou nějaké značky detekovány, program vypočítá pozici a
    rotaci kamery vůči trasovacím značkám.
4.  Jakmile je známa poloha kamery, virtuální 3D grafika může být
    vykreslena ze stejné pozice.
5.  Virtuální grafika je vykreslena přes reálný snímek z videokamery a
    objekty se zobrazí přesně na místa trasovacích značek.

![Obr. 2: Fáze zpracování obrazu ARToolKit v reálném čase.]({static}images/artoolkit-02.jpg)

### Omezení

ARToolKit má určitá omezení, které je potřeba při vývoji aplikací
s rozšířenou realitou brát v úvahu.

-   Virtuální objekty se objeví pouze tehdy, kdy jsou příslušné
    trasovací značky plně viditelné ze strany pozorovatele
    (videokamery). Pokud je část značky zakryta, nelze ji rozpoznat.
-   Správná detekce trasovacích značek ve videu je závislá na světelných
    podmínkách ve scéně. Při špatném osvětlení nemusí být značky
    v prahovaném obraze detekovány. Rušit mohou i odlesky světla na
    značkách. Problémy se světlem lze částečně redukovat nastavením
    vhodného prahu.
-   Správná detekce značek je rovněž závislá na naklonění značek vůči
    pozorovateli (videokameře). Čím více je značka nakloněna, tím hůře
    se rozpoznává.
-   Při tvorbě vlastních značek je důležité zvolit vhodné symboly.
    Platí, že čím jednodušší, tím lepší a tím snadněji se správně
    rozpozná. Nejvhodnější jsou značky s velkými černými a bílými místy
    (s nízkou frekvencí). Komplexnější vzory jsou z větší dálky hůře
    detekovány a můžou zkrátit rozlišovací vzdálenost až o polovinu.
    V tabulce 1 jsou znázorněny přibližné rozlišovací vzdálenosti
    trasovacích značek, které byly experimentálně zjištěny.

<table cellspacing="0" cellpadding="0">
    <tbody>
        <tr>
            <td width="206" valign="top">Velikost značky [cm]</td>
            <td width="212" valign="top">Max. použitelná vzdálenost [cm]</td>
        </tr>
        <tr>
            <td width="206" valign="top">7.0</td>
            <td width="212" valign="top">40.6</td>
        </tr>
        <tr>
            <td width="206" valign="top">8.9</td>
            <td width="212" valign="top">63.5</td>
        </tr>
        <tr>
            <td width="206" valign="top">10.8</td>
            <td width="212" valign="top">86.4</td>
        </tr>
        <tr>
            <td width="206" valign="top">18.7</td>
            <td width="212" valign="top">127</td>
        </tr>
    </tbody>
</table>

Tabulka 1: Rozlišovací vzdálenost trasovacích značek o různé velikosti.

### Kalibrace kamery

Nastavení a parametry videokamery jsou uloženy v binárním souboru
camera\_para.dat (v adresáři bin/Data). Konfigurace kamery se zpracuje
při každém spuštění aplikace ARToolKit.

ARToolKit používá implicitně soubor camera\_para.dat s výchozím
nastavením. Rovněž však umožňuje kalibraci jakékoliv kamery a vytvoření
vlastního konfiguračního souboru. To je vhodné zejména pro kamery s
atypickými objektivy (např. rybí oko). Kalibrace zajistí přesnější
výpočty polohy videokamery pro vykreslení virtuální scény a redukuje
zkreslení. Pro správné provedení kalibrace bude potřeba vytisknout vzory
calib\_dist a calib\_cpara (z adresáře patterns), s kterými budeme
pracovat podobně jako se značkami. K dispozici jsou dva kalibrační
postupy.

-   Dvoukroková kalibrace - složitější použití, ale lepší výsledky.
    Vhodnější pro 3D měření.
-   Jednokroková kalibrace - jednodušší použití, méně přesná.

### Přesnost trasování objektů

ARToolKit umí stabilizovat trasování objektů pomocí funkce historie.
Tato stabilizace redukuje chvění virtuálních objektů, protože při
výpočtu polohy objektu se využívá průměr několika předchozích poloh.
Tímto je zajištěna větší stabilita, ale horší přesnost. Historii lze
použít rovněž i při detekci značek. Výpočet je potom o něco rychlejší a
stabilnější, ale opět méně přesný.

## Trasovací značky

### Metody trasování

Trasovací značky jsou speciální vzory, obvykle vytištěné na papíru,
pomocí kterých se trasují virtuální objekty rozšířené reality. Je to
jedna z metod, jak lze trasovat vrstvu rozšířené reality. Tato metoda
využívá počítačové vidění. Další možnou metodou trasování můžou být
např. polohovací senzory (GPS, kompas, akcelerometr), které jsou
dostupné zpravidla na moderních mobilních zařízeních.

### Podoba trasovacích značek

Z polohy značek ve video obrazu se vypočítává pozice a rotace kamery.
Značky v ARToolKit mají čtvercový tvar. Tvoří je černobílý symbol s
černým okrajem o šířce, která je rovna polovině šířky vnitřní plochy se
symbolem. Vnitřní symbol je černý na bílém podkladu a slouží k rozlišení
více různých značek od sebe. Měl by být co nejjednodušší (viz kapitola
4.3) a nesmí být středově souměrný, aby bylo možné rozlišit orientaci
(natočení) značky ve scéně. Tedy např. značka s kruhem uprostřed je
nevhodná. Pokud používáme více značek v aplikaci s rozšířenou realitou,
tyto značky by neměly být vzájemně podobné, aby nedošlo k záměně. Značky
je vhodné tisknout na tvrdý, nelesknoucí se papír a případně podlepit
kartonem, aby se neohýbaly. Je potřeba zvolit vhodnou velikost značky
podle použití. Na obrázku 3 jsou ukázány příklady trasovacích značek,
které lze rovněž najít v adresáři patterns ve formátu PDF k vytisknutí.

![Obr. 3: Ukázky trasovacích značek ARToolKit.]({static}images/artoolkit-03.jpg)

### Konfigurační soubor

Seznam použitých značek je obvykle uložen v konfiguračním souboru
object\_data (v adresáři bin/Data), který se načítá při inicializaci
aplikace ARToolKit.  V souboru je uložen počet použitých značek a ke
každé značce její pojmenování, datový soubor, šířka značky na vytištěném
papíru v milimetrech (včetně okrajů) a její střed.

### Tvorba vlastních značek

ARToolKit umožňuje tvorbu vlastních značek pomocí nástroje mk\_patt.
Tento program umožňuje vygenerovat datový soubor značky z natrénovaných
dat z videokamery. Než spustíme trénování, je potřeba vhodně navrhnout
symbol naší nové značky a následně značku vytisknout. Pro tvorbu značek
lze použít šablonu, uloženou v souboru patterns/blankPatt.gif. Nakonec
je potřeba vytvořit příslušný konfigurační soubor k vytvořeným značkám.

### Trasování pomocí více značek

ARToolKit umožňuje trasování jednoho objektu pomocí více značek. Pomocí
sady několika značek s vzájemně neměnnou pozicí (např. značky nalepené
na pevné podložce) lze určit jedinou polohu. To lze využít v případě,
kdy některá značka je mimo zorný úhel pozorovatele (videokamery).
V běžném případě by objekt zmizel, ale pomocí multi značek lze pozici
dopočítat. Pokud je viditelná alespoň jedna značka z dané sady,
ARToolKit dokáže dopočítat pozici zbylých značek, které jsou mimo zorný
úhel. Sadu multi značek je potřeba nadefinovat v konfiguračním souboru
marker.dat (v adresáři bin/Data/multi), obdobně jako běžné značky. Navíc
je potřeba pro každou značku nastavit transformační matici, udávající
přesnou polohu v souřadnicovém systému. Správné nastavení transformační
matice může být v některých případech velmi obtížné.

## Vývoj aplikací v ARToolKit

### ARToolKit framework

ARToolKit poskytuje funkce, které se volají v určitém pořadí a tvoří tak
program s rozšířenou realitou. Některé funkce je však možné používat
samostatně. ARToolKit je multiplatformní, pro renderování virtuální
vrstvy používá OpenGL a pro správu událostí a oken používá GLUT. API je
napsáno v jazyce C.

ARToolKit tvoří tři hlavní moduly:

-   AR modul - jádro systému, zajišťující trasování značek a zpracování
    parametrů kamery.
-   Video modul - zajišťuje snímání video obrazu.
-   Gsub modul - funkce zajišťující vykreslování 3D grafiky.

![Obr. 4: Architektura ARToolKit.]({static}images/artoolkit-04.jpg)

### Formát obrazových dat

Jednotlivé moduly ARToolKit používají odlišné formáty obrazových dat.

![Obr. 5: Formát dat při zpracování obrazu v ARToolKit.]({static}images/artoolkit-05.jpg)

### Kostra zdrojového kódu aplikace

1.  Inicializace - inicializace a nastavení videokamery, zpracování
    konfiguračního souboru značek.
2.  Hlavní smyčka:
    1.  Načtení snímku z videokamery.
    2.  Detekce trasovacích značek a rozpoznání vzorů ve snímku.
    3.  Výpočet pozice a rotace kamery vzhledem k rozpoznaným značkám.
    4.  Vykreslení snímku a virtuálních objektů.

3.  Ukončení - ukončení snímání videokamery a vypnutí programu.

## Instalace ARToolKit pro Visual Studio

### Prerekvizity

-   Vývojové prostředí Microsoft Visual Studio, případně Cygwin.
-   Knihovna DSVideoLib, zajišťující komunikaci s ovladači videokamery
    (DSVideoLib je součástí instalačního balíčku ARToolKit).
-   GLUT (OpenGL Utility Toolkit) runtime a SDK.
-   DirectX 9.0b nebo novější.
-   Videokamera nebo webkamera, podporující rozhraní USB nebo Firewire.
-   OpenVRML knihovna (je součástí instalačního balíčku ARToolKit).

### Instalace

1.  Stáhneme instalační balíček z oficiálního webu
    <http://www.hitl.washington.edu/artoolkit/>, případně balíček
    ARToolKit-2.7.1-bin-book.zip z adresy
    <http://books.ascii.jp/9784048673617/>, kde jsou opraveny některé
    zdrojové kódy, které v původní verzi způsobovaly chyby při kompilaci
    programů, pracujících s OpenVRML.
2.  Rozbalíme instalační balíček do adresáře [ARToolKit].
3.  Rozbalíme knihovnu DSVideoLib do adresáře „DSVL“ v [ARToolKit].
4.  Zkopírujeme soubory DSVL.dll a DSVLd.dll z adresáře
    [ARToolKit]\\DSVL\\bin do [ARToolKit]\\bin.
5.  Nainstalujeme knihovny GLUT. Dll soubory zkopírujeme do systémové
    složky Windows „System32“. Knihovny a hlavičkové soubory umístíme do
    SDK adresáře Visual Studia.
6.  Spustíme skript [ARToolKit]\\Configure.win32.bat, který vytvoří
    soubor include\\AR\\config.h.
7.  Otevřeme ARToolKit.sln ve Visual Studiu a sestavíme solution
    příkazem Build.
8.  Pro zprovoznění OpenVRML rozbalíme tento balíček do adresáře
    [ARToolKit].
9.  Zkopírujeme soubor js32.dll z adresáře [ARToolKit]\\OpenVRML\\bin do
    [ARToolKit]\\bin.
10. V konfiguračním manažeru Visual Studia povolíme projekty libARvrml a
    simpleVRML a znovu sestavíme příkazem Build.

### Struktura ARToolKit

ARToolKit obsahuje následující adresáře:

-   bin - nástroje, příklady, kalibrační soubory videokamery,
    konfigurační soubory značek a multi-značek, VRML modely a jejich
    konfigurační soubory, spustitelné programy končící sufixem „d“ jsou
    určeny pro ladění (debug)
-   doc - dokumentace
-   DSVL - soubory knihovny DSVideoLib
-   examples - zdrojové soubory ukázkových aplikací
-   include - hlavičkové soubory ARToolKit
-   lib - knihovny a zdrojové kódy ARToolKit
-   OpenVRML - soubory knihovny OpenVRML
-   patterns - trasovací značky v PDF k vytisknutí
-   util - zdrojové soubory nástrojů

### Testovací a ukázkové aplikace

Po úspěšném sestavení solution bychom měli vyzkoušet testovací aplikace
(v adresáři bin) a ověřit, zda vše správně funguje. Nejdříve bychom měli
vyzkoušet grafický test graphicsTest, kterým ověříme správnou funkčnost
OpenGL a GLUT. Na obrazovce by se měla po spuštění programu objevit
modrá rotující konvička. Dále vyzkoušíme video test videoTest, kterým
ověříme správnou funkčnost videokamery a zobrazování video výstupu na
displeji. Na obrazovce by se mělo objevit okno s nastavením konfigurace
kamery (podobně jako na obrázku 6) a po potvrzení a zvolení správného
nastavení obraz z videokamery. Pokud oba tyto testy fungují správně,
máte potvrzeno, že vaše kamera podporuje grafický modul a video modul
ARToolKit.

![Obr. 6: Nastavení konfigurace videokamery.]({static}images/artoolkit-06.jpg)

Pro spuštění ukázkových aplikací ARToolKit je potřeba mít k dispozici
vytisknuté trasovací značky (z adresáře patterns). Některé ukázkové
aplikace mají implementovaný debug mode, který se zapíná/vypíná
tlačítkem „d“ a zobrazuje prahovaný obraz. U některých aplikací lze
nastavit manuálně hodnotu prahu pomocí tlačítka „t“. Zdrojové kódy
ukázkových aplikací nalezneme v adresáři examples.

## Příklady využití

-   zábava, hry
-   interaktivní průvodce v muzeu
-   navigace v budově
-   efekty ve filmu
-   reklama na plakátu

## Zdroje

[1] OsgART [online]. 2009 [cit. 2010-11-04]. OsgART: Augmented Reality
for OpenSceneGraph. Dostupné z WWW:
http://osgart.org/wiki/File:Build\_artoolkit\_simpletest.jpg.

[2] ARToolKit [online]. 2007 [cit. 2010-11-04]. ARToolKit
Documentation - How does ARToolKit work. Dostupné z WWW:
http://www.hitl.washington.edu/artoolkit/documentation/images/diagram.jpg.

[3] ARToolKit [online]. 2007 [cit. 2010-11-04]. ARToolKit
Documentation - ARToolKit framework. Dostupné z WWW:
http://www.hitl.washington.edu/artoolkit/documentation/images/artarchitecture.jpg.

[4] ARToolKit [online]. 2007 [cit. 2010-11-04]. ARToolKit
Documentation - ARToolKit framework. Dostupné z WWW:
http://www.hitl.washington.edu/artoolkit/documentation/images/formatpipeline.jpg.

[5] ARToolKit [online]. 2007 [cit. 2010-11-04]. ARToolKit
Documentation - First example. Dostupné z WWW:
http://www.hitl.washington.edu/artoolkit/documentation/images/configCamWindows.jpg.

[6] ARToolKit [online]. 2007 [cit. 2010-11-04]. Dostupné z WWW:
http://www.hitl.washington.edu/artoolkit/.

[7] ARToolKit. In Wikipedia : the free encyclopedia [online]. St.
Petersburg (Florida) : Wikipedia Foundation, 16.1.2008, last modified on
11.6.2010 [cit. 2010-11-04]. Dostupné z WWW:
http://en.wikipedia.org/wiki/ARToolKit.

[8] KATO, Hirokazu. Inside ARToolKit [online]. Japan : Hiroshima City
University, 2002 [cit. 2010-11-04]. Dostupné z WWW:
http://www.hitl.washington.edu/artoolkit/Papers/ART02-Tutorial.pdf.

[9] KATO, Hirokazu; BILLINGHURST, Mark. Marker Tracking and HMD
Calibration for a Video-based Augmented Reality Conferencing System
[online]. Hiroshima City University and University of Washington :
Faculty of Information Sciences and Human Interface Technology
Laboratory, 1999 [cit. 2010-11-04]. Dostupné z WWW:
http://www.hitl.washington.edu/artoolkit/Papers/IWAR99.kato.pdf.

[10] ARToolworks support library [online]. 2010 [cit. 2010-11-04].
ARToolKit Professional. Dostupné z WWW:
http://www.artoolworks.com/support/library/ARToolKit\_Professional.
