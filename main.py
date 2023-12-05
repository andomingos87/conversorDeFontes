import os
import subprocess
from fontTools.ttLib import TTFont
from fontTools.ttLib.woff2 import compress

def convert_fonts(input_folder):
    for file in os.listdir(input_folder):
        if file.endswith(".otf") or file.endswith(".ttf"):
            file_path = os.path.join(input_folder, file)
            font = TTFont(file_path)
            
            # Convertendo para TTF se for OTF
            ttf_path = file_path
            if file.endswith(".otf"):
                ttf_path = file_path.replace('.otf', '.ttf')
                font.save(ttf_path)

            # Convertendo para WOFF
            woff_path = file_path.replace('.otf', '.woff').replace('.ttf', '.woff')
            font.flavor = 'woff'
            font.save(woff_path)

            # Convertendo para WOFF2
            woff2_path = file_path.replace('.otf', '.woff2').replace('.ttf', '.woff2')
            compress(ttf_path, woff2_path)

            # Convertendo para EOT
            eot_path = ttf_path.replace('.ttf', '.eot')
            with open(eot_path, 'wb') as eot_file:
                subprocess.run(['ttf2eot', ttf_path], stdout=eot_file)

            print(f'Fonte convertida: {file}')

# Uso da função
convert_fonts('/Users/anderson/Downloads/Trap_/trapfont')
