# Esercitazione – Gestione File da Terminale

## Obiettivo
Creare una struttura di progetto da terminale usando i comandi `mkdir`, `touch`, `cp`, `mv`, `tree` e `history`.

---

## Parte 1 – Crea la struttura

Nella cartella **Documenti**, crea la seguente struttura di cartelle:

```
sito-web/
├── assets/
├── archivio/
├── scripts/
└── pages/
```


Crea i seguenti file vuoti nelle rispettive cartelle:

- **assets/**: `style.css`, `logo.png`
- **scripts/**: `app.js`, `helpers.js`  
- **pages/**: `index.html`, `about.html`


---

## Parte 2 – Copia i file nella cartella archivio

Copia **solo i file** (non le sottocartelle) da `assets/`, `scripts/` e `pages/` nella cartella `archivio/`:

```bash
cp sito-web/assets/* sito-web/archivio/
cp sito-web/scripts/* sito-web/archivio/
cp sito-web/pages/* sito-web/archivio/
```

---

## Parte 3 – Rinomina i file copiati

Rinomina tutti i file nella cartella `archivio/` aggiungendo `_old` prima dell'estensione:

**Esempi:**
- `app.js` → `app_old.js`
- `style.css` → `style_old.css`
---

## Parte 4 – Verifica e consegna

### 1. Verifica con `tree`


**Risultato atteso:**
```
sito-web/
├── archivio/
│   ├── about_old.html
│   ├── app_old.js
│   ├── helpers_old.js
│   ├── index_old.html
│   ├── logo_old.png
│   └── style_old.css
├── assets/
│   ├── logo.png
│   └── style.css
├── pages/
│   ├── about.html
│   └── index.html
└── scripts/
    ├── app.js
    └── helpers.js
```

### 2. Visualizza la cronologia comandi

```bash
history
```

### 3. **Consegna**

1. Copia **a mano** tutti i comandi da `history`
2. Incollali in `comandi.txt`
---