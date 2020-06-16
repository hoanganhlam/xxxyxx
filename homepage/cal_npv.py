import numpy_financial as np
from .yfinance_api import *
from .models import sStock

# average NPV from different areas source from Evaluate


def avg_npv(area):
    switcher = {
        'Oncology': [620.6349206],
        'Central Nervous System': [397.6190476],
        'Musculoskeletal': [883.3333333],
        'Cardiovascular': [294.7368421],
        'Immunomodulators': [1085.185185],
        'Respiratory': [2006.25],
        'Gastro-Intestinal': [708.3333333],
        'Systemic Anti-infectives': [162.745098],
        'Blood': [971.4285714],
        'Sensory Organs': [793.3333333],
        'Dermatology': [310.5263158],
        'Endocrine': [409.0909091],
        'Genito-Urinary': [37.5],
        'Various': [124.137931]
    }
    return switcher.get(area, "Invalid")

# average development cost for different areas, from Evaluate


def avg_cost(area):
    switcher = {
        'Oncology': float(723.015873),
        'Central Nervous System': float(738.0952381),
        'Musculoskeletal': float(829.1666667),
        'Cardiovascular': float(1036.842105),
        'Immunomodulators': float(555.5555556),
        'Respiratory': float(575),
        'Gastro-Intestinal': float(350),
        'Systemic Anti-infectives': float(160.7843137),
        'Blood': float(304.7619048),
        'Sensory Organs': float(326.6666667),
        'Dermatology': float(205.2631579),
        'Endocrine': float(354.5454545),
        'Genito-Urinary': float(250),
        'Various': float(141.3793103)
    }
    return switcher.get(area, "Invalid")

# Cashflow is generated by adding avg_cost for therapeutic area by average cost for trials and
# adding average npv for a specific area


def generate_cashflow(Phase, npv, avg_cost):
    switcher = {
        'Phase 1': [-0.09 * avg_cost, -0.09 * avg_cost] + [-0.2 * avg_cost, -0.2 * avg_cost, -0.2 * avg_cost, -0.2 * avg_cost] + [-1] + npv,
        'Phase 1/Phase 2': [-0.2 * avg_cost, -0.2 * avg_cost, -0.2 * avg_cost, -0.2 * avg_cost] + [-1] + npv,
        'Phase 2': [-0.2 * avg_cost, -0.2 * avg_cost, -0.2 * avg_cost, -0.2 * avg_cost] + [-1] + npv,
        'Phase 2/Phase 3': [-1] + npv,
        'Phase 3': [-1] + npv,
        'PDUFA': npv,
        'BLA': npv
    }
    return switcher.get(Phase, "Invalid")

# calculate net present value


def cal_npv(cashflows):
    discountRate = 0.11  # Nine percent per annum
    npv = np.npv(discountRate, cashflows)

    return npv


##################sample code########################################################################
# cal_npv requires 2 informations, the clinical stage and the therapeutic area of the drug
# print(cal_npv(generate_cashflow('Phase 3', avg_npv(
#     'Respiratory'), avg_cost('Respiratory'))))


# functions for calculation upside and downside of companies


# npv = cal_npv(generate_cashflow(phase, avg_npv(area), avg_cost(area))
# EV = get_EV(symbol)
# netcash = get_cash(symbol)
# thay marketCap = EV


def calculate_downside(EV, netcash):
    if EV > 0:
        if netcash > EV:
            return 0
        else:
            return round((EV - netcash) / EV, 2)
    else:
        return 0


def calculate_upside(EV, npv):
    if EV > 0:
        if (npv - EV) / EV <= 0:
            return 0
        else:
            round((npv - EV) / EV, 2)
    else:
        if (npv + abs(EV)) / abs(EV) <= 0:
            return 0
        else:
            return round((npv + abs(EV)) / abs(EV), 0)







#Example code###############################
#print(calculate_upside(get_EV('ADMS'),cal_npv(generate_cashflow('Phase 3', avg_npv('Central Nervous System'), avg_cost('Central Nervous System')))))
# print(calculate_downside(get_EV('ADMS'), get_cash('ADMS')))
# print(get_cash('ADMS')[1])
#print(cal_npv(generate_cashflow('Phase 3', avg_npv('Central Nervous System'), avg_cost('Central Nervous System'))))
# print(get_EV('ADMS'))
