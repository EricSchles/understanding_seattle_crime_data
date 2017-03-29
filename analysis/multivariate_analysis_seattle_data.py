import numpy as np
import pandas as pd
import statsmodels.api as sm
from scipy import stats
import matplotlib.pyplot as plt
from statsmodels.graphics.api import qqplot
import time
from sklearn.svm import SVR
from sklearn.neighbors import KNeighborsRegressor
from functools import partial

df = pd.read_csv("Seattle_Police_Department_911_Incident_Response.csv")

df["Event Clearance Date"] = pd.to_datetime(df["Event Clearance Date"], format="%m/%d/%Y %I:%M:%S %p")

def zone_to_int(zone_mapping,zone):
    return zone_mapping[zone]

def get_hour(ts):
    return ts.hour

def crime_severity(description):
    description = description.strip()
    #severity increases with magnitude
    zero = [
        "TRAFFIC RELATED CALLS",
        "MISCELLANEOUS MISDEMEANORS",
        "NUISANCE, MISCHIEF",
        "PUBLIC GATHERINGS",
        "BIKE",
        "ANIMAL COMPLAINTS",
        "FRAUD CALLS",
        "OTHER PROPERTY",
        "PROPERTY - MISSING, FOUND",
        "LIQUOR VIOLATIONS",
        "DISTURBANCES",
        "SHOPLIFTING"
    ]
    #non violent
    one = [
        "MENTAL HEALTH",
        "BEHAVIORAL HEALTH",
        "FALSE ALARMS",
        "FALSE ALACAD"
    ]
    two = [
        "DRIVE BY (NO INJURY)", # I'm not 100% sure what this is...
        "PROPERTY DAMAGE",
        "TRESPASS",
        "BURGLARY",
        "ROBBERY",
        "HARBOR CALLS",
        "RECKLESS BURNING",
        "LEWD CONDUCT",
        "AUTO THEFTS",
        "SUSPICIOUS CIRCUMSTANCES",
        "FAILURE TO REGISTER (SEX OFFENDER)",
        "PROPERTY - MISSING, FOUND",
        "PERSONS - LOST, FOUND, MISSING"
    ]
    three = [
        "WEAPONS CALLS",
        "MOTOR VEHICLE COLLISION INVESTIGATION",
        "THREATS",
        "THREATS, HARASSMENT",
        "ACCIDENT INVESTIGATION",
        "PROWLER",
        "CAR PROWL",
        "NARCOTICS COMPLAINTS"
    ]
    four = [
        "VICE CALLS",
        "OTHER VICE",
        "ASSAULTS",
        "ARREST",
        "HAZARDS",
        "PROSTITUTION",
    ]
    five = [
        "HOMICIDE",
        "PERSON DOWN/INJURY"
    ]
    zero = [elem.lower() for elem in zero]
    one = [elem.lower() for elem in one]
    two = [elem.lower() for elem in two]
    three = [elem.lower() for elem in three]
    four = [elem.lower() for elem in four]
    five = [elem.lower() for elem in five]
    if description.lower() in zero:
        return 0.0
    elif description.lower() in one:
        return 1.0
    elif description.lower() in two:
        return 2.0
    elif description.lower() in three:
        return 3.0
    elif description.lower() in four:
        return 4.0
    elif description.lower() in five:
        return 5.0
    else:
        #for debugging
        return description

zones = ['CCD', 'J1', 'B3', 'L2', 'F2', 'B2', 'LS', 'WP', 'B1', 'Q2', 'MS', 'R3', 'W', 'BS', 'TAC3', 'H2', 'U1', 'QS', 'W1', 'Q3', 'RS', 'LAPT', 'E', 'C3', 'CTY', 'K3', 'G1', 'ES', 'TRF', 'EP', 'L3', 'E3', 'INV', 'SCTR1', 'O1', 'NS', 'R1', 'D3', 'N2', 'CS', 'M2', 'US', 'DET', 'EDD', 'WS', 'SS', 'D1', 'C2', 'J2', '99', 'R2', 'C1', 'J3', 'U3', 'K2', 'NP', 'E1', 'S1', 'S', 'GS', 'W2', 'SP', 'KS', 'K1', 'S2', 'S3', 'DS', 'G2', 'M3', 'N', 'E2', 'HS', 'F3', 'N1', 'F1', 'FS', 'OS', 'JS', 'U2', 'N3', 'Q1', 'O3', 'H3', 'W3', 'G3', 'KCIO07', 'L1', 'M1', 'D2', 'O2', 'COMM']
zone_mapping = {}.fromkeys(zones,0)
zone_mapping = {key:index for index,key in enumerate(zone_mapping.keys())}

print("got rid of nulls")
df = df[pd.notnull(df["Event Clearance Group"])]
df = df[pd.notnull(df["Zone/Beat"])]
df["hour"] = df["Event Clearance Date"].apply(get_hour)
print("created hour column")
df["crime_severity"] = df["Event Clearance Group"].apply(crime_severity)
print("created crime severity column")
zone_map = partial(zone_to_int,zone_mapping)
print("created zone map")
df["zone_int"] = df["Zone/Beat"].apply(zone_map)
print("created zone column")
Y = "crime_severity"
X = ["hour","zone_int"]

scores = []
for neighbor in range(1,5):
    msk = np.random.rand(len(df)) < 0.8
    train = df[msk]
    train = train.dropna()
    test = df[~msk]
    test = test.dropna()
    X_train = train[X]
    X_test = test[X]
    Y_train = train[Y]
    Y_test = test[Y]

    neigh = KNeighborsRegressor(n_neighbors=neighbor)
    neigh.fit(X_train, Y_train)
    scores.append(neigh.score(X_test, Y_test))

for index,score in enumerate(scores):
    print("K:",index,"Score",score)

msk = np.random.rand(len(df)) < 0.8
train = df[msk]
test = df[~msk]
train = train.dropna()
test = test.dropna()
X_train = train[X]
X_test = test[X]
y_train = train[Y]
y_test = test[Y]
clf = SVR()
print("got to train svr")
clf.fit(X_train, y_train)
print("finished fitting svr")
print("SVM linear score",clf.score(X_test, y_test))
# model = sm.OLS(y, X)
# result = model.fit()
# print(result.summary())
# # Plot outputs
# fig, ax = plt.subplots(figsize=(8,6))
# res = result
# ax.plot(X, y, 'o', label="data")
# ax.plot(X, res.fittedvalues, 'r--.', label="OLS")
# ax.legend(loc='best');
# plt.show()
