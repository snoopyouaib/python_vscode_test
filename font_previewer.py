"""
BDF Font Previewer v0.1
==================
Visualisez vos polices BDF sans matériel - générez des aperçus PNG

Usage:
    python font_previewer.py
    python font_previewer.py --text "PILOTE" --font fonts/helvB12.bdf
    python font_previewer.py --compare  # Compare toutes les polices
"""

from PIL import Image, ImageDraw
import os
import argparse
from pathlib import Path


class BDFFont:
    """Parser simple pour fichiers BDF (Bitmap Distribution Format)"""
    
    def __init__(self, filepath):
        self.filepath = filepath
        self.name = Path(filepath).stem
        self.chars = {}
        self.properties = {}
        self._parse()
    
    def _parse(self):
        """Parse le fichier BDF"""
        with open(self.filepath, 'r', encoding='utf-8', errors='ignore') as f:
            lines = [line.strip() for line in f.readlines()]
        
        # Propriétés globales
        for line in lines:
            if line.startswith('FONT '):
                self.properties['font_name'] = line.split(' ', 1)[1]
            elif line.startswith('SIZE '):
                parts = line.split()
                self.properties['size'] = int(parts[1])
            elif line.startswith('FONTBOUNDINGBOX'):
                parts = line.split()
                self.properties['bbox_width'] = int(parts[1])
                self.properties['bbox_height'] = int(parts[2])
                self.properties['bbox_x'] = int(parts[3])
                self.properties['bbox_y'] = int(parts[4])
        
        # Parse chaque caractère
        i = 0
        while i < len(lines):
            if lines[i].startswith('STARTCHAR'):
                char_data = self._parse_char(lines, i)
                if char_data:
                    encoding = char_data['encoding']
                    self.chars[encoding] = char_data
            i += 1
    
    def _parse_char(self, lines, start_idx):
        """Parse un caractère individuel"""
        char_data = {}
        i = start_idx
        
        while i < len(lines) and not lines[i].startswith('ENDCHAR'):
            line = lines[i]
            
            if line.startswith('ENCODING'):
                char_data['encoding'] = int(line.split()[1])
            elif line.startswith('DWIDTH'):
                parts = line.split()
                char_data['dwidth_x'] = int(parts[1])
                char_data['dwidth_y'] = int(parts[2])
            elif line.startswith('BBX'):
                parts = line.split()
                char_data['bbx_width'] = int(parts[1])
                char_data['bbx_height'] = int(parts[2])
                char_data['bbx_x'] = int(parts[3])
                char_data['bbx_y'] = int(parts[4])
            elif line.startswith('BITMAP'):
                # Lire les données bitmap
                bitmap = []
                i += 1
                while i < len(lines) and not lines[i].startswith('ENDCHAR'):
                    bitmap.append(lines[i])
                    i += 1
                char_data['bitmap'] = bitmap
                break
            
            i += 1
        
        return char_data if 'encoding' in char_data else None
    
    def render_char(self, char_code):
        """Rend un caractère en image PIL"""
        if char_code not in self.chars:
            return None
        
        char_data = self.chars[char_code]
        width = char_data.get('bbx_width', 0)
        height = char_data.get('bbx_height', 0)
        
        if width == 0 or height == 0:
            return None
        
        # Créer l'image
        img = Image.new('1', (width, height), 0)
        pixels = img.load()
        
        bitmap = char_data.get('bitmap', [])
        for y, hex_line in enumerate(bitmap):
            if y >= height:
                break
            
            # Convertir hexa en bits
            # Important: la longueur de hex_line détermine combien de bits on a
            if not hex_line:
                continue
                
            value = int(hex_line, 16)
            # Calculer le nombre de bits disponibles (4 bits par caractère hexa)
            num_bits = len(hex_line) * 4
            
            # Extraire les bits de gauche à droite
            for x in range(min(width, num_bits)):
                # Bit le plus significatif en premier (MSB first)
                if value & (1 << (num_bits - 1 - x)):
                    pixels[x, y] = 1
        
        return img, char_data
    
    def render_text(self, text, spacing=2, scale=1):
        """Rend une chaîne de texte complète"""
        # Calculer la largeur totale
        total_width = 0
        char_images = []
        
        for char in text:
            char_code = ord(char)
            result = self.render_char(char_code)
            if result:
                img, data = result
                char_images.append((img, data))
                total_width += data.get('dwidth_x', img.width) + spacing
            else:
                # Espace pour caractère manquant
                total_width += 8 + spacing
        
        if not char_images:
            return None
        
        # Hauteur maximale
        max_height = self.properties.get('bbox_height', 16)
        
        # Créer l'image finale
        final_img = Image.new('1', (total_width, max_height), 0)
        
        x_offset = 0
        for img, data in char_images:
            # Position verticale (baseline)
            y_offset = max_height - data.get('bbx_height', 0) - data.get('bbx_y', 0)
            final_img.paste(img, (x_offset + data.get('bbx_x', 0), y_offset))
            x_offset += data.get('dwidth_x', img.width) + spacing
        
        # Appliquer le scale si demandé
        if scale > 1:
            new_size = (final_img.width * scale, final_img.height * scale)
            final_img = final_img.resize(new_size, Image.NEAREST)
        
        return final_img


