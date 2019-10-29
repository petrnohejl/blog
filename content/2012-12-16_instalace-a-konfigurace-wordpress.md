Title: Instalace a konfigurace Wordpress
Category: Informační technologie

Jedna známá potřebovala vyrobit web a požádala mě o jeho realizaci. Pro
její potřeby se skvěle hodí blogovací systém. Zvolil jsem Wordpress,
protože už s ním mám nějaké zkušenosti. Myslím, že to je pěkně udělaný
software a jeho výhoda je, že je open source. Rozhodl jsem se sepsat
podrobný návod/tutoriál, jak rychle nainstalovat a bezpečně nastavit
blogovací systém Wordpress. Postup instalace píšu hlavně pro vlastní
potřeby - určitě se ještě bude v budoucnu hodit.

## Instalace krok za krokem

 1. [Stáhneme](https://wordpress.org/download/) nejnovější originální verzi Wordpress (bez překladů).
 2. Zkopírujeme všechny soubory na server.
 3. Vytvoříme novou databázi v phpMyAdmin. Zvolíme porovnání
    *utf8\_general\_ci*.
 4. Spustíme instalaci v prohlížeči na adrese */wp-admin/setup-config.php*.
 5. Vyplníme přístupy k databázi a nastavíme prefix v názvu databázových
    tabulek. Prefix by neměl být z bezpečnostních důvodů "wp\_".
 6. Pokud nejde konfigurační soubor *wp-config.php* vytvořit automaticky,
    zkopírujeme konfiguraci do souboru *wp-config.php* manuálně a nahrajeme
    na server. Instalátor nastaví konfiguraci databáze, prefix a
    bezpečnostní klíče.
 7. Pokračujeme v instalaci na adrese */wp-admin/install.php*.
 8. Vyplníme základní údaje a vytvoříme administrátorský účet. Uživatelské
    jméno administrátora by nemělo být z bezpečnostních důvodů "admin".
    Spustíme instalaci.
 9. Nyní nastavíme další parametry v [konfiguračním souboru *wp-config.php*](#konfiguracni-soubor-wp-configphp):
    1.  Ujistíme se, že máme vyplněny bezpečnostní klíče. Pokud ne, můžeme
        je [vygenerovat](https://api.wordpress.org/secret-key/1.1/salt/).
    2.  Nastavíme jazyk (instalaci jazyka provedeme později).
    3.  Vypneme vytváření revizí.
    4.  Pokud jsme v minulosti vytvořili nějaké revize, můžeme je [smazat z databáze pomocí SQL příkazu](#odstraneni-revizi-z-databaze) ([zdroj](http://blog.andreineculau.com/2008/07/delete-wordpress-26-revisions/)).
    5.  Vypneme automatické ukládání.
10. Smažeme z adresáře */wp-content/plugins* nepotřebné pluginy. Např. Hello Dolly.
11. Smažeme z adresáře */wp-content/themes* nepotřebné šablony.
12. Stáhneme [češtinu pro Wordpress](http://www.separatista.net/):
    1.  Stáhneme češtinu pro samotný Wordpress a příslušné soubory
        zkopírujeme do adresáře */wp-content/languages*.
    2.  Stáhneme češtinu pro vybranou šablonu a příslušné soubory
        zkopírujeme do adresáře *languages* v adresáři se šablonou.
    3.  Aktuální verzi češtiny lze také stáhnout z [GlotPress](http://translate.wordpress.org/projects/wp/dev). Název
        hlavního souboru s češtinou by měl být "cs\_CZ", administrace
        "admin-cs\_CZ", města "continents-cities-cs\_CZ". Nahrát bychom měli
        soubory ve formátu ".po" a ".mo".
13. Přihlásíme se v administraci */wp-admin* a nastavíme:
    1.  Vzhled - vybereme šablonu a nastavíme její parametry. Pokud nechceme
        použít některou z oficiálních šablon, můžeme stáhnout z internetu
        jinou.
    2.  Uživatelé - vytvoříme uživatele (redaktory).
    3.  Nastavení - obecné nastavení blogu.
14. V Nastavení - trvalé odkazy - nakonfigurujeme *.htaccess* soubor. [Vygenerovaný kód](#soubor-htaccess) zkopírujeme na server do souboru */.htaccess*.
15. Volitelně můžeme použít [*.htaccess* a *.htpasswd*](#soubor-htaccess-pro-adresar-admin) v adresáři
    *wp-admin* pro zvýšení bezpečnosti. Přístup do administrace potom bude
    2x zaheslován. Soubor *.htpasswd* lze vygenerovat [zde](http://www.htaccesstools.com/htpasswd-generator/). Více na
    [websitedefender.com](http://www.websitedefender.com/wordpress-security/htaccess-files-wordpress-security/).
16. Nainstalujeme, aktivujeme a nastavíme pluginy:
    1.  [Akismet](https://wordpress.org/extend/plugins/akismet/)
    2.  [Bad Behavior](https://wordpress.org/extend/plugins/bad-behavior/)
    3.  [Simple Google Analytics](https://wordpress.org/extend/plugins/simple-google-analytics/)
    4.  [Sociable](https://wordpress.org/extend/plugins/sociable/)
    5.  [Comment Reply Notification](https://wordpress.org/extend/plugins/comment-reply-notification/)
    6.  [Resize Image After Upload](https://wordpress.org/extend/plugins/resize-image-after-upload/)
    7.  Případně místo předchozího [Resize images before upload](https://wordpress.org/extend/plugins/resize-images-before-upload/)
    8.  [Simple Lightbox](https://wordpress.org/extend/plugins/simple-lightbox/)
17. Vytvoříme účet na Google Analytics a nastavíme v pluginu UA kód.
18. Vytvoříme na serveru adresář */wp-content/uploads*.
19. Nastavíme práva souborů a složek webu na serveru pomocí příkazů *chmod*,
    *chown*, *chgrp*. Pro hromadné nastavení lze použít [skript](https://github.com/petrnohejl/Unix-Scripts/blob/master/permissions.sh).
20. V případě potřeby [ručně upravíme](#manualni-upravy-wordpressu) šablony/pluginy a uložíme si
    provedené změny pro případ aktualizace na novější verze dané
    šablony/pluginu.
21. V případě vydání aktualizace Wordpressu postupujeme podle [instrukcí](https://wordpress.org/support/article/updating-wordpress/).
22. Vytvoříme základní strukturu webu: kategorie, stránky, homepage, články.

## Konfigurační soubor wp-config.php

    :::php
    define('WPLANG', 'cs_CZ'); // language
    define('WP_POST_REVISIONS', 0); // disable revisions
    define('AUTOSAVE_INTERVAL', 86400 ); // disable autosave by long interval (in seconds)

## Odstranění revizí z databáze

    :::mysql
    DELETE a,b,c
    FROM wp_posts a
    LEFT JOIN wp_term_relationships b ON (a.ID = b.object_id)
    LEFT JOIN wp_postmeta c ON (a.ID = c.post_id)
    WHERE a.post_type = 'revision'

## Soubor .htaccess

    :::apache
    Options -Indexes
     
    RewriteEngine On
    RewriteBase /
    RewriteRule ^index\.php$ - [L]
    RewriteCond %{REQUEST_FILENAME} !-f
    RewriteCond %{REQUEST_FILENAME} !-d
    RewriteRule . /index.php [L]

## Soubor .htaccess pro adresář admin

Soubor *.htaccess*:

    :::apache
    AuthUserFile /home/www/com_example/www/wp-admin/.htpasswd
    AuthType Basic
    AuthName "Access to Wordpress admin"
    Order Deny,Allow
    Deny from all
    Require valid-user
    Satisfy any

Soubor *.htpasswd*, obsahující login "test", heslo "test":

    :::text
    test:$apr1$YGH0twy8$JeDHWGMP41wXRaxTFgqtr1

## Manuální úpravy Wordpressu

Úprava souboru *functions.php* v šabloně twentyeleven, která odstraní z
hlavního menu v administraci některé položky pro redaktory (pro admina
jsou zachovány):

    :::php
    // remove unnecessary menus
    // http://wordpress.stackexchange.com/questions/9505/hide-admin-menus-per-role-in-wordpress#answer-9581
    function remove_menus()
    {
        global $menu;
        global $current_user;
        get_currentuserinfo();
     
        if($current_user-&gt;user_level &lt; 10)
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

Úprava souboru *style.css* v šabloně twentyeleven, která zmenší a
přeuspořádá hlavičku webu:

    :::css
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

Úprava souboru *comment-reply-notification.php* v pluginu Comment Reply
Notification, která počeští checkbox ve formuláři:

    :::html+php
    function addreplyidformfield(){
        if($this->options['mail_notify'] === 'parent_check')
            echo '<p><input type="checkbox" name="comment_mail_notify" id="comment_mail_notify" value="comment_mail_notify" checked="checked" style="width: auto;" /><label for="comment_mail_notify">' . __('Upozornit e-mailem, pokud sem někdo přidá nový komentář', 'comment-reply-notification') . '</label></p>';
        elseif($this->options['mail_notify'] === 'parent_uncheck')
            echo '<p><input type="checkbox" name="comment_mail_notify" id="comment_mail_notify" value="comment_mail_notify" style="width: auto;" /><label for="comment_mail_notify">' . __('Upozornit e-mailem, pokud sem někdo přidá nový komentář', 'comment-reply-notification') . '</label></p>';
        else{}
    }

Úprava souboru *class.resize.php* v pluginu Resize Image After Upload,
která změní kompresní poměr obrázků:

    :::php
    function saveImage($numQuality = 75){
    ...

Úprava souboru *sociable.css* v pluginu Sociable, která opraví rozhozený
layout u Facebook tlačítka:

    :::css
    #Facebook_Counter iframe {
        width:128px !important;
    }
