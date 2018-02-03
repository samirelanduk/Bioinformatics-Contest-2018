"""
Aerobic Respiration: 1 glucose + 6 oxygen --> 38 ATP

Fermentation: 1 glucose --> 2 ATP
"""

RESP_ATP = 38
FERM_ATP = 2

with open("input.txt") as f:
    lines = [line.rstrip() for line in f]

answers = []
for line in lines[1:]:
    glucose_cost, oxygen_cost, money = [int(val) for val in line.split()]

    # How much does it cost to do resperation per mol of glucose?
    resp_cost_per_glucose = glucose_cost + (6 * oxygen_cost)

    # How much does each mole of ATP cost to make via respiration?
    resp_cost_per_atp = resp_cost_per_glucose / RESP_ATP

    # How much does each mole of ATP cost to make via fermentation?
    ferm_cost_per_atp = glucose_cost / FERM_ATP

    # Which is more cost effective?
    if resp_cost_per_atp > ferm_cost_per_atp:
        # Fermentation is more cost effective
        max_atp = money / ferm_cost_per_atp
    else:
        # Respiration is more effective
        max_atp = money / resp_cost_per_atp
    answers.append(str(max_atp) + "\n")

with open("output.txt", "w") as f:
    f.writelines(answers)
