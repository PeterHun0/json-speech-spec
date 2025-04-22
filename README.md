# JSON Speech Spec v1.1

Ez a projekt egy szabványosított `.json` formátumot definiál beszédfelismeréshez, fordításhoz és AI-alapú narrációhoz. A formátum célja, hogy géppel jól feldolgozható, kontextus-gazdag, többrétegű szövegblokkokat tároljon, beleértve az AI és emberi munka megkülönböztetését is.

## Tartalom

- `json_format_spec_with_markup_v1_1_FINAL.md` – Ember által olvasható specifikáció
- `json_format_v1_1.schema.json` – Gépi validálási séma (Draft-07)
- `testdata/` – Tesztpéldák különböző nyelveken
- `releases/` – Verziótörténet

## Használat

```bash
# JSON validálása Node.js alatt:
npm install -g ajv-cli
ajv validate -s json_format_v1_1.schema.json -d testdata/sample_en.json
```

## Licenc

MIT License – szabadon felhasználható és módosítható, forrásmegjelöléssel.