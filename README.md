# Úvod do programování: příklady ke zkoušce
## Daniel Pumr

V této složce lze nalézt programy vytvořené pro splnění zkoušky z předmětu 
Úvod do programování na Přirodovědecké fakultě Univerzity Karlovy.
Podrobná dokumentace a popis fungování programů je v souboru [dokumentace.pdf](dokumentace.pdf).
Níže je pouze stručně popsáno fungování programů z hlediska uživatele.

### [posloupnost1](posloupnost1.py)
Úkolem tohoto programu je ze dvou zadaných posloupností čísel vytvořit sjednocení.

Po spuštění se program nejprve zeptá, zda chcete pracovat s desetinnými čísly. 
V případě, že chcete, aby dokázal program desetinná čísla zpracovat, na pište “ano”. 
Program akceptuje také zápis “ANO” a “Ano”. Pokud nezapíšete nic či cokoli jiného 
než jednu z vybraných možností, program bude pracovat pouze s celými čísly 
a po zadání desetinného skončí s chybou.
Dále je třeba postupně zadat vstupní posloupnosti, ze kterých bude vytvořeno sjednocení. 
Jednotlivá čísla oddělujte mezerou. Desetinná čísla zapisujte s tečkou. 
Pokud bude posloupnost zapsána s desetinnými čísly ačkoli tak nebyl program nastaven, 
desetinná čísla budou zapsána s čárkou, nebo budou-li použity jiné znaky než čísla, 
program skončí s chybou. V jedné posloupnosti by se nemělo jedno číslo objevovat dvakrát. 
V takovém případě se objeví dvakrát i ve sjednocené posloupnosti.
Po zadání těchto vstupů program ukáže výslednou sjednocenou posloupnost.

### [posloupnost2](posloupnost2.py)
Program z hlediska uživatele funguje stejně jako program posloupnost1.py s tím rozdílem, 
že kromě sjednocení informuje i o průniku a doplňcích. 
Dále také program v případě více stejných hodnot zadaných do jedné posloupnosti narozdíl 
od programu posloupnost1.py tyto hodnoty zachová.
Hlavní rozdíl oproti prvnímu programu je ve zdrojovém kódu.

### [vzdalenost](vzdalenost.py)
Úkolem tohoto programu je spočítat vzdálenost mezi dvěma body na kouli.

Po spuštění programu budete ze všeho nejdříve otázáni, jaký poloměr má koule, 
na která bude vzdálenost mezi body počítána. Hodnotu udávejte v kilometrech, 
desetinná čísla pište za tečku. Pokud hodnotu nezadáte, nebo zadáte hodnotu, 
která není v platném formátu, bude program počítat s hodnotou 6371,11, 
která reprezentuje střední poloměr planety Země.
Před dalším postupem vás program informuje o tom, kterou hodnotu přijal a bude s ní počítat. 
Následně je třeba zadat souřadnice bodů, pro které bude vzdálenost počítána. 
Šířku a délku bodu zadávejte ve stupních, desetinná čísla oddělujte tečkou. 
V případě, že zadáte hodnotu, které souřadnice nemohou nabývat, 
program vás o tom informuje a vyzve vás k opakovanému zadání. 
V případě, že zadáte jinou než číselnou hodnotu, program bude ukončen.
Po správném zadání souřadnic program souhrnně vypíše, se kterými hodnotami počítal 
a pod tím vypíše vzdálenost bodů v kilometrech.

