import score # for local IDE
# T4 ----
# Implement the Disaster START triage (Simple Triage and Rapid Treatment)
# categorization according to the p24triage.png flowchart.
# (obtained from https://www.uptodate.com/contents/image?imageKey=OBGYN%2F129155)
# 'triage' should return one of these categories:
# "EXPECTANT", "IMMEDIATE", "DELAYED", "MINOR"
# Edge cases in numerical comparisons (resp_rate=30, cap_refill=2) are not tested.
# Do not change the order of the parameters.
# Hint: conditional returns make code readable and maintainable = writeable
# I provided documentation for the function as commonly written in a multiline comment
# at the top of the function (docstring) that explains the parameters and arguments.
def triage(can_walk, breathing, br_repos, resp_rate, pulse, cap_refill, commands):
    """categorize disaster victims according to START triage 
    
    Parameters
    ----------
    can_walk   : bool
    breathing  : bool
    br_repos   : bool         # is there spontaneous breathing after repositioning airway?
    resp_rate  : int          # respiratory rate [number of breaths per minute]
    pulse      : str          # radial pulse: "present", "absent" or "NA"
    cap_refill : int or float # capillary refill [in seconds]
    commands   : bool         # are simple commands followed?

    Returns
    ------
    category : str
    """
    category = "CAT"
    return category

print("t1", triage(True , True , True , 24, "present", 3, True )) # MINOR
print("t2", triage(False, False, False, 00, "absent" , 0, False)) # EXPECTANT
print("t3", triage(False, False, True , 35, "absent" , 4, False)) # IMMEDIATE
print("t4", triage(False, True , True , 22, "present", 1, False)) # IMMEDIATE
print("t5", triage(False, True , True , 19, "present", 1, True )) # DELAYED

score.score() # for local IDE

# If you want to see your score on openHPI, click Submit after scoring.
# score.score(submit=True) # for local IDE
