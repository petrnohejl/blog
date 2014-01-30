Title: Apache a mod_python pro webový framework Django
Date: 2011-02-09 00:06
Author: peno
Category: Informační technologie
Tags: Django, projekt, Python, tutoriál, webdesign
Slug: apache-a-mod_python-pro-webovy-framework-django

Tento tutoriál stručně popisuje postup, jak nainstalovat, nastavit a
zprovoznit webový server Apache 2.2 s modulem mod\_python na systému
GNU/Linux Ubuntu 9.10. Dále popisuje postup, jak nainstalovat databázi
MySQL, webový framework Django a zprovoznit je na webovém serveru
Apache. Na závěr je ukázán příklad vytvoření nového Django projektu a
spuštění na serveru Apache. Tutoriál byl napsán v rámci 2. projektu do
předmětu
<abbr title="Přenos dat, počítačové sítě a protokoly">PDS</abbr>, který
jsem absolvoval v letním semestru 2010.

Úvod
====

[Apache HTTP Server][] je nejrozšířenější softwarový webový server s
otevřeným kódem pro GNU/Linux, BSD, Solaris, Mac OS X, Microsoft Windows
a další platformy. V současné době dodává prohlížečům na celém světě
většinu internetových stránek. Výhody Apache: výkon a spolehlivost,
široké možnosti, open source. [1]

[Mod\_python][] je modul pro webový server Apache, který na serveru
umožňuje spouštění skriptů, napsaných v jazyce Python.

[Django][] je vyspělý webový framework napsaný v jazyce Python, který
podporuje rychlý vývoj a čisté, pragmatické konstrukce.

Instalace Apache
================

Instalaci serveru Apache 2.2 provedeme spuštěním připraveného dávkového
skriptu *install\_apache.sh*. Skript byl napsán pro operační systém
GNU/Linux Ubuntu 9.10 a na jiných systémech není zaručena jeho
funkčnost. Všechny skripty a příkazy je potřeba spouštět jako admin
(příkazem sudo). Pro správnou instalaci je nutné mít na disku dostatek
místa (minimálně 50 MB). Dále je potřeba mít správně nainstalován ANSI-C
kompilátor, nástroj make a další potřebné utility, používané
v instalačním skriptu.

``` {lang="bash"}
#! /bin/bash
#skript: install_apache.sh
#popis: davkovy skript pro instalaci serveru Apache na OS GNU/Linux Ubuntu 9.10
#autor: Petr Nohejl (xnohej00)

#promenne
MIRROR=http://ftp.sh.cvut.cz/MIRRORS/apache/httpd/httpd-2.2.15.tar.gz
VERSION=httpd-2.2.15
TEMP=APACHE_INSTALL #pozor, tento adresar se nakonci skriptu maze!

cd
sudo mkdir $TEMP
cd $TEMP
sudo wget $MIRROR
sudo gzip -d $VERSION.tar.gz
sudo tar xvf $VERSION.tar
cd $VERSION
./configure --prefix=/usr/local/apache2 --enable-rewrite=shared --enable-speling=shared --with-mpm=prefork
sudo make
sudo make install
cd
sudo rm -rf $TEMP
```

Skript nejdříve vytvoří pracovní adresář a do něj stáhne (z internetu)
pomocí nástroje *wget* zkomprimovaný instalační balíček. Ten rozbalí
pomocí nástrojů *gzip* a *tar*. Dále spustí konfigurační skript
*configure*, který připraví projekt ke kompilaci a vytvoří soubor
*Makefile*. Konfigurace trvá delší dobu, a proto je třeba být trpělivý.
Dále se projekt zkompiluje pomocí příkazu *make* a nainstaluje pomocí
příkazu *make install*. Tyto operace rovněž trvají delší čas. Nakonec
skript vymaže pracovní adresář. Pokud chcete mít nad vším vlastní
kontrolu, je lepší instalovat server ručně (bez použití dávkového
skriptu) a řídit se postupem, popsaným výše.

Při spouštění konfiguračního skriptu máme možnost nastavit mnoho
parametrů. Pomocí přepínače *--prefix* nastavíme adresář, kam bude
server nainstalován. Pomocí přepínače *--enable* můžeme nainstalovat
volitelné moduly. Příznak *shared* značí, že modul je dynamicky sdílený
(DSO). Pokud nainstalujeme nějaký modul s příznakem *shared*,
automaticky se zapne podpora DSO (jinak ji musíme v případě potřeby
explicitně zapnout příkazem *--enable-so* při konfiguraci). Přepínač
*--with-mpm* nastavuje model procesů serveru. Parametrů existuje daleko
více. Pro více informací o instalaci Apache navštivte dokumentaci:
<http://httpd.apache.org/docs/2.2/install.html>.

Konfigurace Apache
==================

