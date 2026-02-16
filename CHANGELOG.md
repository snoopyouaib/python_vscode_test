# 📝 Changelog

## Version 1.1 - 2026-02-16

### 🐛 Corrections
- **Fix parser BDF** : Correction du rendu des polices avec padding (ex: Spleen)
  - Le parser gère maintenant correctement les données hexadécimales de tailles variables
  - Les polices comme `spleen-5x8.bdf` et `spleen-12x24.bdf` s'affichent correctement
  - Bug: les caractères apparaissaient fragmentés ou incomplets

### ✨ Améliorations
- **Support des sous-dossiers** : Le script scanne maintenant récursivement tous les sous-dossiers de `fonts/`
  - Organisez vos polices par catégorie (small/, medium/, large/, etc.)
  - `python font_previewer.py` trouve automatiquement toutes les polices
  - `--compare` fonctionne aussi avec les sous-dossiers

### 📚 Documentation
- Mise à jour du README dans `fonts/` avec exemples d'organisation
- Ajout de suggestions de structure par taille/type de police

## Version 1.0 - 2026-02-16

### 🎉 Version Initiale
- Parser BDF complet pour fichiers Bitmap Distribution Format
- Génération d'aperçus PNG avec couleurs personnalisables
- Simulation de matrice RGB 64x64
- Comparaison de plusieurs polices côte à côte
- Support ligne de commande avec arguments
- Exemples d'utilisation (examples.py)
- Documentation complète
- Configuration VS Code
- Support Git/GitHub

---

## 🔮 Améliorations Futures Possibles

- [ ] Support d'autres formats de polices (PCF, PSF)
- [ ] Interface graphique (Tkinter/Qt)
- [ ] Animation de scroll en temps réel
- [ ] Export en sprite sheet
- [ ] Métriques de lisibilité automatiques
- [ ] Génération de variantes (bold, italic)
- [ ] Preview avec plusieurs lignes de texte
- [ ] Support des polices couleur
- [ ] Batch processing avec configuration JSON
- [ ] Conversion entre formats de polices
