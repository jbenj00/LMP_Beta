# X4 Scripting Reference — Claude Code Source Pack

**Rebuilt:** 2026-11-10 from supplied `X4_Scripting_Reference.html`.  
**Reference origin:** game archive extracts identified by the source HTML, originally extracted 2026-11-09.  
**Target:** GUNPIRE Logistics / X4: Foundations 9.00.

## Read this first

This package contains **byte-for-byte recovered originals** embedded in the supplied HTML, rather than a lossy HTML-to-Markdown conversion. The five recovered files match the MD5 hashes recorded in the HTML source. The source itself describes archive numbers for these files; we have not independently inspected the user's installed game version.

### Primary sources

| File | Purpose |
|---|---|
| `schemas/md.xsd` | MD schema: cues, conditions, actions, XML structure |
| `schemas/aiscripts.xsd` | AI script schema |
| `schemas/common.xsd` | Shared action/condition/type schema used by MD and AI |
| `schemas/scriptproperties.xml` | Script property definitions and datatype relations |
| `schemas/scriptproperties.html` | Original ancillary property documentation HTML |

### Fast targeted indexes

| Index | Purpose |
|---|---|
| `indexes/INDEX_md.md` | MD top-level declarations |
| `indexes/INDEX_aiscripts.md` | AI top-level declarations |
| `indexes/INDEX_common.md` | Shared top-level declarations |
| `indexes/INDEX_scriptproperties.md` | Direct properties grouped by datatype |
| `indexes/INDEX_GUNPIRE_topics.md` | GUNPIRE-relevant symbol *name matches* |
| `indexes/symbols.json` | Searchable machine-readable symbol catalog |
| `SOURCE_CHECKSUMS.json` | Size, MD5, and SHA256 of recovered sources |

## Usage for Claude Code

1. Start with `README.md` and the relevant `indexes/INDEX_*.md`.
2. Search a specific symbol in the original XSD/XML, and inspect surrounding declaration and attributes.
3. For MD and AI snippets check nested node definitions in their schemas and `common.xsd`.
4. For properties, check the owning datatype and parent/import inheritance in `scriptproperties.xml`.
5. Cross-check examples with vanilla/installed mod source. **Schema acceptance does not guarantee the desired engine runtime behavior.**
6. Record uncertainties as UNVERIFIED. Do not fabricate actions, events, or Lua hooks.

## Coverage and limits

- Recovered schema declarations: md.xsd 47, aiscripts.xsd 47, common.xsd 396.
- Recovered direct datatype properties: 1940.
- The bundle does **not** include X4 Lua API documents or runtime test results. Use separate GUNPIRE UI/support references and inspect actual Lua mod sources.
- The output is a documentation/reference pack, **not an installable game extension**.
- The original HTML is not included inside this package; retain it separately for human browsing.

## Integrity

Original source MD5 checksums were matched against the HTML-embedded original source data. See `SOURCE_CHECKSUMS.json` for exact hashes.