Po úspěšné instalaci je potřeba Apache správně nakonfigurovat.
Konfigurační soubor s nastavením serveru se nachází v adresáři
/usr/local/apache2/conf/httpd.conf. Soubor otevřeme v libovolném
textovém editoru:

``` {lang="bash"}
sudo gedit /usr/local/apache2/conf/httpd.conf
```

Nastavíme proměnnou *Listen* (na jakém portu a IP se bude naslouchat),
odkomentujeme řádek se *ServerName*a nastavíme název serveru, nastavíme
proměnnou DocumentRoot (kořenový adresář webových dokumentů). Dále
můžeme nastavovat i další parametry serveru. Pro více informací o
konfiguraci serveru navštivte dokumentaci:
<http://httpd.apache.org/docs/2.2/mod/directives.html>. Příklad změn v
konfiguračním souboru pro základní nastavení:

``` {lang="bash"}
Listen 127.0.0.1:666
ServerName www.example.com:80
DocumentRoot "/usr/local/apache2/htdocs"
```

Po každé změně konfiguračního souboru je nutné server restartovat.

Spuštění serveru
================

Pokud jsme server správně nainstalovali a nakonfigurovali, můžeme jej
spustit a otestovat správnou funkčnost:

``` {lang="bash"}
sudo /usr/local/apache2/bin/apachectl –k start
firefox http://127.0.0.1:666/
sudo /usr/local/apache2/bin/apachectl –k restart
sudo /usr/local/apache2/bin/apachectl –k stop
```

Pokud je vše v pořádku, měl by se nám v prohlížeči vypsat nápis "It
works!".

[caption id="attachment\_253" align="alignnone" width="300"
caption="Spuštění serveru Apache"][![Spuštění serveru
Apache][]][][/caption]

Instalace a konfigurace mod\_python
===================================

Nyní nainstalujeme pro Apache modul mod\_python. Před vlastní instalací
modulu je potřeba mít správně nainstalován Python (minimálně verzi 2.3),
balíček Python dev a samozřejmě Apache. Mod\_python vyžaduje podporu DSO
(Dynamic Shared Object), kterou lze nastavit při instalaci (konfiguraci)
Apache. Instalaci mod\_python můžeme provést buď pomocí utility
*apt-get*, nebo si můžeme modul stáhnout z internetu, sestavit a
nainstalovat. Druhá možnost je poněkud komplikovaná a proto zvolíme
jednodušší cestu s pomocí *apt-get*, která udělá vše potřebné za nás.

``` {lang="bash"}
sudo apt-get install libapache2-mod-python
```

Po úspěšné instalaci modulu budeme muset opět upravit konfigurační
soubor serveru:

``` {lang="bash"}
sudo gedit /usr/local/apache2/conf/httpd.conf
```

Přidáme příkaz *LoadModule* na správné místo v souboru (viz komentáře
v konfiguračním souboru) pro načtení modulu a poté přidáme další příkazy
pro nastavení handleru pro následné testování serveru (např. na konec
konfiguračního souboru). Nezapomeneme provést restart serveru, aby se
znovu načetl konfigurační soubor.

``` {lang="apache"}
LoadModule python_module /usr/lib/apache2/modules/mod_python.so


    SetHandler mod_python
    PythonHandler mod_python.testhandler


 
    AddHandler mod_python .py
    PythonHandler mptest 
    PythonDebug On 
```

Nyní můžeme vyzkoušet ladící výpis serveru:

``` {lang="bash"}
firefox http://127.0.0.1:666/mpinfo
```

Pokud je vše v pořádku, měl by se nám v prohlížeči vypsat ladící výpis.

[caption id="attachment\_254" align="alignnone" width="300"
caption="Ladící výpis mod\_python"][![Ladící výpis
mod\_python][]][][/caption]

Dále si vytvoříme testovací skript *mptest.py* v jazyce Python:

``` {lang="bash"}
sudo mkdir /usr/local/apache2/htdocs/test
sudo gedit /usr/local/apache2/htdocs/test/mptest.py
```

Do skriptu *mptest.py* uložíme následující kód:

``` {lang="python"}
from mod_python import apache
def handler(req):
    req.content_type = 'text/plain'
    req.write("Hello World! I am Python.")
    return apache.OK
```

A nakonec spustíme testovací skript:

``` {lang="bash"}
firefox http://127.0.0.1:666/test/mptest.py
```

Pokud je vše v pořádku, měl by se nám v prohlížeči vypsat nápis "Hello
World! I am Python.".

[caption id="attachment\_256" align="alignnone" width="300"
caption="Hello Python"][![Hello Python][]][][/caption]

Základní konfigurace Publisher Handler
======================================

