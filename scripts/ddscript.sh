#!/bin/bash

if xdotool search --name "dropdown" 2>/dev/null; then
  i3-msg [title="dropdown"] scratchpad show
  #i3-msg [title="dropdown"] move position center
else
    kitty -T dropdown --detach -e tmux new-session -s dropdown &
    while ! xdotool search --name "dropdown" 2>/dev/null; do
        sleep 0.1
    done  
  i3-msg [title="dropdown"] scratchpad show
  #i3-msg [title="dropdown"] move position center
fi

exit 0