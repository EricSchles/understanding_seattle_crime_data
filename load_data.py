import pandas as pd
from app.models import SeattleCrimeData
from app import db
from datetime import datetime

df = pd.read_csv("Seattle_Police_Department_911_Incident_Response.csv")

for i in df.index:
    data = SeattleCrimeData(
        cad_cdw_id=str(df.ix[i]["CAD CDW ID"]),
        cad_event_number=str(df.ix[i]["CAD Event Number"]),
        general_offense_number=str(df.ix[i]["General Offense Number"]),
        event_clearance_code=str(df.ix[i]["Event Clearance Code"]),
        event_clearance_description=str(df.ix[i]["Event Clearance Description"]),
        event_clearance_subgroup=str(df.ix[i]["Event Clearance SubGroup"]),
        event_clearance_group=str(df.ix[i]["Event Clearance Group"]),
        event_clearance_date=datetime.strptime(df.ix[i]["Event Clearance Date"], "%m/%d/%Y %I:%M:%S %p"),
        hundred_block_location=str(df.ix[i]["Hundred Block Location"]),
        district_sector=str(df.ix[i]["District/Sector"]),
        zone_beat=str(df.ix[i]["Zone/Beat"]),
        census_tract=str(df.ix[i]["Census Tract"]),
        longitude=df.ix[i]["Longitude"],
        latitude=df.ix[i]["Latitude"],
        incident_location=str(df.ix[i]["Incident Location"]),
        initial_type_description=str(df.ix[i]["Initial Type Description"]),
        initial_type_subgroup=str(df.ix[i]["Initial Type Subgroup"]),
        initial_type_group=str(df.ix[i]["Initial Type Group"]),
        at_scene_time=datetime.now()
        )
    db.session.add(data)
    db.session.commit()
