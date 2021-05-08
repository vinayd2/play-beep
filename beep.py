import sys, os

WARNING_BEEP_DURATION = (1000, 2000)

try:
    import winsound

except ImportError:
    import os

    if sys.platform == "darwin":

        def beep(freq, duration):
            # brew install SoX --> install SOund eXchange universal sound sample translator on mac
            # TODO: consider `osascript` and `say` optionally
            os.system(
                f"play -n synth {duration/1000} sin {freq} >/dev/null 2>&1")
    else:

        def beep(freq, duration):
            # apt-get install beep  --> install beep package on linux distros before running
            os.system('beep -f %s -l %s' % (freq, duration))

else:
    def beep(freq, duration):
        winsound.Beep(freq, duration)

beep(WARNING_BEEP_DURATION[0], WARNING_BEEP_DURATION[1])