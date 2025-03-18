# Úvod do programování v jazyce Python

## 9/03/2025

## Proměnné

Proměnné jsou místa, kam ukládáme různé hodnoty, které se v průběhu programu mohou měnit.

V jazyce python deklarujeme proměnnou vytvořením názvu a přiřazením hodnoty.

```python
x = 5 
y = "Hello"
```

Hodnotu i datový typ proměnné můžeme v průběhu programu měnit.

```python
x = 5 
x = "World" # x má nyní hodnotu "World"
```

## Datové typy

Proměnné mohou ukládat data v různých datových typech, které nám například určují, jakých hodnot smí proměnná nabývat nebo jaké operace se s těmito daty mohou provádět.

Základními datovými typy v pythonu jsou:

| název | zkratka | popis | hodnota |
| --- | --- | --- | --- |
| integer | int | celá čísla | -2, 0, 3, 15 |
| float | float | reálná čísla, čísla s plovoucí <br> desetinnou čárkou (v pythonu desetinná tečka) | -3.5, 0.2, 5.0 |
| boolean | bool | pravdivostní hodnoty | True, False |
| string | str | textové řetězce | "Pepa", "Hello world", "5" |
| list | list | seznamy, uspořádané soubory hodnot | [1, 6, 8, -2], ["jablko", "banán"] |

Python obsahuje i další datové typy, ale ty pro účely tohoto návodu zatím potřebovat nebudeme.

## Základní aritmetické operace

Základní aritmetické operátory:

| symbol | popis |
| --- | --- |
| +, -, *, / | základní aritmetické operace |
| //, % | celočíselné dělení, zbytek po dělení |
| ** | umocnění |

Operátory porovnávání:

| symbol | popis |
| --- | --- |
| ==, != | rovná se, nerovná se |
| >, < | větší, menší |
| >=, <= | větší rovno, menší rovno |

Výstupem porovnávání je datový typ boolean – hodnoty True a False.

# Základy jazyka Python

V následující kapitole si ukážeme základy jazyka Python.

## Komentáře

Jazyk Python nám umožňuje do kódu vkládat komentáře. Při spuštění kódu se tento blok nezpracovává. Komentáře tedy slouží např. pro vysvětlení části kódu.

  

```python
# Toto je komentář
```

## Výstup do konzole

Výstup kódu v pythonu chceme obvykle vypsat do konzole. Pro to nám slouží funkce `print()` . Tato funkce nám umožňuje do konzole vypisovat například text, proměnné, pole,…

```python
print("Hello world") # funkce do konzole vypíše text "Hello world""
```

Funkce `print()` nám také umožňuje vypisovat více hodnot na jeden řádek:

```python
x = 5
print(x, 10, "Jablko")
```

## Vstup z konzole

Pomocí funkce `input()` můžeme získat vstup z konzole od uživatele.

```python
x = input() # do proměnné x se uloží hodnota zadaná na vstupu
```

Funkci input() můžeme také doplnit o vstupní hlášku:

```python
x = input("Zadej hodnotu x: ") # při spuštění kódu se objeví hláška "Zadej hodnotu x: "
```

> POZOR: hodnota zadaná na vstupu bude vždy uložena jako text. Pokud budeme chtít datový typ změnit, musíme hodnotu **přetypovat.**
> 

## Práce s proměnnými

Z jedné z předchozí kapitol už víme, co to proměnná je. Nyní se naučíme s proměnnými pracovat.

### Pravidla pro pojmenování proměnných

Samotný jazyk Python žádná pravidla pro pojmenování proměnných neurčuje, ale pro zachování přehlednosti kódu se řídíme podle pravidel pro stylizaci Python kódu.

Názvy proměnných píšeme vždy malými písmeny:

```python
variable = 5
```

Pro víceslovné názvy proměnných používáme jako oddělovač podtržítko `_`. Tomuto způsobu zápisu říkáme *snake case.*

```python
my_name = "Pepa"
```

> Vsuvka: nejpoužívanějšími způsoby zápisu názvů v programování jsou:
> 
> - camelCase
> - snake_case
> - PascalCase

Dobrým pravidlem při vytváření názvu proměnných je dávat proměnné takový název, ze kterého můžeme odhadnout, jakou hodnotu proměnná pravděpodobně nese. Pokud budu například používat proměnnou, která má jako hodnotu mé jméno, dám ji název `my_name`. Vím tedy, že tato proměnná bude pravděpodobně obsahovat textový řetězec se jménem.

Jelikož v programování se používá výhradně angličtina, je dobré dávat proměnným anglické názvy.

Také musíme dávat pozor na rezervovaná klíčová slova – tato slova nemůžeme použít jako názvy proměnných. Těmito slovy jsou: 

`False` `True` `None` `and` `as` `assert` `break` `class` `continue` `def` `del` `elif` `else` `except` `finally` `for` `from` `global` `if` `import` `in` `is` `lambda` `nonlocal` `not` `or` `pass` `raise` `return` `try` `while` `with` `yield`

> Nezapomeňte, že Python je tzv. *case sensitive –* rozlišuje malá a velká písmena. Tudíž například proměnné `var` a `Var` jsou dvě různé proměnné.
> 

### Přetypování proměnných

Řekli jsme si, že při vytváření proměnné Python určí její datový typ podle přiřazené hodnoty. Někdy se nám ale může stát, že tento datový typ chceme změnit – proto je možné proměnné v Pythonu “přetypovávat”. Pro to nám slouží funkce `int()`, `float()`, `str()` a další.

```python
x = 5 # proměnné x je přiřazena celočíselná hodnota hodnota 5 – tudíž je datový typ integer

x = str(x) # proměnná x je přetypována na textový řetězec – datový typ string. V x je nyní uložena hodnota "5"

x = float(x) # proměnná x je přetypována na reálné číslo – datový typ float. V x je nyní uložena hodnota 5.0

x = int(x) # proměnná x je nyní přetypována zpět na integer. V x je nyní uložena hodnota 5
```
# Spracoval Jan Hruška, Matyáš Grabka, Alex Levandovsky

