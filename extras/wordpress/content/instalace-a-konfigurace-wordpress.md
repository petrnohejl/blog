Title: Instalace a konfigurace Wordpress
Date: 2012-12-16 01:58
Author: peno
Category: Informační technologie, Nové
Tags: blog, tutoriál, webdesign, Wordpress
Slug: instalace-a-konfigurace-wordpress

Jedna známá potřebovala vyrobit web a požádala mě o jeho realizaci. Pro
její potřeby se skvěle hodí blogovací systém. Zvolil jsem Wordpress,
protože už s ním mám nějaké zkušenosti. Myslím, že to je pěkně udělaný
software a jeho výhoda je, že je open source. Rozhodl jsem se sepsat
podrobný návod/tutoriál, jak rychle nainstalovat a bezpečně nastavit
blogovací systém Wordpress. Postup instalace píšu hlavně pro vlastní
potřeby - určitě se ještě bude v budoucnu hodit.

Instalace krok za krokem
========================

<ol>
<li>
[Stáhneme][] nejnovější originální verzi Wordpress (bez překladů).

</li>
<li>
Zkopírujeme všechny soubory na server.

</li>
<li>
Vytvoříme novou databázi v phpMyAdmin. Zvolíme porovnání
*utf8\_general\_ci*.

</li>
<li>
Spustíme instalaci v prohlížeči na adrese */wp-admin/setup-config.php*.

</li>
<li>
Vyplníme přístupy k databázi a nastavíme prefix v názvu databázových
tabulek. Prefix by neměl být z bezpečnostních důvodů "wp\_".

</li>
<li>
Pokud nejde konfigurační soubor *wp-config.php* vytvořit automaticky,
zkopírujeme konfiguraci do souboru *wp-config.php* manuálně a nahrajeme
na server. Instalátor nastaví konfiguraci databáze, prefix a
bezpečnostní klíče.

</li>
<li>
Pokračujeme v instalaci na adrese */wp-admin/install.php*.

</li>
<li>
Vyplníme základní údaje a vytvoříme administrátorský účet. Uživatelské
jméno administrátora by nemělo být z bezpečnostních důvodů "admin".
Spustíme instalaci.

</li>
<li>
Nyní nastavíme další parametry v [konfiguračním souboru
*wp-config.php*][]:

</li>
1.  Ujistíme se, že máme vyplněny bezpečnostní klíče. Pokud ne, můžeme
    je [vygenerovat][].
2.  Nastavíme jazyk (instalaci jazyka provedeme později).\
3.  Vypneme vytváření revizí*.*
4.  Pokud jsme v minulosti vytvořili nějaké revize, můžeme je [smazat z
    databáze pomocí SQL příkazu][] ([zdroj][]).\
5.  Vypneme automatické ukládání*.*

<li>
Smažeme z adresáře */wp-content/plugins* nepotřebné pluginy. Např. Hello
Dolly.

</li>
<li>
Smažeme z adresáře */wp-content/themes* nepotřebné šablony.

</li>
<li>
Stáhneme [češtinu pro Wordpress][]:

</li>
1.  Stáhneme češtinu pro samotný Wordpress a příslušné soubory
    zkopírujeme do adresáře */wp-content/languages*.
2.  Stáhneme češtinu pro vybranou šablonu a příslušné soubory
    zkopírujeme do adresáře *languages* v adresáři se šablonou.
3.  Aktuální verzi češtiny lze také stáhnout z [GlotPress][]. Název
    hlavního souboru s češtinou by měl být "cs\_CZ", administrace
    "admin-cs\_CZ", města "continents-cities-cs\_CZ". Nahrát bychom měli
    soubory ve formátu ".po" a ".mo".

<li>
Přihlásíme se v administraci */wp-admin* a nastavíme:

</li>
1.  Vzhled - vybereme šablonu a nastavíme její parametry. Pokud nechceme
    použít některou z oficiálních šablon, můžeme stáhnout z internetu
    jinou.
