import os
from PIL import Image, ImageDraw, ImageFont

# Demande à l'utilisateur de saisir le chemin d'accès du dossier à parcourir
folder_path = input("Enter the folder path: ")

# Demande à l'utilisateur de saisir l'option pour le watermark
option = input("Enter the watermark option (1'default settings' or 2'Custom settings'): ")

if option == "1":
    watermark_text = input("Enter watermark text: ")

    #Creation du dossier pour mettre les photos avec watermark
    output_folder = os.path.join(folder_path, "watermarked")
    if not os.path.exists(output_folder):
        os.mkdir(output_folder)

    #Parcours des fichiers
    for filename in os.listdir(folder_path):
        filepath = os.path.join(folder_path, filename)

        #Image ?
        if not filepath.endswith(".jpg") and not filepath.endswith(".png"):
            continue

        #Open image
        image = Image.open(filepath)

        #Ajout du watermark
        draw = ImageDraw.Draw(image)
        font_path = "/System/Library/Fonts/Supplemental/Arial Black.ttf"
        font_size = int(image.width / 10)
        font = ImageFont.truetype(font_path, font_size)
        text_width, text_height = draw.textsize(watermark_text, font=font)
        draw.text(((image.width - text_width) / 2, (image.height - text_height) / 2), watermark_text, fill=(255, 255, 255, 128), font=font)

        #CTRL+S image
        new_filename = os.path.join(output_folder, filename)
        image.save(new_filename)

    print("Watermark successfully added to images in the folder.")
    
elif option == "2":
    #Renseignement des paramétres
    watermark_text = input("Enter watermark text: ")
    watermark_color = input("Enter watermark color (in RGB, separated by commas): ")
    font_path = input("Enter path: ")
    watermark_opacity = int(input("Enter watermark opacity (between 0 and 255): "))

    output_folder = os.path.join(folder_path, "watermarked")
    if not os.path.exists(output_folder):
        os.mkdir(output_folder)

    for filename in os.listdir(folder_path):
        filepath = os.path.join(folder_path, filename)

        if not filepath.endswith(".jpg") and not filepath.endswith(".png"):
            continue

        image = Image.open(filepath)

        draw = ImageDraw.Draw(image)
        font_size = int(image.width / 10)
        font = ImageFont.truetype(font_path, font_size)

        # Conversion de la couleur du watermark en tuple RGB
        watermark_color = tuple(map(int, watermark_color.split(",")))

        text_width, text_height = draw.textsize(watermark_text, font=font)
        draw.text(((image.width - text_width) / 2, (image.height - text_height) / 2), watermark_text, fill=(*watermark_color, watermark_opacity), font=font)

        # Enregistrement de l'image modifiée dans le nouveau dossier
        new_filename = os.path.join(output_folder, filename)
        image.save(new_filename)

    print("Watermark successfully added to images in the folder.)
