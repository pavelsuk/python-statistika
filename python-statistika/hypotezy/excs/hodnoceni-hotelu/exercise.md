---
title: Hodnocení hotelů
demand: 2
---

Stáhni si soubor [global_hotel_reviews.csv](assets/global_hotel_reviews.csv). Naším úkolem je porovnat průměrné hodnocení hotelů ve Francii a Švýcarsku. Číselné hodnocení je ve sloupci `Rating` a obsahuje pouze hodnoty 2, 4, 6, 8 a 10. V tomto případě použij Mann-Whitney test, protože data nemají normální rozdělení. Země, kde se hotel nachází, je ve sloupci `Country`.

1. Definuj testové hypotézy.
1. Proveď test hypotézy a vyhodnoť výsledky.

Níže máš kód k načtení dat. Vytvoří ti dvě série (`data_fr` a `data_sw`) a ty můžeš použít ve svém testu.


```python
import pandas as pd

# Načtení dat z CSV souboru do DataFrame objektu
# Ty pravděpodobně podadresář statistika-1-assets nemáš, tak ho smaž
data = pd.read_csv("statistika-1-assets/global_hotel_reviews.csv")

# Přetvoření tabulky tak, aby se hodnoty "Rating" seskupily pod jediný sloupec "variable"
data = data.melt("Country", "Rating")

# Vyfiltrování dat pouze pro zemi "France" a získání hodnot sloupce "value"
data_fr = data[data["Country"] == "France"]["value"]

# Vyfiltrování dat pouze pro zemi "Switzerland" a získání hodnot sloupce "value"
data_sw = data[data["Country"] == "Switzerland"]["value"]

```
