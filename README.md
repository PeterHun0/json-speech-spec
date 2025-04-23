
# JSON Speech Spec

This repository defines a standardized JSON format for representing structured, interpretable speech data.
It aims to support multilingual projects, speech synthesis, and AI training datasets.

## 🎯 Objectives
- Interoperable, language-agnostic format
- Support for speech recognition and synthesis
- Easy validation via JSON Schema
- Readable by both humans and machines

---

## 🧩 Structure

### Required fields:
```json
{
  "meta": {
    "language": "en",
    "version": "1.0"
  },
  "segments": [
    {
      "start": "00:00:01.000",
      "end": "00:00:03.000",
      "text": "Hello world!"
    }
  ]
}
```

### Field explanations:
- `meta.language`: ISO 639-1 code (e.g., `"en"`, `"de"`, `"fr"`)
- `meta.version`: version of the specification (e.g., `"1.0"`)
- `segments`: list of timestamped text blocks
  - `start`, `end`: timestamps (e.g., `"00:00:01.000"`)
  - `text`: spoken text in that segment

---

## ✅ Validation

Use the provided JSON Schema `schema/speech-spec-schema.json` for validation:

```bash
python tools/validate_json.py examples/example_en.json schema/speech-spec-schema.json
```

---

## 🔄 Conversion

The tool `tools/json_to_txt.py` converts JSON speech data to plain TXT:

```bash
python tools/json_to_txt.py examples/example_en.json
```

---

## 🌍 Language Examples

The `examples/` folder includes files in:
- English (`example_en.json`)
- German (`example_de.json`)
- French (`example_fr.json`)
- Spanish (`example_es.json`)
- Chinese (`example_zh.json`)

---

## 🤝 Contributing

See `CONTRIBUTING.md` for guidelines on contributing.

---

## 📄 License

This project is licensed under the MIT License. See `LICENSE`.

---

## 🔮 Development Roadmap (Based on Claude & Gemini suggestions)

- Glossary and reviewer fields, character limits, placeholders
- Support for synthesis & XLIFF-inspired compatibility
- Reducing redundancy and improving status tracking
- Machine translation & human review coordination
- JSON Schema kept in sync with documentation

---

## 📚 Addendum: .TXT format standard (2025-04-17)

^^|@-@    FULL CONSOLIDATED SUMMARY – ChatGPT and .TXT standardization    @-@|^^

^^|@-@    DATE: 2025-04-17    @-@|^^

### 1. ChatGPT Versions & AI Models
- OpenAI models: GPT-3, GPT-3.5, GPT-4, GPT-4 Turbo (currently used)
- Other systems: Claude (Anthropic), Gemini (Google), LLaMA (Meta), Grok (xAI)
- GPT-5 expected in late 2025 – goal: multimodal AI with adaptive submodel switching
- Access tiers: Free, Plus, Pro

### 2. .TXT Specification – v1.0 and v1.1 Principles

**Core (v1.0):**
- Version handling and base format: ^^|@-@    ...    @-@|^^
- Date format: ISO 8601 (YYYY-MM-DD)
- Required blocks: version, date, content, closure

**Extended syntax (v1.1 – TextTranslationISO format):**
- 🔹 Block ID: 3 letters + 3 digits (e.g., ABC123)
- 🔹 ENTER block: line breaks marked as `==ENTER==` with unique ID
- 🔹 Suggested block length: max 5 lines (12pt, A4)

**Syntax example:**
```
^^|[{ABC123}]|^^
^^|<Original text>|^^
^^|->Translated text<-|^^
^^|//Translator note//|^^
^^|#Developer comment#|^^
^^|@@Context@@|^^
^^|%%Duration in seconds%%|^^
^^|§§Status§§|^^
^^|-##Translator ID##-|^^
^^|[/{ABC123}/]|^^
```

**Symbol meanings:**
- `^^|[{ID}]|^^` – Block start  
- `^^|[/{ID}/]|^^` – Block end  
- `<...>` – Original text  
- `->...<-` – Translated text  
- `=AI=` – Machine-generated content  
- `//...//` – Translator note  
- `#...#` – Developer comment  
- `@@...@@` – Context  
- `%%...%%` – Duration  
- `§§...§§` – Status  
- `-##...##-` – Translator ID  

### 3. Practical Use
- ChatGPT interprets text files according to the current version (v1.0)
- Future changes will be versioned (e.g., v1.1)

### 4. Next Steps
- GPT-5 discussion scheduled for this week
- The standard format is actively used and applied to all related documents

^^|@-@    END    @-@|^^
