# 🔤 BDF Font Previewer

Prévisualisez vos polices BDF (Bitmap Distribution Format) sans matériel - générez des aperçus PNG pour tester avant de les utiliser sur votre matrice RGB ou autres affichages embarqués.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)

## ✨ Fonctionnalités

- 📸 **Aperçus PNG** de vos polices BDF
- 🎨 **Simulation de matrice RGB** 64x64 pixels
- 🔄 **Comparaison** de plusieurs polices côte à côte
- 🎯 **Texte personnalisé** pour tester vos cas d'usage
- ⚡ **Rapide et simple** - un seul script Python

## 🚀 Installation

### 1. Cloner le projet

```bash
git clone https://github.com/VotreUsername/python_vscode_test.git
cd python_vscode_test
```

### 2. Créer un environnement virtuel (recommandé)

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/macOS
python3 -m venv venv
source venv/bin/activate
```

### 3. Installer les dépendances

```bash
pip install -r requirements.txt
```

## 📖 Utilisation

### Mode basique - Toutes les polices

Traite toutes les polices du dossier `fonts/` :

```bash
python font_previewer.py
```

Génère :
- `previews/[nom_police]_preview.png` - aperçu standard
- `previews/[nom_police]_matrix.png` - simulation matrice 64x64

### Aperçu d'une police spécifique

```bash
python font_previewer.py --font fonts/helvB12.bdf --text "PILOTE 12:45"
```

### Simulation matrice RGB

Voir comment votre texte apparaîtra sur une matrice 64x64 :

```bash
python font_previewer.py --font fonts/helvB12.bdf --text "PILOTE" --matrix
```

### Comparaison de polices

Comparer toutes vos polices avec le même texte :

```bash
python font_previewer.py --compare --text "SESSION 1"
```

### Personnaliser la sortie

```bash
python font_previewer.py --font fonts/helvB12.bdf --text "CUSTOM" --output mon_apercu.png
```

## 📁 Structure du Projet

```
python_vscode_test/
├── font_previewer.py    # Script principal
├── fonts/               # Placez vos fichiers .bdf ici
│   └── helvB12.bdf     # Exemple de police
├── previews/            # Aperçus générés (créé auto)
├── examples/            # Exemples d'utilisation
├── requirements.txt     # Dépendances Python
├── README.md           # Ce fichier
└── .gitignore          # Fichiers à ignorer par Git
```

## 🎨 Exemples de Résultats

### Aperçu Standard
![Exemple aperçu](examples/example_preview.png)

### Simulation Matrice 64x64
![Exemple matrice](examples/example_matrix.png)

### Comparaison
![Exemple comparaison](examples/example_comparison.png)

## 🔧 Options Avancées

### Couleurs personnalisées

Éditez `font_previewer.py` :

```python
# Ligne ~150 - create_preview()
bg_color=(30, 30, 30)    # Fond sombre
fg_color=(0, 255, 100)   # Vert pour le texte

# Ligne ~200 - simulate_matrix_display()
pixels_matrix[px, py] = (255, 0, 0)  # Rouge (comme votre matrice)
```

### Taille de la simulation

```python
# Ligne ~195
scale = 8  # Chaque pixel matrice = 8x8 pixels dans l'aperçu
```

## 🎯 Cas d'Usage

### Pour matrices RGB (Pico + CircuitPython)

1. Testez vos polices **avant** de les uploader sur le Pico
2. Vérifiez que votre texte **tient** sur 64 pixels
3. Comparez la **lisibilité** de différentes polices
4. Générez des **docs** avec des aperçus

### Pour documentation

1. Créez des aperçus de toutes vos polices
2. Incluez-les dans votre README
3. Partagez avec votre équipe

### Pour développement UI

1. Testez différents textes
2. Vérifiez l'espacement
3. Optimisez la lisibilité

## 🐛 Dépannage

### Erreur "No module named 'PIL'"

```bash
pip install Pillow
```

### Police non reconnue

Vérifiez que votre fichier est bien au format BDF (Bitmap Distribution Format). Les fichiers doivent contenir les sections `STARTCHAR`, `BITMAP`, etc.

### Caractères manquants

Certaines polices ne contiennent pas tous les caractères. Le script affichera un espace pour les caractères manquants.

## 🔮 Améliorations Futures

- [ ] Support d'autres formats de polices (PCF, PSF)
- [ ] Interface graphique (Tkinter/Qt)
- [ ] Animation de scroll
- [ ] Export en sprite sheet
- [ ] Éditeur de police intégré

## 🤝 Contribution

Les contributions sont les bienvenues !

1. Fork le projet
2. Créez une branche (`git checkout -b feature/amelioration`)
3. Commit vos changements (`git commit -m 'Ajout fonctionnalité X'`)
4. Push (`git push origin feature/amelioration`)
5. Ouvrez une Pull Request

## 📝 License

MIT License - Voir [LICENSE](LICENSE) pour plus de détails

## 👨‍💻 Auteur

**Noopy** - Développeur embarqué (Pico, CircuitPython, MicroPython)

## 🙏 Remerciements

- Format BDF créé par Adobe
- Communauté Adafruit pour les bibliothèques CircuitPython
- Claude pour l'assistance au développement

## 📚 Ressources

- [Format BDF Specification](https://www.adobe.com/content/dam/acom/en/devnet/font/pdfs/5005.BDF_Spec.pdf)
- [CircuitPython BDF Fonts](https://learn.adafruit.com/custom-fonts-for-pyportal-circuitpython-display)
- [Pillow Documentation](https://pillow.readthedocs.io/)

---

⭐ Si ce projet vous aide, n'hésitez pas à lui donner une étoile !
