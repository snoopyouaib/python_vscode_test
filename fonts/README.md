# 📁 Dossier Fonts

## Où trouver vos polices BDF ?

Vos polices BDF se trouvent déjà sur votre Pico dans le projet `circuitpython_test` !

### Sur votre Pico (CIRCUITPY)
```
CIRCUITPY:/fonts/
└── helvB12.bdf
```

### Copier depuis le Pico vers ce projet

1. Branchez votre Pico en USB
2. Ouvrez le lecteur `CIRCUITPY:`
3. Copiez le dossier `fonts/` complet ici

**Ou depuis votre projet GitHub :**
https://github.com/snoopyouaib/circuitpython_test/tree/main/fonts

## Structure recommandée

```
fonts/
├── helvB12.bdf          # Votre police actuelle
├── autre_police.bdf     # Autres polices à tester
└── README.md            # Ce fichier
```

## Où trouver plus de polices BDF ?

### Sources gratuites

1. **X.Org Fonts** (polices bitmap classiques)
   - https://www.x.org/releases/

2. **Adafruit CircuitPython Fonts**
   - https://github.com/adafruit/Adafruit_CircuitPython_Bitmap_Font

3. **GNU Unifont**
   - http://unifoundry.com/unifont/

4. **Vintage Computer Fonts**
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

## Conseils

- **Taille** : Pour une matrice 64x64, privilégiez des polices de 8 à 16 pixels de haut
- **Largeur** : Testez que votre texte tient sur 64 pixels
- **Lisibilité** : Les polices bold (gras) sont plus visibles sur LED
- **Mono vs Proportionnelle** : Les polices monospace sont plus faciles à calculer

## Compatibilité CircuitPython

Toutes les polices BDF ne fonctionnent pas forcément avec `adafruit_bitmap_font`. Testez d'abord avec ce script Python avant de les uploader sur le Pico !

## Besoin d'aide ?

Utilisez `font_previewer.py` pour :
- ✅ Tester si la police est compatible
- ✅ Voir le rendu avant upload
- ✅ Vérifier que votre texte tient
- ✅ Comparer plusieurs polices

---

💡 **Astuce** : Gardez ce dossier versionné dans Git pour ne pas perdre vos polices testées !
