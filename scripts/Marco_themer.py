import argparse
import os
import re
import shutil

def invert_color(color):
    """Invert a color code."""
    # Ensure the color starts with #
    if not color.startswith("#"):
        return color

    # Convert the 6-character color code into RGB values
    r = int(color[1:3], 16)
    g = int(color[3:5], 16)
    b = int(color[5:7], 16)

    # Calculate the inverted colors
    inv_r = 255 - r
    inv_g = 255 - g
    inv_b = 255 - b

    # Convert the RGB values back into a color code format
    inverted_color = "#{:02X}{:02X}{:02X}".format(inv_r, inv_g, inv_b)
    
    return inverted_color

def adjust_relative_color(color, old_bg, new_bg):
    """Adjust color to maintain its relative distance from the new background."""

    if not color.startswith("#"):
        return color

    # Extract RGB values
    r = int(color[1:3], 16)
    g = int(color[3:5], 16)
    b = int(color[5:7], 16)

    old_bg_r = int(old_bg[1:3], 16)
    old_bg_g = int(old_bg[3:5], 16)
    old_bg_b = int(old_bg[5:7], 16)

    new_bg_r = int(new_bg[1:3], 16)
    new_bg_g = int(new_bg[3:5], 16)
    new_bg_b = int(new_bg[5:7], 16)

    # Calculate relative distances
    r_dist = (r - old_bg_r) / (255 - old_bg_r)
    g_dist = (g - old_bg_g) / (255 - old_bg_g)
    b_dist = (b - old_bg_b) / (255 - old_bg_b)

    # Calculate adjusted colors
    adj_r = round(new_bg_r + r_dist * (255 - new_bg_r))
    adj_g = round(new_bg_g + g_dist * (255 - new_bg_g))
    adj_b = round(new_bg_b + b_dist * (255 - new_bg_b))

    adjusted_color = "#{:02X}{:02X}{:02X}".format(adj_r, adj_g, adj_b)

    return adjusted_color

def backup_and_invert_colors_in_files(files_to_modify,old_bg,new_bg):
    color_pattern = re.compile(r'#[0-9a-fA-F]{6}')

    for file_path in files_to_modify:
        # Backup the file
        backup_path = file_path + ".backup"
        shutil.copy(file_path, backup_path)

        with open(file_path, 'r') as file:
            contents = file.read()

        # Find and replace all color codes
        new_contents = color_pattern.sub(lambda match: invert_color(match.group()), contents)

        # Write the updated content back to the original file
        with open(file_path, 'w') as file:
            file.write(new_contents)

def replace_word_in_file(filename, search_word, replace_word):
    with open(filename, 'r') as file:
        file_contents = file.read()

    new_contents = file_contents.replace(search_word, replace_word)

    with open(filename, 'w') as file:
        file.write(new_contents)


def find_color_in_file(filename, define_string):
    with open(filename, 'r') as file:
        file_contents = file.read()

    # Use find to locate the define string
    index = file_contents.find(define_string)
    
    if index == -1:
        print("Define string not found!")
        return None

    # Extract the color value
    start_index = index + len(define_string)
    end_index = file_contents.find(';', start_index)
    original_color = file_contents[start_index:end_index].strip()

    return original_color  # Return both the original and new color values

def main(theme):
    files_to_modify = [
        "../themes/Gruvbox-Dark-BL/gtk-3.0/gtk.css",
        "../vscode/equinusocio.vsc-community-material-theme-1.4.6/themes/Community-Material-Theme-Darker.json",
        "../themes/Gruvbox-Dark-BL/gtk-4.0/gtk.css",
        "../configs/kitty/current-theme.conf",
        "../configs/polybar/config.ini",
        "../configs/dunst/dunstrc"
    ]
    filename = "../themes/Gruvbox-Dark-BL/gtk-3.0/gtk.css"
    fg_string = "@define-color theme_fg_color"
    bg_string = "@define-color theme_bg_color"

    old_fg_color = find_color_in_file(filename, fg_string)
    old_bg_color = find_color_in_file(filename, bg_string)

    if theme == "swap":
        backup_and_invert_colors_in_files(files_to_modify,old_bg_color,old_fg_color)
        
    else:

        print(f"Original foreground color found: {old_fg_color}")
        print(f"Original background color found: {old_bg_color}")
        print(f"DON'T SWAP THE COLORS IN THIS WAY INSTEAD USE: --theme swap")
        new_fg_color = input("Enter the new foreground color you want to replace with: ")
        new_bg_color = input("Enter the new background color you want to replace with: ")

        for file in files_to_modify:
            replace_word_in_file(file, old_fg_color, new_fg_color)
            replace_word_in_file(file, old_bg_color, new_bg_color)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Modify theme based on input parameter (swap).")
    parser.add_argument('--theme', type=str, choices=['swap'], default=None, help="For now you can just swap.")

    args = parser.parse_args()

    main(args.theme)


#f1e8d9
#e8d6b9