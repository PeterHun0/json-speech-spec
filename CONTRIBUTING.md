# Hozzájárulási útmutató

Köszönjük, hogy hozzájárulsz a JSON Speech Spec fejlesztéséhez!

## Hogyan javasolj új mezőt?

- Nyiss egy GitHub issue-t vagy pull requestet
- Írd le: cél, típusa, példaérték, AI-érintettség

## Validálási lépések új fájlhoz

1. Használj UTF-8 karakterkódolást
2. Érvényesíts a `json_format_v1_1.schema.json` alapján
3. Tartsd be a mezők sorrendjét és neveit
4. Ne hagyj el kötelező mezőt

## Formázási irányelvek

- Minden mező `camelCase` vagy `snake_case` (de konzisztens)
- Időbélyegek: ISO 8601 (`YYYY-MM-DD` vagy `YYYY-MM-DDThh:mm:ss`)
- Szövegformázás: idézőjelek `"` mindig, semmi aposztróf `'`