Title: Instalace Windows XP z USB flash (Acer Aspire One)
Date: 2010-09-14 20:28
Author: peno
Category: Informační technologie
Tags: tutoriál, Windows
Slug: instalace-windows-xp-z-usb-flash-acer-aspire-one

V tomto tutoriálu bych chtěl popsat, jak úspěšně nainstalovat OS Windows
XP na netbook Acer Aspire One pomocí USB flashky. Návod by měl však bez
problému fungovat pro všechny počítače obecně.

Před pár dny jsem potřeboval přeinstalovat operační systém Windows XP,
protože systém byl naposled instalován před dvěma roky a byl tak
zahlcený a pomalý, že už na něm nešlo dál pracovat. Konkrétně šlo o
netbook Acer Aspire One. Problém tkví v tom, že tento netbook nemá
CD-ROM mechaniku. Nabízí se nám tedy otázka: "Jak operační systém
Windows XP nainstalovat, když nemůžu použít CD?" Nejsnadnější možný
způsob je pomocí USB flash klíčenky / disku.

Na internetu jsem prošel mnoho tutoriálů, ale vždycky se našel nějaký
problém. Vyzkoušel jsem aplikace PeToUSB a USB\_MultiBoot, ale ani jedna
mi nefungovala. Program vracel nepochopitelné errory ("E: has NOT FAT
FAT32 or NTFS Format and is NOT Valid"), ačkoliv byla flashka
zformátována do FAT32 a měla velikost 1 GB (systém souborů FAT32
nepodporuje soubory větší než 4 GiB). Nakonec jsem narazil v jedné
[diskuzi][]na velmi jednoduché a funkční řešení.

#### Zde je postup:

1.  K přípravě instalačního USB disku budeme potřebovat jakýkoliv
    počítač s OS Windows (libovolné verze) a CD-ROM mechanikou (tu však
    lze emulovat virtuální mechanikou, viz níže). Připravíme si USB
    flash disk s minimální kapacitou 1 GB a zformátujeme jej do systému
    souborů FAT32 nebo NTFS. Pozor! Při formátu ztratíte všechna vaše
    data na USB disku!
2.  Připravíme si instalační CD OS Windows XP, případně můžeme použít
    virtuální mechaniku např. pomocí [Daemon Tools][] a načíst CD z ISO
    souboru.
3.  Stáhneme si z internetu program WinSetupFromUSB a spustíme jej. V
    sekci "USB disk selection" vybereme náš flash disk. V sekci "Add to
    USB disk" zaškrtneme volbu Windows XP a vybereme CD-ROM jednotku, ve
    které máme instalační CD Windows XP. Nakonec stačí stisknout
    tlačítko "GO" a čekat, než se připraví instalační USB flash disk a
    zkopírují se všechny soubory z CD. Ovládání programu WinSetupFromUSB
    se může v různých verzích lišit, ale princip je stejný.
4.  Pokud máme vše nachystané, zálohované a jsme připraveni
    přeinstalovat systém, vložíme USB disk do počítače, který hodláme
    přeinstalovat a restartujeme počítač. Při startování počítače
    stiskneme tlačítko F2 pro nastavení BIOSu a v něm nastavíme primárně
    bootování z USB. Případně stiskneme tlačítko F12 a vybereme možnost
    bootování z USB. Měla by se nám zobrazit bootovací obrazovka
    GRUB4DOS.
5.  Nyní vybereme možnost "First Part of installation" a potvrdíme. Mělo
    by se zobrazit standardní modré instalační okno Windows XP. Dále
    postupujeme jako při běžné instalaci a řídíme se pokyny na
    obrazovce. Po prvním restartu vybereme v GRUB4DOS možnost "2nd Part
    of installation" a pokračujeme v instalaci standardním způsobem.
6.  Po úspěšném nainstalování systému provedeme update a nainstalujeme
    [ovladače, které lze stáhnout na stránkách Acer][].
7.  Nyní bychom měli mít nainstalován funkční systém Windows XP.
    Instalační USB disk si můžeme uschovat pro pozdější možnou
    reinstalaci.

[caption id="attachment\_202" align="alignnone" width="229"
caption="WinSetupFromUSB"][![WinSetupFromUSB][]][][/caption]

Budu rád, když někomu tento návod pomůže. Případné dotazy rád zodpovím v
diskuzi.

  [diskuzi]: http://duncsweb.com/2009/07/17/e-has-not-fat-fat32-or-ntfs-format-and-is-not-valid/
  [Daemon Tools]: http://www.daemon-tools.cc
  [ovladače, které lze stáhnout na stránkách Acer]: http://support.acer-euro.com/drivers/notebook/as_one_150.html
  [WinSetupFromUSB]: http://blog.jestrab.net/wp-content/uploads/instalace-windows-xp-z-usb-flash-acer-aspire-one-229x300.jpg
    "WinSetupFromUSB"
  [![WinSetupFromUSB][]]: http://blog.jestrab.net/wp-content/uploads/instalace-windows-xp-z-usb-flash-acer-aspire-one.jpg
    "WinSetupFromUSB"
