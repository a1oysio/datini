# Prodotti olivicoli di Foggia — dataset

Prezzi settimanali all'ingrosso di olio d'oliva, olive da olio e olive da mensa
rilevati il mercoledì dalla Borsa Merci di Foggia, letti dai listini PDF
pubblicati dalla
[Camera di Commercio di Foggia](https://www.fg.camcom.gov.it/servizi/storico-dei-listini-settimanali).
Dal 9 ottobre 2024.

**Condizioni d'uso.** Le stesse del listino dei cereali: vedi
[`dataset/foggia/`](../foggia/README.md). Leggi anche il
[DISCLAIMER](../../DISCLAIMER.md).

## File e schema

Come per [Foggia](../foggia/README.md) e [Bologna](../bologna/README.md):
`products.csv`, `prices/<anno>.csv` con `date, code, low, high`, `meta.json`,
`datapackage.json`, `exchange.json`; `revisions.csv` compare alla prima
rettifica. I codici sono assegnati dal progetto alla prima comparsa della voce.

È un dataset a parte da quello dei cereali perché il listino è un altro
documento, con una numerazione sua, anche se esce lo stesso giorno e si legge
con lo stesso parser.

## Cose da sapere

- **Unità.** L'olio è in euro al chilo (`EUR/kg`), le olive in euro al quintale
  (`EUR/100kg`), come le scrive il listino. Non convertire senza guardare
  l'unità.
- **Stagione.** Olive da olio e da mensa si quotano solo da ottobre a gennaio;
  nel resto dell'anno le righe ci sono ma sono vuote.
- **Non quotato.** `NQ` diventa un campo vuoto. Molte voci DOP e IGP sono quasi
  sempre non quotate.
