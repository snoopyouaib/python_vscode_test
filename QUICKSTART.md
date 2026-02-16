# 🚀 Guide de Démarrage Rapide

## Installation en 3 étapes

### 1. Cloner et ouvrir dans VS Code
```bash
git clone https://github.com/VotreUsername/python_vscode_test.git
cd python_vscode_test
code .
```

### 2. Créer l'environnement virtuel
```bash
python -m venv venv
venv\Scripts\activate  # Windows
pip install -r requirements.txt
```

### 3. Ajouter vos polices
Copiez vos fichiers `.bdf` dans le dossier `fonts/`

## Utilisation Rapide

### Tester avec vos polices
```bash
python font_previewer.py
```

### Comparer vos polices
```bash
python font_previewer.py --compare --text "PILOTE 12:45"
```

### Simuler sur matrice 64x64
```bash
python font_previewer.py --font fonts/helvB12.bdf --text "SESSION 1" --matrix
```

## Résultats

Tous les aperçus sont dans `previews/` :
- `[police]_preview.png` - aperçu standard
- `[police]_matrix.png` - simulation matrice
- `comparison.png` - comparaison de toutes les polices

## Exemples Avancés

Pour voir tous les cas d'usage :
```bash
python examples.py
```

## Aide

Toutes les options :
```bash
python font_previewer.py --help
```

## Prochaines Étapes

1. ✅ Testez vos polices
2. 📸 Générez des aperçus
3. 🎯 Choisissez la meilleure police pour votre projet
4. 🚀 Utilisez-la sur votre Pico !

---

Pour plus de détails, consultez [README.md](README.md)
