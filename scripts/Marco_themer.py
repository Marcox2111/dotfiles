def replace_word_in_file(filename, search_word, replace_word):
    with open(filename, 'r') as file:
        file_contents = file.read()

    new_contents = file_contents.replace(search_word, replace_word)

    with open(filename, 'w') as file:
        file.write(new_contents)


def replace_color_in_file(filename, define_string, new_color):
    with open(filename, 'r') as file:
        file_contents = file.read()

    # Use find to locate the define string
    index = file_contents.find(define_string)
    
    if index == -1:
        print("Define string not found!")
        return

    # Extract the color value
    start_index = index + len(define_string)
    end_index = file_contents.find(';', start_index)
    original_color = file_contents[start_index:end_index].strip()

    # Replace occurrences of the color
    new_contents = file_contents.replace(original_color, new_color)

    with open(filename, 'w') as file:
        file.write(new_contents)

    return original_color  # Return the original color value

filename = "../themes/Gruvbox-Dark-BL/gtk-3.0/gtk.css"
define_string = "@define-color theme_fg_color"
new_color = "#e8d6b9"  # Choose your replacement color here


old_color=replace_color_in_file(filename, define_string, new_color)

filename = "../vscode/equinusocio.vsc-community-material-theme-1.4.6/themes/Community-Material-Theme-Darker.json"
replace_word_in_file(filename, old_color, new_color)

filename = "../themes/Gruvbox-Dark-BL/gtk-4.0/gtk.css"
replace_word_in_file(filename, old_color, new_color)

filename = "../configs/kitty/current-theme.conf"
replace_word_in_file(filename, old_color, new_color)

filename = "../configs/polybar/config.ini"
replace_word_in_file(filename, old_color, new_color)


#f1e8d9
#e8d6b9