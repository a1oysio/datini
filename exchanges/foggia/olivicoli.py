"""Prodotti olivicoli di Foggia: il secondo listino settimanale della Borsa Merci.

Dall'ottobre 2024 la Camera di Commercio pubblica a parte olio d'oliva, olive da
olio e olive da mensa.  Il PDF ha lo stesso impianto di quello dei cereali e si
legge con lo stesso parser; cambia solo la cartella da cui si scarica.  Ha una
numerazione sua, quindi e' un dataset a parte: ``dataset/foggia-olivicoli/``.

    python -m pipeline.update  --exchange foggia-olivicoli
    python -m exchanges.foggia.olivicoli --dest data/foggia-olivicoli
"""
from __future__ import annotations

from exchanges.foggia import fetcher
from exchanges.foggia.fetcher import fetch  # noqa: F401  (per pipeline.bologna.Source)
from exchanges.foggia.parser import parse_file  # noqa: F401

CODE = "FG-OL"
NAME = "Prodotti olivicoli di Foggia"
SLUG = "foggia-olivicoli"
SOURCE_URL = fetcher.INDEX_URL
LICENSE = "Listini pubblici della Camera di Commercio di Foggia, riutilizzabili citando la fonte"


def list_bulletins(timeout: float = 30.0):
    return fetcher.list_bulletins(timeout, folder=fetcher.OLIVICOLI)


if __name__ == "__main__":
    raise SystemExit(fetcher.main(fetcher.OLIVICOLI))
