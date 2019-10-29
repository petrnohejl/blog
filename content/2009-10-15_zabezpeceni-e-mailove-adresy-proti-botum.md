Title: Zabezpečení e-mailové adresy proti botům
Category: Informační technologie

Ahoj! Dneska jsem programoval můj nový web a narazil jsem na
problematiku antispamové ochrany e-mailové adresy na stránkách.
Potřeboval jsem vypsat na web klasický e-mailový odkaz a nechtěl jsem
pro to používat žádné speciální nástroje jako např. generování obrázku,
captcha apod. Přečetl jsem si několik diskuzí a podařilo se mi e-mailové
adresy na mých stránkách zabezpečit níže popsaným způsobem. Jak moc je
zabezpečení účinné si netroufám odhadnout, ale myslím si, že mnoho
spambotů mu podlehne. Samozřejmě nejlepší je e-mailové kontakty
nezveřejňovat, pokud to není potřeba. V následujícím příkladu je použita
vymyšlená adresa mail@mail.cz.

## HTML kód odkazu

    :::html
    <a class="contact">
    m&#97;<!--spambot@.&#64;retarder-->&#105;l<span><!--spambot&#64;.@retarder-->@</span>&#109;ai&#108;<!--spambot@.&#64;retarder-->.cz
    </a>

## jQuery skript

    :::javascript
    $(document).ready(function() {
        bind_mail ();
    });

    function bind_mail () {
        $('.contact').attr("hr"+"ef", "ma"+"il" + "to:"+"mai" +  /*spambot@.retarder*/ "l@m" +  /*spambot.@retarder*/ "ai"+"l.cz");
    }

## Vysvětlení

Znaky e-mailové adresy převedeme pomocí [převodníku](https://textmod.pavucina.com/prevod-html-entity) na HTML entity
(můžeme zkombinovat normální znaky s HTML entitami). Znak zavináče
obalíme do značky `<span>` a to celé vložíme do značky `<a>`, která
ovšem nebude mít parametr `href`. Mezi znaky navíc vložíme několik
komentářů. Do komentáře navíc můžeme vložit nějaké znaky (zavináč,
tečka), používané v e-mailové adrese, abychom bota ještě více zmátli. V
Java Scriptovém kódu spojíme pomocí operátoru zřetězení více podřetězců
a můžeme opět vložit několik komentářů na zmatení.

Při načtení stránky se zavolá funkce, která přidá všem elementům s
třídou `.contact` atribut `href` s příslušnou hodnotou. Výsledkem je, že
uživateli s podporou Java Scriptu se zobrazí plnohodnotný klikací odkaz.
Uživateli bez podpory Java Scriptu se sice nezobrazí normální odkaz, ale
uvidí danou adresu a může si ji případně zkopírovat.

Běžný spambot bude hledat adresu odkazu, který ukazuje na e-mail pomocí
prefixu `mailto:`. Zde však narazí, protože atribut `href` nastavuje až
Java Script. Spambot by mohl procházet i Java Scripty, ale dle mého
názoru je toto málo pravděpodobné, protože by už bylo hledání adresy
příliš náročné. Dalšími překážkami pro bota jsou kódované znaky do HTML
entit, vložené komentáře a značky `<span>`, zřetězené podřetězce.
Podobných překážek pro spamboty lze vymyslet ještě více, např.
zalamování sekvence kódu na více řádků apod. Více o této problematice se
můžete dozvědět například na [security-portal.cz](https://www.security-portal.cz/clanky/jak-skr%C3%BDt-emailovou-adresu-p%C5%99ed-spammery).