def create_preview(font_path, text="ABCDEFGHIJKLMNOPQRSTUVWXYZ 0123456789", 
                   output_path=None, scale=4, bg_color=(30, 30, 30), 
                   fg_color=(0, 255, 100)):
    """Crée un aperçu PNG d'une police avec le texte donné"""
    
    font = BDFFont(font_path)
    
    # Rendre le texte
    bitmap = font.render_text(text, spacing=1, scale=1)
    
    if bitmap is None:
        print(f"❌ Impossible de rendre le texte avec {font.name}")
        return None
    
    # Convertir en RGB avec couleurs personnalisées
    width, height = bitmap.size
    rgb_img = Image.new('RGB', (width * scale, height * scale), bg_color)
    
    # Appliquer les pixels
    bitmap_scaled = bitmap.resize((width * scale, height * scale), Image.NEAREST)
    pixels_bmp = bitmap_scaled.load()
    pixels_rgb = rgb_img.load()
    
    for y in range(height * scale):
        for x in range(width * scale):
            if pixels_bmp[x, y]:
                pixels_rgb[x, y] = fg_color
    
    # Ajouter du padding et des infos
    padding = 20
    final_height = rgb_img.height + padding * 2 + 30
    final_img = Image.new('RGB', (rgb_img.width + padding * 2, final_height), bg_color)
    final_img.paste(rgb_img, (padding, padding + 30))
    
    # Ajouter le titre
    draw = ImageDraw.Draw(final_img)
    title = f"{font.properties.get('font_name', font.name)} - Size: {font.properties.get('size', 'N/A')}"
    draw.text((padding, 5), title, fill=(200, 200, 200))
    
    # Sauvegarder
    if output_path is None:
        output_path = f"previews/{font.name}_preview.png"
    
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    final_img.save(output_path)
    print(f"✅ Aperçu créé : {output_path}")
    
    return output_path


def simulate_matrix_display(font_path, text, matrix_width=64, matrix_height=64,
                            output_path=None):
    """Simule l'affichage sur une matrice RGB 64x64"""
    
    font = BDFFont(font_path)
    bitmap = font.render_text(text, spacing=1, scale=1)
    
    if bitmap is None:
        print(f"❌ Impossible de simuler avec {font.name}")
        return None
    
    # Créer l'image de la matrice
    scale = 8  # Chaque pixel de la matrice = 8x8 pixels dans l'aperçu
    matrix_img = Image.new('RGB', (matrix_width * scale, matrix_height * scale), (10, 10, 10))
    
    # Centrer le texte
    x_pos = (matrix_width - bitmap.width) // 2
    y_pos = (matrix_height - bitmap.height) // 2
    
    # Dessiner une grille légère pour visualiser les pixels
    draw = ImageDraw.Draw(matrix_img)
    for i in range(0, matrix_width * scale, scale):
        draw.line([(i, 0), (i, matrix_height * scale)], fill=(30, 30, 30), width=1)
    for i in range(0, matrix_height * scale, scale):
        draw.line([(0, i), (matrix_width * scale, i)], fill=(30, 30, 30), width=1)
    
    # Dessiner le texte
    pixels_bmp = bitmap.load()
    pixels_matrix = matrix_img.load()
    
    for y in range(bitmap.height):
        for x in range(bitmap.width):
            if pixels_bmp[x, y]:
                # Position sur la matrice
                mx = x_pos + x
                my = y_pos + y
                
                if 0 <= mx < matrix_width and 0 <= my < matrix_height:
                    # Remplir le pixel (8x8) en rouge (comme votre matrice)
                    for dy in range(scale):
                        for dx in range(scale):
                            px = mx * scale + dx
                            py = my * scale + dy
                            pixels_matrix[px, py] = (255, 0, 0)
    
    # Sauvegarder
    if output_path is None:
        output_path = f"previews/{font.name}_matrix_sim.png"
    
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    matrix_img.save(output_path)
    print(f"✅ Simulation matrice créée : {output_path}")
    
    return output_path