Publisher Handler je standardní mod\_python handler pro zobrazování
webových stránek. V předchozí kapitole jsme si v konfiguračním souboru
Apache nastavili jednoduchý handler, který odchytává URL končící na
*.py* ve složce *test*a spouští skript (handler) *mptest.py*. Pokud
chceme mít více handlerů, použijeme pokročilejší handler Publisher.
V konfiguračním souboru Apache nastavíme (předešlý handler z předchozí
kapitoly zakomentujeme):

``` {lang="apache"}
 
    AddHandler mod_python .py
    PythonHandler mod_python.publisher 
    PythonDebug On 
```

Restartujeme server pro znovunačtení konfigurace. Dále si vytvoříme
jednoduchou dynamickou webovou stránku v Pythonu (jednoduchá
kalkulačka). Vytvoříme si novou složku a dva zdrojové soubory:

``` {lang="bash"}
sudo mkdir /usr/local/apache2/htdocs/form
sudo gedit /usr/local/apache2/htdocs/form/index.html
sudo gedit /usr/local/apache2/htdocs/form/form.py
```

Do souboru *index.html* uložíme následující kód:

``` {lang="html4strict"}
    
    Calculator    
    Enter two numbers:                  
    
         + 
         =
        
    
```

Do skriptu *form.py* uložíme následující kód:

``` {lang="python"}
def msg(req, num1, num2):
    # make sure the user provided all the parameters
    if not(num1 and num2): return "ResultMissing some parametre!"
    # provide feedback to the user
    try: result = int(num1) + int(num2)
    except: return "ResultInvalid parametres!"    
    return "Result" + str(result) + ""
```

Nakonec zobrazíme web v prohlížeči:

``` {lang="bash"}
firefox http://127.0.0.1:666/form/
```

Pokud je vše v pořádku, měl by se nám v prohlížeči zobrazit formulář s
nadpisem "Calculator".

[caption id="attachment\_255" align="alignnone" width="300"
caption="Calculator"][![Calculator][]][][/caption]

Pro více informací o konfiguraci mod\_python navštivte dokumentaci:
<http://www.modpython.org/live/current/doc-html/modpython.html>.

Instalace MySQL serveru
=======================

Pro práci s webovým frameworkem Django budeme potřebovat databázi.
Nainstalujeme MySQL server pomocí nástroje *apt-get*a podporu MySQL pro
Python. Alternativně můžeme použít jiné databáze (např. SQLite).

``` {lang="bash"}
sudo apt-get install mysql-server python-mysqldb
```

Instalace frameworku Django a vytvoření projektu
================================================

Pro instalaci budeme potřebovat program SVN. Ten můžeme případně
nainstalovat pomocí programu *apt-get*.

``` {lang="bash"}
sudo apt-get install subversion
```

Nainstalujeme vývojovou verzi Djanga z SVN repozitáře:

``` {lang="bash"}
cd
svn co http://code.djangoproject.com/svn/django/trunk/ django_src
```

Nyní vytvoříme symbolický odkaz na Django, aby jej systém mohl najít a
mohl s ním pracovat. Nejprve si zjistíme, kde se nachází adresář
*site-packages*, a potom vyvoříme samotný odkaz (místo "YOUR-DIR"
doplňte řetězec z předchozího příkazu *python -c*):

``` {lang="bash"}
python -c "from distutils.sysconfig import get_python_lib; print get_python_lib()"
sudo ln -s `pwd`/django_src/django YOUR-DIR/django
sudo cp ~/django_src/django/bin/django-admin.py /usr/local/bin
```

Dále si vytvoříme několik adresářů, které bude Django používat:

``` {lang="bash"}
cd
mkdir django_projects
mkdir django_templates
mkdir media
```

Poté vytvoříme symbolické odkazy na media (css, javascript atd.):

``` {lang="bash"}
cd /usr/local/apache2/htdocs
sudo ln -s  ~/media media
sudo ln -s ~/django_src/django/contrib/admin/media admin_media
```

Nyní už můžeme vytvořit nový Django projekt standardním způsobem
(postup, jak vytvořit Django projekt není součástí tohoto tutoriálu).

``` {lang="bash"}
cd ~/django_projects
django-admin.py startproject mysite
```

Django vyzkoušíme na projektu *Mysite*, který zobrazuje ankety *Polls*.
Projekt najdete v tutoriálu na oficiálních stránkách Djanga:
<http://docs.djangoproject.com/en/dev/intro/tutorial01/>. Uložíme jej do
složky *django\_projects*a následně vyzkoušíme, zda jej Apache zobrazí.
Pokud v Django projektu používáme SQLite (jako v našem ukázkovém
projektu *Mysite*), musíme povolit zápis do souboru. V nastavení Django
projektu *settings.py* nezapomeneme správně nastavit připojení k
databázi (případně cestu k sqlite), proměnnou *TEMPLATE\_DIRS* a media
(místo "USER-NAME" doplňte vaše systémové uživatelské jméno).

