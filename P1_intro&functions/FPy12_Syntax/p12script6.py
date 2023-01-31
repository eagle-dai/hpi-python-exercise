import score # for local IDE
# This is an unscored bonus script.
# Here, you can run an emacs-compatible linter on your scripts.
# It is not scored as it raises the time from 2 to 6 seconds (for each score run!).
# There will be a separate linter task with clickable line numbers in exercise 1.7

# In Rstudio, VScode etc, linter feedback is integrated (see slides).
# Further exercises will not contain this code, but you may copy it to other scripts :)

from pylint import epylint
lintopt = ["--disable=missing-module-docstring,invalid-name"]
epylint.lint("p12script1.py", options=lintopt)
epylint.lint("p12script2.py", options=lintopt)
epylint.lint("p12script3.py", options=lintopt)
epylint.lint("p12script4.py", options=lintopt)
epylint.lint("p12script5.py", options=lintopt)

# This code does not run on Windows. Use the linter in your IDE :)


# If you want to see your score on openHPI (optional), click Submit after scoring.
# score.score(submit=True) # for local IDE
# Optimally, only mark the code for running it and leave it as a comment.