def compare_fonts(font_dir="fonts", text="PILOTE 12:45", output_path="previews/comparison.png"):
    """Compare toutes les polices disponibles côte à côte"""
    
    # Trouver tous les fichiers BDF
    font_files = list(Path(font_dir).glob("*.bdf"))
    
    if not font_files:
        print(f"❌ Aucune police trouvée dans {font_dir}")
        return None
    
    print(f"📚 {len(font_files)} police(s) trouvée(s)")
    
    # Rendre chaque police
    previews = []
    max_width = 0
    total_height = 0
    
    for font_file in font_files:
        font = BDFFont(font_file)
        bitmap = font.render_text(text, spacing=1, scale=4)
        
        if bitmap:
            previews.append((font.name, bitmap))
            max_width = max(max_width, bitmap.width)
            total_height += bitmap.height + 40  # 40 pour le titre
    
    if not previews:
        print("❌ Aucune police n'a pu être rendue")
        return None
    
    # Créer l'image de comparaison
    padding = 20
    bg_color = (30, 30, 30)
    final_img = Image.new('RGB', (max_width + padding * 2, total_height + padding * 2), bg_color)
    draw = ImageDraw.Draw(final_img)
    
    y_offset = padding
    for name, bitmap in previews:
        # Titre
        draw.text((padding, y_offset), name, fill=(200, 200, 200))
        y_offset += 20
        
        # Convertir bitmap en RGB
        rgb_preview = Image.new('RGB', bitmap.size, bg_color)
        pixels_bmp = bitmap.load()
        pixels_rgb = rgb_preview.load()
        
        for y in range(bitmap.height):
            for x in range(bitmap.width):
                if pixels_bmp[x, y]:
                    pixels_rgb[x, y] = (0, 255, 100)
        
        final_img.paste(rgb_preview, (padding, y_offset))
        y_offset += bitmap.height + 20
    
    # Sauvegarder
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    final_img.save(output_path)
    print(f"✅ Comparaison créée : {output_path}")
    
    return output_path


def main():
    parser = argparse.ArgumentParser(description="Prévisualiser des polices BDF")
    parser.add_argument('--font', type=str, help='Chemin vers un fichier .bdf')
    parser.add_argument('--text', type=str, default='ABCDEFGHIJKLMNOPQRSTUVWXYZ 0123456789',
                       help='Texte à afficher')
    parser.add_argument('--compare', action='store_true', 
                       help='Compare toutes les polices du dossier fonts/')
    parser.add_argument('--matrix', action='store_true',
                       help='Simule l\'affichage sur une matrice 64x64')
    parser.add_argument('--output', type=str, help='Fichier de sortie PNG')
    
    args = parser.parse_args()
    
    if args.compare:
        # Mode comparaison
        compare_fonts(text=args.text, output_path=args.output or "previews/comparison.png")
    
    elif args.font:
        # Mode fichier unique
        if args.matrix:
            simulate_matrix_display(args.font, args.text, output_path=args.output)
        else:
            create_preview(args.font, args.text, output_path=args.output)
    
    else:
        # Mode par défaut : traiter toutes les polices
        font_files = list(Path("fonts").glob("*.bdf"))
        
        if not font_files:
            print("❌ Aucune police trouvée dans le dossier fonts/")
            print("💡 Ajoutez vos fichiers .bdf dans le dossier fonts/")
            return
        
        print(f"📚 Traitement de {len(font_files)} police(s)...\n")
        
        for font_file in font_files:
            create_preview(str(font_file), args.text)
            simulate_matrix_display(str(font_file), "PILOTE", 
                                   output_path=f"previews/{font_file.stem}_matrix.png")
        
        print(f"\n✨ Terminé ! Vérifiez le dossier previews/")


if __name__ == "__main__":
    main()