``` {lang="python"}
DATABASE_NAME = '/home/USER-NAME/django_projects/mysite/sqlite3.db'
MEDIA_ROOT = '/media/'
ADMIN_MEDIA_PREFIX = '/admin_media/'
TEMPLATE_DIRS = ( '/home/USER-NAME/django_projects/mysite/mytemplates' )
```

Upravíme konfigurační soubor serveru a nastavíme handler pro Django
(předešlý handler z předchozí kapitoly zakomentujeme, místo "USER-NAME"
doplňte vaše systémové uživatelské jméno):

``` {lang="apache"}
    SetHandler python-program
    PythonHandler django.core.handlers.modpython
    SetEnv DJANGO_SETTINGS_MODULE mysite.settings
    PythonDebug On
    PythonPath "['/home/USER-NAME/django_projects'] + sys.path"



    SetHandler None



    SetHandler None



    SetHandler None
```

Po provedení restartu serveru by měl Django projekt začít fungovat.
Projekt zobrazíme v prohlížeči (login i heslo do administrace je
"admin"):

``` {lang="bash"}
firefox http://127.0.0.1:666/polls/
firefox http://127.0.0.1:666/polls/1/
firefox http://127.0.0.1:666/polls/1/results/
firefox http://127.0.0.1:666/polls/1/vote/
firefox http://127.0.0.1:666/admin/
```

[caption id="attachment\_257" align="alignnone" width="300"
caption="Django admin"][![Django admin][]][][/caption]

<p>
Literatura

</h1>
[1] Apache HTTP Server In *Wikipedia : the free encyclopedia* [online].
St. Petersburg (Florida) : Wikipedia Foundation,\
 [cit. 2010-04-24]. Dostupné z WWW:
\<http://cs.wikipedia.org/wiki/Apache\_HTTP\_Server\>.

[2] *The Apache Software Foundation* [online]. 2010-04-24 [cit.
2010-04-24]. Apache HTTP Server Version 2.2 Documentation. Dostupné z
WWW: \<http://httpd.apache.org/docs/2.2/\>.

[3] *Mod\_python Apache/Python Integration* [online]. 2010-04-24 [cit.
2010-04-24]. Mod\_python Manual. Dostupné z WWW:
\<http://www.modpython.org/live/current/doc-html/modpython.html\>.

[4] *The Django framework* [online]. 2010-04-24 [cit. 2010-04-24]. How
to use Django with Apache and mod\_python. Dostupné z WWW:
\<http://docs.djangoproject.com/en/dev/howto/deployment/modpython/\>.

[5] *Jeff Baier* [online]. 2010-04-26 [cit. 2010-04-26]. Nstalling
Django on an Ubuntu Linux Server. Dostupné z WWW:
\<http://jeffbaier.com/articles/installing-django-on-an-ubuntu-linux-server/\>.

  [Apache HTTP Server]: http://www.apache.org/
  [Mod\_python]: http://www.modpython.org/
  [Django]: http://www.djangoproject.com/
  [Spuštění serveru Apache]: http://blog.jestrab.net/wp-content/uploads/apache-a-mod_python-pro-webovy-framework-django-1-300x206.jpg
    "Spuštění serveru Apache"
  [![Spuštění serveru Apache][]]: http://blog.jestrab.net/wp-content/uploads/apache-a-mod_python-pro-webovy-framework-django-1.jpg
    "Spuštění serveru Apache"
  [Ladící výpis mod\_python]: http://blog.jestrab.net/wp-content/uploads/apache-a-mod_python-pro-webovy-framework-django-2-300x206.jpg
    "Ladící výpis mod_python"
  [![Ladící výpis mod\_python][]]: http://blog.jestrab.net/wp-content/uploads/apache-a-mod_python-pro-webovy-framework-django-2.jpg
    "Ladící výpis mod_python"
  [Hello Python]: http://blog.jestrab.net/wp-content/uploads/apache-a-mod_python-pro-webovy-framework-django-4-300x206.jpg
    "Hello Python"
  [![Hello Python][]]: http://blog.jestrab.net/wp-content/uploads/apache-a-mod_python-pro-webovy-framework-django-4.jpg
    "Hello Python"
  [Calculator]: http://blog.jestrab.net/wp-content/uploads/apache-a-mod_python-pro-webovy-framework-django-3-300x206.jpg
    "Calculator"
  [![Calculator][]]: http://blog.jestrab.net/wp-content/uploads/apache-a-mod_python-pro-webovy-framework-django-3.jpg
    "Calculator"
  [Django admin]: http://blog.jestrab.net/wp-content/uploads/apache-a-mod_python-pro-webovy-framework-django-5-300x206.jpg
    "Django admin"
  [![Django admin][]]: http://blog.jestrab.net/wp-content/uploads/apache-a-mod_python-pro-webovy-framework-django-5.jpg
    "Django admin"
