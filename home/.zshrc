# ---------------------
# Paths and Environment
# ---------------------

# Ensure custom paths are added to $PATH
export PATH="$HOME/.local/kitty.app/bin:$PATH"
export PATH="$HOME/.bin:$PATH"
export PATH="$HOME/Documents/NanoProject/STM32MPU/STM32CubeProgrammer/bin:$PATH"

# Oh-my-zsh configuration path
export ZSH="$HOME/.oh-my-zsh"

# Virtualenv configurations
export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
export WORKON_HOME=$HOME/.virtualenvs
source ~/.local/bin/virtualenvwrapper.sh

# fasd initialization
eval "$(fasd --init auto)"

# -----------------
# Oh-My-Zsh Settings
# -----------------

# Theme configuration
ZSH_THEME="bira"

# Plugins to be loaded
plugins=(git)

source $ZSH/oh-my-zsh.sh

# --------------
# FZF Configurations
# --------------

source /usr/share/doc/fzf/examples/key-bindings.zsh
source /usr/share/doc/fzf/examples/completion.zsh

# export FZF_DEFAULT_OPTS="
# --ansi
# --border
# --layout=reverse
# --info=inline
# --height=80
# --preview-window=:hidden
# --preview '

# (catimg -w $COLUMNS {} 2> /dev/null ||

# ([[ -f {} ]] && (bat --style=numbers --color=always {} || cat {})) ||

# ([[ -d {} ]] && (tree -C {} | less)) ||

# echo {} 2> /dev/null) | head -200'

# --bind '?:toggle-preview'"

export FZF_DEFAULT_OPTS="
--ansi
--border
--layout=reverse
--info=inline
--height=80
--preview-window=:hidden
--preview '

(catimg -w $COLUMNS {} 2> /dev/null ||

([[ -f {} ]] && (bat --style=numbers --color=always {} || cat {})) ||

([[ -d {} ]] && (tree -C {} | less)) ||

echo {} 2> /dev/null) | head -200'

--bind '?:toggle-preview'"


# export FZF_CTRL_T_COMMAND='find . \! \( -type d -path ./.git -prune \) \! -type d \! -name '\''*.tags'\'' -printf '\''%P\n'\'''

export FZF_CTRL_T_COMMAND="fdfind -H --color=always --type f --type d --ignore-file .ignorefile"

gdf() {
  preview="git diff $@ --color=always -- {-1}"
  git diff $@ --name-only | fzf -m --ansi --preview $preview
}

# -------------
# Other Settings
# -------------

export MV_HAL_PLUGIN_PATH=:/usr/lib/CenturyArks/hal/plugins

# Aliases
alias ll='exa -l'
alias la='exa -la'
alias fls='ls -A --color=always | fzf --ansi'

