# .bash_profile

# Get the aliases and functions
[ -f $HOME/.bashrc ] && . $HOME/.bashrc


if [ -z "$DISPLAY" ]; then
    export XKB_DEFAULT_LAYOUT=us  
    export XKB_DEFAULT_VARIANT=dvorak
#    export XKB_DEFAULT_MODEL=pc101
    export XKB_DEFAULT_OPTIONS=caps:escape,altwin:prtsc_rwin
    sway #-d 2> ~/sway.log
fi
