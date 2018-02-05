"""
Aerobic Respiration: 1 glucose + 6 oxygen --> 38 ATP

Fermentation: 1 glucose --> 2 ATP
"""

from math import ceil, floor

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

    # If fermentation is more cost effective, just do that
    if ferm_cost_per_atp < resp_cost_per_atp:
        max_atp = money / ferm_cost_per_atp
    else:
        # Respiration is more cost effective - how much glucose ideally?
        glucose_to_buy = money / resp_cost_per_glucose

        # Shall we round up or down?
        glucose_to_buy_up, glucose_to_buy_down = ceil(glucose_to_buy), floor(glucose_to_buy)
        atps = {}
        for glucose_to_buy in [glucose_to_buy_up, glucose_to_buy_down]:
            glucose_budget = glucose_to_buy * glucose_cost
            oxygen_budget = money - glucose_budget
            oxygen_to_buy = floor(oxygen_budget / oxygen_cost)
            money_left = money - (glucose_budget + (oxygen_to_buy * oxygen_cost))
            if money_left >= glucose_cost:
                glucose_to_buy += floor(money_left / glucose_cost)
            glucose_to_respire = min(oxygen_to_buy / 6, glucose_to_buy)

            atp = glucose_to_respire * RESP_ATP
            remaining_glucose = glucose_to_buy - glucose_to_respire
            atp += remaining_glucose * FERM_ATP
            atps[glucose_to_buy] = atp
        glucose_to_buy = max(atps, key=atps.get)
        answers.append(str(atps[glucose_to_buy]) + "\n")

with open("output.txt", "w") as f:
    f.writelines(answers)
