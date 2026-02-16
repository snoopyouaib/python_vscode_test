# 📁 Dossier Fonts

## Organisation Recommandée

Vous pouvez organiser vos polices dans des sous-dossiers par catégorie :

```
fonts/
├── small/              # Polices petites (5-10px)
│   ├── spleen-5x8.bdf
│   ├── tiny-8x8.bdf
│   └── micro.bdf
│
├── medium/             # Polices moyennes (11-16px)
│   ├── helvB12.bdf
│   ├── terminus-12.bdf
│   └── fixed-13.bdf
│
├── large/              # Polices grandes (17-24px)
│   ├── spleen-12x24.bdf
│   └── bold-20.bdf
│
├── monospace/          # Polices à chasse fixe
│   └── courier-12.bdf
│
├── proportional/       # Polices proportionnelles
│   └── helvetica-12.bdf
│
└── README.md           # Ce fichier
```

**Le script scanne automatiquement tous les sous-dossiers !** 🔍

## Structure Simple (Alternative)

Vous pouvez aussi tout mettre à la racine si vous préférez :

```
fonts/
├── spleen-5x8.bdf
├── helvB12.bdf
├── spleen-12x24.bdf
└── README.md
```

## Où trouver vos polices BDF ?

### Sur votre Pico (CIRCUITPY)
```
CIRCUITPY:/fonts/
└── helvB12.bdf
```

### Depuis votre projet GitHub
https://github.com/snoopyouaib/circuitpython_test/tree/main/fonts

## Où trouver plus de polices BDF ?

### Sources gratuites

1. **X.Org Fonts** (polices bitmap classiques)
   - https://www.x.org/releases/

2. **Adafruit CircuitPython Fonts**
   - https://github.com/adafruit/Adafruit_CircuitPython_Bitmap_Font

3. **GNU Unifont**
   - http://unifoundry.com/unifont/

4. **Spleen** (polices bitmap modernes)
   - https://github.com/fcambus/spleen

5. **Vintage Computer Fonts**
   - https://github.com/rewtnull/amigafonts

### Créer vos propres polices

**FontForge** (gratuit et open-source) :
- https://fontforge.org/
- Peut convertir TTF → BDF

**Online BDF Editor** :
- https://velipso.com/tools/bdf-editor/

## Format BDF

Le format BDF (Bitmap Distribution Format) est un format texte qui décrit des polices bitmap pixel par pixel.

### Exemple minimal

```
STARTFONT 2.1
FONT -misc-fixed-medium-r-normal--10-100-75-75-c-60-iso8859-1
SIZE 10 75 75
FONTBOUNDINGBOX 6 10 0 -2
STARTCHAR A
ENCODING 65
DWIDTH 6 0
BBX 5 7 0 0
BITMAP
20
50
88
88
F8
88
88
ENDCHAR
ENDFONT
```

## Conseils par Taille de Matrice

### Matrice 64x64 (votre cas)
- **Petites** (5-8px) : Texte long, plusieurs lignes
- **Moyennes** (10-14px) : Équilibre lisibilité/espace
- **Grandes** (16-24px) : Mots courts, très lisible

### Recommandations
- **Bold/Gras** : Plus visible sur LED
- **Monospace** : Plus facile à calculer l'espacement
- **Sans-serif** : Plus lisible en petit

## Utilisation du Script

### Scanner tous les sous-dossiers
```bash
python font_previewer.py
```

### Comparer toutes les polices (même dans sous-dossiers)
```bash
python font_previewer.py --compare --text "PILOTE"
```

### Tester une police spécifique
```bash
python font_previewer.py --font fonts/small/spleen-5x8.bdf --text "TEST"
```

## Compatibilité CircuitPython

Toutes les polices BDF ne fonctionnent pas forcément avec `adafruit_bitmap_font`. 

**Testez d'abord avec ce script avant de les uploader sur le Pico !**

## Besoin d'aide ?

Utilisez `font_previewer.py` pour :
- ✅ Tester si la police est compatible
- ✅ Voir le rendu avant upload
- ✅ Vérifier que votre texte tient
- ✅ Comparer plusieurs polices

---

💡 **Astuce** : Gardez ce dossier versionné dans Git pour ne pas perdre vos polices testées !
