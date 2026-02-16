"""
Exemples d'utilisation du BDF Font Previewer
=============================================

Ce fichier montre différentes façons d'utiliser le module font_previewer
"""

from font_previewer import BDFFont, create_preview, simulate_matrix_display, compare_fonts
from pathlib import Path


def example_1_basic_preview():
    """Exemple 1 : Créer un aperçu simple d'une police"""
    print("=== Exemple 1 : Aperçu basique ===\n")
    
    font_path = "fonts/helvB12.bdf"
    
    if Path(font_path).exists():
        create_preview(
            font_path=font_path,
            text="PILOTE SESSION 1",
            output_path="previews/example1.png"
        )
    else:
        print(f"⚠️  Police non trouvée : {font_path}")
        print("💡 Ajoutez vos fichiers .bdf dans le dossier fonts/")


def example_2_matrix_simulation():
    """Exemple 2 : Simuler l'affichage sur une matrice RGB"""
    print("\n=== Exemple 2 : Simulation matrice 64x64 ===\n")
    
    font_path = "fonts/helvB12.bdf"
    
    if Path(font_path).exists():
        simulate_matrix_display(
            font_path=font_path,
            text="12:45",
            matrix_width=64,
            matrix_height=64,
            output_path="previews/example2_matrix.png"
        )
    else:
        print(f"⚠️  Police non trouvée : {font_path}")


def example_3_custom_colors():
    """Exemple 3 : Utiliser des couleurs personnalisées"""
    print("\n=== Exemple 3 : Couleurs personnalisées ===\n")
    
    font_path = "fonts/helvB12.bdf"
    
    if Path(font_path).exists():
        create_preview(
            font_path=font_path,
            text="ROUGE BLEU VERT",
            output_path="previews/example3_red.png",
            bg_color=(0, 0, 0),      # Fond noir
            fg_color=(255, 0, 0)     # Texte rouge
        )
        
        create_preview(
            font_path=font_path,
            text="ROUGE BLEU VERT",
            output_path="previews/example3_blue.png",
            bg_color=(0, 0, 0),      # Fond noir
            fg_color=(0, 100, 255)   # Texte bleu
        )
    else:
        print(f"⚠️  Police non trouvée : {font_path}")


def example_4_compare_all_fonts():
    """Exemple 4 : Comparer toutes les polices disponibles"""
    print("\n=== Exemple 4 : Comparaison de polices ===\n")
    
    compare_fonts(
        font_dir="fonts",
        text="DEBUTANT 09:00",
        output_path="previews/example4_comparison.png"
    )


def example_5_programmatic_usage():
    """Exemple 5 : Utiliser la classe BDFFont directement"""
    print("\n=== Exemple 5 : Usage programmatique ===\n")
    
    font_path = "fonts/helvB12.bdf"
    
    if Path(font_path).exists():
        # Charger la police
        font = BDFFont(font_path)
        
        # Afficher les propriétés
        print(f"Nom de la police : {font.properties.get('font_name', 'N/A')}")
        print(f"Taille : {font.properties.get('size', 'N/A')}")
        print(f"BBox : {font.properties.get('bbox_width', 'N/A')}x{font.properties.get('bbox_height', 'N/A')}")
        print(f"Nombre de caractères : {len(font.chars)}")
        
        # Rendre un seul caractère
        char_img, char_data = font.render_char(ord('A'))
        if char_img:
            print(f"\nCaractère 'A' :")
            print(f"  Largeur : {char_data['bbx_width']} pixels")
            print(f"  Hauteur : {char_data['bbx_height']} pixels")
            print(f"  Avancement : {char_data['dwidth_x']} pixels")
        
        # Rendre du texte
        text_img = font.render_text("HELLO", spacing=2, scale=1)
        if text_img:
            print(f"\nTexte 'HELLO' :")
            print(f"  Dimensions : {text_img.size[0]}x{text_img.size[1]} pixels")
    else:
        print(f"⚠️  Police non trouvée : {font_path}")


def example_6_test_all_categories():
    """Exemple 6 : Tester les 4 catégories de votre projet paddock"""
    print("\n=== Exemple 6 : Test catégories paddock ===\n")
    
    font_path = "fonts/helvB12.bdf"
    
    if not Path(font_path).exists():
        print(f"⚠️  Police non trouvée : {font_path}")
        return
    
    categories = [
        ("PILOTE", (255, 0, 0)),      # Rouge
        ("CONFIRME", (255, 255, 0)),  # Jaune
        ("INTER", (0, 255, 0)),       # Vert
        ("DEBUTANT", (0, 100, 255))   # Bleu
    ]
    
    for text, color in categories:
        create_preview(
            font_path=font_path,
            text=text,
            output_path=f"previews/category_{text.lower()}.png",
            bg_color=(20, 20, 20),
            fg_color=color,
            scale=6
        )
        
        simulate_matrix_display(
            font_path=font_path,
            text=text,
            output_path=f"previews/matrix_{text.lower()}.png"
        )


if __name__ == "__main__":
    print("🎨 BDF Font Previewer - Exemples d'utilisation\n")
    print("=" * 60)
    
    # Créer le dossier previews s'il n'existe pas
    Path("previews").mkdir(exist_ok=True)
    
    # Vérifier qu'il y a des polices
    fonts = list(Path("fonts").glob("*.bdf"))
    if not fonts:
        print("\n⚠️  ATTENTION : Aucune police .bdf trouvée dans fonts/")
        print("💡 Ajoutez vos fichiers .bdf dans le dossier fonts/ pour tester\n")
        return
    
    print(f"✅ {len(fonts)} police(s) trouvée(s)\n")
    
    # Exécuter les exemples
    try:
        example_1_basic_preview()
        example_2_matrix_simulation()
        example_3_custom_colors()
        example_4_compare_all_fonts()
        example_5_programmatic_usage()
        example_6_test_all_categories()
        
        print("\n" + "=" * 60)
        print("✨ Tous les exemples ont été exécutés !")
        print("📁 Vérifiez le dossier previews/ pour voir les résultats")
        
    except Exception as e:
        print(f"\n❌ Erreur : {e}")
        import traceback
        traceback.print_exc()
