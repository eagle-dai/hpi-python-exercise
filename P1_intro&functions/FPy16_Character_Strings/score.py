'''This enables scoring while working on the exercise in Rstudio,
without leaving the Python execution environment.'''

# Scoring in the browser takes ca 2.1 seconds.
# Scoring locally through     import score ; score.score()     takes 2.9 seconds.

# You could also have a second Rstudio open with something like
# codeoceanR::rt_score("C:/Dropbox/kurs/py_exercises_solved/FPy12_Syntax")
# Then scoring takes 2.0 seconds only, but is in a separate window.


# If anybody has a better approach (keyboard shortcut? VScode?), please let me know!

# PS: codeoceanR::rt_score() is complicated, it is highly unlikely that I will
# implement it in Python. See the source code at
# https://github.com/openHPI/codeoceanR/blob/main/R/rt_score.R

import subprocess
import os
import platform
import glob
def score(submit=False):
    '''Send code to CodeOcean, run scoring script, display results'''
## DO NOT RUN IN CODEOCEAN BROWSER INSTANCE ####################################
    if os.getenv("CODEOCEAN")=="true":
        return
    dn = subprocess.DEVNULL
## LOCAL SCORING IN TASK DEVELOPMENT ON BERRYS COMPUTER ########################
    if os.getcwd() == "C:\\Dropbox\\R\\kurs\\py_exercises":
        fn = glob.glob('*testrun.py')[-1] # last testrun file name
        print("----- Locally running python", fn, "-----")
        cmd = f"python {fn}"
        # needs a separate python call due to caching in Rstudio
        sc = subprocess.run(cmd, shell=True, capture_output=True, stdin=dn, text=True)
        print(sc.stdout.rstrip())
        return
## REGULAR STUDENT CALL ########################################################
    if submit:
        cmd = "codeoceanR::rt_submit(confirm=FALSE)"
    else:
        cmd = "codeoceanR::rt_score()"
    if platform.system() != "Windows": # At least on Mac, Linux untested
        cmd = f"'{cmd}'"
    cmd = f"R -e {cmd}"
    sc = subprocess.run(cmd, shell=True, capture_output=True, stdin=dn, text=True)
    print(sc.stderr)
    return
