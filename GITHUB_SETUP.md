# 📤 Publier sur GitHub - Guide Pas à Pas

## Prérequis

✅ Compte GitHub créé  
✅ Git installé sur votre PC  
✅ Projet prêt localement  

## Étape 1 : Créer le repository sur GitHub

1. Allez sur https://github.com
2. Cliquez sur le **+** en haut à droite → **New repository**
3. Remplissez :
   - **Repository name** : `python_vscode_test`
   - **Description** : `BDF Font Previewer - Visualize bitmap fonts without hardware`
   - **Public** ou **Private** : à votre choix
   - ⚠️ **NE COCHEZ PAS** "Add a README" (on en a déjà un)
4. Cliquez **Create repository**

## Étape 2 : Initialiser Git localement

Ouvrez un terminal dans votre projet :

```bash
# Aller dans le dossier du projet
cd C:\chemin\vers\MesProjets\Python\python_vscode_test

# Initialiser Git
git init

# Ajouter tous les fichiers
git add .

# Premier commit
git commit -m "Initial commit - BDF Font Previewer"
```

## Étape 3 : Lier au repository GitHub

GitHub vous donne des commandes après création du repo. Utilisez celles-ci :

```bash
# Ajouter le remote (remplacez VotreUsername par votre nom d'utilisateur GitHub)
git remote add origin https://github.com/VotreUsername/python_vscode_test.git

# Renommer la branche en 'main' (si nécessaire)
git branch -M main

# Pousser le code
git push -u origin main
```

**Note :** GitHub vous demandera peut-être de vous authentifier :
- Utilisez votre username GitHub
- Pour le mot de passe, utilisez un **Personal Access Token** (plus de support pour les mots de passe classiques)

## Étape 4 : Créer un Personal Access Token (si nécessaire)

Si Git vous demande un mot de passe :

1. Sur GitHub : **Settings** → **Developer settings** → **Personal access tokens** → **Tokens (classic)**
2. Cliquez **Generate new token (classic)**
3. Nom : `Git Access from PC`
4. Cochez : `repo` (full control)
5. Générez et **copiez le token** (vous ne le reverrez plus !)
6. Utilisez ce token comme mot de passe quand Git vous le demande

## Étape 5 : Vérifier

1. Allez sur `https://github.com/VotreUsername/python_vscode_test`
2. Vous devriez voir tous vos fichiers ! 🎉

## Workflow Quotidien

### Après avoir modifié des fichiers :

```bash
# Voir ce qui a changé
git status

# Ajouter les modifications
git add .

# Commit avec un message descriptif
git commit -m "Ajout fonction de simulation matricielle"

# Pousser sur GitHub
git push
```

### Raccourcis VS Code (plus facile !)

1. `Ctrl + Shift + G` pour ouvrir le panneau Git
2. Écrivez votre message de commit
3. Cliquez sur ✓ (commit)
4. Cliquez sur les 3 points → Push

## Structure Finale sur GitHub

```
python_vscode_test/
├── .vscode/
│   ├── settings.json
│   └── extensions.json
├── fonts/
│   └── (vos polices .bdf)
├── previews/
│   └── (aperçus générés)
├── examples/
│   └── (exemples d'images)
├── font_previewer.py
├── examples.py
├── requirements.txt
├── README.md
├── QUICKSTART.md
├── .gitignore
└── GITHUB_SETUP.md (ce fichier)
```

## Conseils

### Messages de commit clairs

✅ Bon :
```
git commit -m "Ajout support couleurs personnalisées"
git commit -m "Fix bug calcul largeur texte"
git commit -m "Documentation exemples d'usage"
```

❌ Mauvais :
```
git commit -m "update"
git commit -m "fix"
git commit -m "test"
```

### Créer des branches

Pour tester sans risque :

```bash
# Créer et basculer sur une nouvelle branche
git checkout -b feature/nouvelle-fonctionnalite

# Faire vos modifs, puis commit
git add .
git commit -m "Test nouvelle feature"

# Pousser la branche
git push -u origin feature/nouvelle-fonctionnalite

# Retour sur main
git checkout main

# Fusionner (si la feature marche)
git merge feature/nouvelle-fonctionnalite
```

### .gitignore est votre ami

Le `.gitignore` fourni exclut automatiquement :
- `__pycache__/` (fichiers temporaires Python)
- `venv/` (environnement virtuel - trop lourd)
- `.vscode/` (config locale)

## Problèmes Courants

### "remote origin already exists"
```bash
git remote remove origin
git remote add origin https://github.com/VotreUsername/python_vscode_test.git
```

### "Permission denied"
Vérifiez votre Personal Access Token ou configurez SSH

### "Nothing to commit"
C'est normal si vous n'avez rien modifié !

### Fichiers trop gros
GitHub limite à 100 MB par fichier. Utilisez Git LFS pour les gros fichiers.

## Ressources

- [GitHub Desktop](https://desktop.github.com/) - Interface graphique pour Git
- [Git Documentation](https://git-scm.com/doc)
- [GitHub Guides](https://guides.github.com/)

---

🎉 **Félicitations !** Votre projet est maintenant sur GitHub et accessible à tous !

N'oubliez pas d'ajouter une belle description et des tags sur la page du repo pour le rendre plus visible.
