#!/usr/bin/python3

import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import (
    SquareModuleDrawer,
    CircleModuleDrawer,
    RoundedModuleDrawer,
    GappedSquareModuleDrawer,
    VerticalBarsDrawer,
    HorizontalBarsDrawer,
)
from qrcode.image.styles.colormasks import (
    RadialGradiantColorMask,
    HorizontalGradiantColorMask,
    VerticalGradiantColorMask,
    SolidFillColorMask,
)
import os



# Couleurs pour le terminal
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def print_header():
    """Affiche un en-tête stylisé."""
    header = f"""
{Colors.HEADER}{Colors.BOLD}
  _____          _   _ ____  _____ ____
 |_   _|__   ___| | | | __ )| ____|  _ \
   | |/ _ \ / __| | | |  _ \|  _| | |_) |
   | | (_) | (__| |_| | |_) | |___|  _ <
   |_|\___/ \___|\___/|____/|_____|_| \_\
{Colors.ENDC}
{Colors.BLUE}Générateur de QR Codes Personnalisés{Colors.ENDC}
    """
    print(header)

def print_shapes_menu():
    """Affiche le menu des formes."""
    print(f"\n{Colors.YELLOW}--- Formes disponibles ---{Colors.ENDC}")
    print(f"{Colors.GREEN}1.{Colors.ENDC} Carrés")
    print(f"{Colors.GREEN}2.{Colors.ENDC} Cercles")
    print(f"{Colors.GREEN}3.{Colors.ENDC} Carrés arrondis")
    print(f"{Colors.GREEN}4.{Colors.ENDC} Carrés creux")
    print(f"{Colors.GREEN}5.{Colors.ENDC} Barres verticales")
    print(f"{Colors.GREEN}6.{Colors.ENDC} Barres horizontales")

def print_colors_menu():
    """Affiche le menu des couleurs."""
    print(f"\n{Colors.YELLOW}--- Styles de couleur disponibles ---{Colors.ENDC}")
    print(f"{Colors.GREEN}1.{Colors.ENDC} Noir uni")
    print(f"{Colors.GREEN}2.{Colors.ENDC} Dégradé radial (bleu -> rouge)")
    print(f"{Colors.GREEN}3.{Colors.ENDC} Dégradé horizontal (rouge -> bleu)")
    print(f"{Colors.GREEN}4.{Colors.ENDC} Dégradé vertical (vert -> jaune)")

def generate_custom_qr(url, output_path, filename, module_drawer, color_mask):
    """Génère un QR code avec la forme et la couleur choisies."""
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(
        image_factory=StyledPilImage,
        module_drawer=module_drawer,
        color_mask=color_mask,
    )
    output_file = os.path.join(output_path, f"{filename}.png")
    img.save(output_file)
    print(f"\n{Colors.BLUE}QR Code généré : {output_file}{Colors.ENDC}")

def main():
    print_header()

    # Menu pour choisir la forme
    print_shapes_menu()
    shape_choice = input(f"{Colors.BOLD}\nChoisissez une forme (1-6) : {Colors.ENDC}")

    # Menu pour choisir la couleur
    print_colors_menu()
    color_choice = input(f"{Colors.BOLD}\nChoisissez un style de couleur (1-4) : {Colors.ENDC}")

    # Récupérer les paramètres utilisateur
    url = input(f"\n{Colors.BOLD}Entrez l'URL pour le QR Code : {Colors.ENDC}")
    output_path = input(f"{Colors.BOLD}Entrez le chemin pour sauvegarder le fichier : {Colors.ENDC}")
    filename = input(f"{Colors.BOLD}Entrez le nom du fichier (sans extension) : {Colors.ENDC}")

    # Dictionnaire pour associer les choix aux classes
    module_drawers = {
        "1": SquareModuleDrawer(),
        "2": CircleModuleDrawer(),
        "3": RoundedModuleDrawer(),
        "4": GappedSquareModuleDrawer(),
        "5": VerticalBarsDrawer(),
        "6": HorizontalBarsDrawer(),
    }

    # Déterminer la couleur choisie
    if color_choice == "1":
        color_mask = SolidFillColorMask(front_color=(0, 0, 0))
    elif color_choice == "2":
        color_mask = RadialGradiantColorMask(
            back_color=(255, 255, 255),
            center_color=(0, 0, 255),
            edge_color=(255, 0, 0),
        )
    elif color_choice == "3":
        color_mask = HorizontalGradiantColorMask(
            back_color=(255, 255, 255),
            left_color=(255, 0, 0),
            right_color=(0, 0, 255),
        )
    elif color_choice == "4":
        color_mask = VerticalGradiantColorMask(
            back_color=(255, 255, 255),
            top_color=(0, 255, 0),
            bottom_color=(255, 255, 0),
        )
    else:
        color_mask = SolidFillColorMask(front_color=(0, 0, 0))

    # Générer le QR code avec les choix de l'utilisateur
    generate_custom_qr(
        url,
        output_path,
        filename,
        module_drawers.get(shape_choice, SquareModuleDrawer()),
        color_mask,
    )

if __name__ == "__main__":
    main()