2.  Uživatelé - vytvoříme uživatele (redaktory).
3.  Nastavení - obecné nastavení blogu.

<li>
V Nastavení - trvalé odkazy - nakonfigurujeme *.htaccess* soubor.
[Vygenerovaný kód][] zkopírujeme na server do souboru */.htaccess*.

</li>
<li>
Volitelně můžeme použít [*.htaccess* a *.htpasswd*][] v adresáři
*wp-admin* pro zvýšení bezpečnosti. Přístup do administrace potom bude
2x zaheslován. Soubor *.htpasswd* lze vygenerovat [zde][]. Více na
[websitedefender.com][].

</li>
<li>
Nainstalujeme, aktivujeme a nastavíme pluginy:

</li>
1.  [Akismet][]
2.  [Bad Behavior][]
3.  [Simple Google Analytics][]
4.  [Sociable][]
5.  [Comment Reply Notification][]
6.  [Resize Image After Upload][]
7.  Případně místo předchozího [Resize images before upload][]
8.  [Simple Lightbox][]

<li>
Vytvoříme účet na Google Analytics a nastavíme v pluginu UA kód.

</li>
<li>
Vytvoříme na serveru adresář */wp-content/uploads*.

</li>
<li>
Nastavíme práva souborů a složek webu na serveru pomocí příkazů *chmod*,
*chown*, *chgrp*. Pro hromadné nastavení lze použít [skript][].

</li>
<li>
V případě potřeby [ručně upravíme][] šablony/pluginy a uložíme si
provedené změny pro případ aktualizace na novější verze dané
šablony/pluginu.

</li>
<li>
V případě vydání aktualizace Wordpressu postupujeme podle [instrukcí][].

</li>
<li>
Vytvoříme základní strukturu webu: kategorie, stránky, homepage, články.

</li>
</ol>
Konfigurační soubor wp-config.php {#bookmark-wpconfig}
=================================

``` {lang="php"}
define('WPLANG', 'cs_CZ'); // language
define('WP_POST_REVISIONS', 0); // disable revisions
define('AUTOSAVE_INTERVAL', 86400 ); // disable autosave by long interval (in seconds)
```

Odstranění revizí z databáze {#bookmark-revisions}
============================

``` {lang="mysql"}
DELETE a,b,c
FROM wp_posts a
LEFT JOIN wp_term_relationships b ON (a.ID = b.object_id)
LEFT JOIN wp_postmeta c ON (a.ID = c.post_id)
WHERE a.post_type = 'revision'
```

Soubor .htaccess {#bookmark-htaccess}
================

``` {lang="apache"}
Options -Indexes

RewriteEngine On
RewriteBase /
RewriteRule ^index\.php$ - [L]
RewriteCond %{REQUEST_FILENAME} !-f
RewriteCond %{REQUEST_FILENAME} !-d
RewriteRule . /index.php [L]
```

Soubor .htaccess pro adresář admin {#bookmark-htaccess-wpadmin}
==================================

Soubor *.htaccess*:

``` {lang="apache"}
AuthUserFile /home/www/com_example/www/wp-admin/.htpasswd
AuthType Basic
AuthName "Access to Wordpress admin"
Order Deny,Allow
Deny from all
Require valid-user
Satisfy any
```

Soubor *.htpasswd*, obsahující login "test", heslo "test":

``` {lang="apache"}
test:$apr1$YGH0twy8$JeDHWGMP41wXRaxTFgqtr1
```

Manuální úpravy Wordpressu {#bookmark-customize}
==========================

Úprava souboru *functions.php* v šabloně twentyeleven, která odstraní z
hlavního menu v administraci některé položky pro redaktory (pro admina
jsou zachovány):

``` {lang="php"}
// remove unnecessary menus
// http://wordpress.stackexchange.com/questions/9505/hide-admin-menus-per-role-in-wordpress#answer-9581
function remove_menus()
{
    global $menu;
    global $current_user;
    get_currentuserinfo();

    if($current_user->user_level < 10)
    {
        $restricted = array(
                            __('Appearance'),
                            __('Plugins'),
                            __('Users'),
                            __('Tools'),
                            __('Settings'),
        );
        end ($menu);
        while (prev($menu)){
            $value = explode(' ',$menu[key($menu)][0]);
            if(in_array($value[0] != NULL?$value[0]:"" , $restricted)){unset($menu[key($menu)]);}
        }// end while

    }// end if
}
add_action('admin_menu', 'remove_menus');
```

Úprava souboru *style.css* v šabloně twentyeleven, která zmenší a
přeuspořádá hlavičku webu:

``` {lang="css"}
#page {
    margin: 1em auto;
}
#site-title {
    float: left;
    padding: 0;
    margin: 20px 20px 20px 0;
}
#site-description {
    float: left;
    clear: none;
    font-size: 24px;
    font-weight: bold;
    line-height: 36px;
    padding: 0;
    margin: 20px 0 20px 0;

}
#site-title a {
    font-size: 24px;
}
#branding #searchform {
    top: 22px;
}
#branding img {
    clear: both;
}
```

Úprava souboru *comment-reply-notification.php* v pluginu Comment Reply
Notification, která počeští checkbox ve formuláři:

``` {lang="php"}
function addreplyidformfield(){
    if($this->options['mail_notify'] === 'parent_check')
        echo '' . __('Upozornit e-mailem, pokud sem někdo přidá nový komentář', 'comment-reply-notification') . '';
    elseif($this->options['mail_notify'] === 'parent_uncheck')
        echo '' . __('Upozornit e-mailem, pokud sem někdo přidá nový komentář', 'comment-reply-notification') . '';
    else{}
}
```

Úprava souboru *class.resize.php* v pluginu Resize Image After Upload,
která změní kompresní poměr obrázků:

``` {lang="php"}
function saveImage($numQuality = 75){
...
```

Úprava souboru *sociable.css* v pluginu Sociable, která opraví rozhozený
layout u Facebook tlačítka:

``` {lang="css"}
#Facebook_Counter iframe {
    width:128px !important;
}
```

  [Stáhneme]: http://wordpress.org/download/
  [konfiguračním souboru *wp-config.php*]: #bookmark-wpconfig
  [vygenerovat]: https://api.wordpress.org/secret-key/1.1/salt/
  [smazat z databáze pomocí SQL příkazu]: #bookmark-revisions
  [zdroj]: http://blog.andreineculau.com/2008/07/delete-wordpress-26-revisions/
  [češtinu pro Wordpress]: http://www.separatista.net/
  [GlotPress]: http://translate.wordpress.org/projects/wp/dev
  [Vygenerovaný kód]: #bookmark-htaccess
  [*.htaccess* a *.htpasswd*]: #bookmark-htaccess-wpadmin
  [zde]: http://www.htaccesstools.com/htpasswd-generator/
  [websitedefender.com]: http://www.websitedefender.com/wordpress-security/htaccess-files-wordpress-security/
  [Akismet]: http://wordpress.org/extend/plugins/akismet/
  [Bad Behavior]: http://wordpress.org/extend/plugins/bad-behavior/
  [Simple Google Analytics]: http://wordpress.org/extend/plugins/simple-google-analytics/
  [Sociable]: http://wordpress.org/extend/plugins/sociable/
  [Comment Reply Notification]: http://wordpress.org/extend/plugins/comment-reply-notification/
  [Resize Image After Upload]: http://wordpress.org/extend/plugins/resize-image-after-upload/
  [Resize images before upload]: http://wordpress.org/extend/plugins/resize-images-before-upload/
  [Simple Lightbox]: http://wordpress.org/extend/plugins/simple-lightbox/
  [skript]: https://github.com/petrnohejl/Unix-Scripts/blob/master/permissions.sh
  [ručně upravíme]: #bookmark-customize
  [instrukcí]: %20http://codex.wordpress.org/Upgrading_WordPress
