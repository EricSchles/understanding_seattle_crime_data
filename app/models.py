"""
Here the models for our database is defined.

I am using Postgres, Flask-SQLAlchemy for this application.

For an introduction to Flask-SQLAlchemy check out: http://flask-sqlalchemy.pocoo.org/2.1/

__init__ function for each model is a constructor, and is necessary to enter
""" 
from app import db
from datetime import datetime

class SeattleCrimeData(db.Model):
    """
    This model gives us a database version of all the data in Seattle_Police_Department_911_Incident_Response.csv from: https://data.seattle.gov/Public-Safety/Seattle-Police-Department-911-Incident-Response/3k2p-39jp
    
    To understand the types checkout: https://dev.socrata.com/foundry/data.seattle.gov/pu5n-trf4
    There doesn't appear to be a data dictionary for this dataset.  Making deductions about specific datapoints hard.
    In lue of a data dictionary, I will likely have to build one over time.
    parameters:
    
    ID information:
    @cad_cdw_id -
    @cad_event_number -
    
    About what happened:
    @general_offense_number - 
    @event_clearance_code - 
    @event_clearance_description - 
    @event_clearance_subgroup - 
    @event_clearance_group -
    
    When it happened:
    @event_clearance_date -

    Where it happened:
    @hundred_block_location -  
    @district_sector - 
    @zone_beat - 
    @census_tract - 
    @longitude - 
    @latitude - 
    @incident_location - a "point" data type in geojson parlance.  We'll treat this is a json blob, rendering on the front end, if needed.
    
    Further descriptive information:
    @initial_type_description - 
    @initial_type_subgroup - 
    @initial_type_group - 
    @at_scene_time - 

    functions:
    __str__ - 
    """
    __tablename__ = 'seattle_crime_data'
    id = db.Column(db.Integer, primary_key=True)
    cad_cdw_id = db.Column(db.String)
    cad_event_number = db.Column(db.String)
    general_offense_number = db.Column(db.String)
    event_clearance_code = db.Column(db.String)
    event_clearance_description = db.Column(db.String)
    event_clearance_subgroup = db.Column(db.String)
    event_clearance_group = db.Column(db.String)
    event_clearance_date = db.Column(db.DateTime)
    hundred_block_location = db.Column(db.String)
    district_sector = db.Column(db.String)
    zone_beat = db.Column(db.String)
    census_tract = db.Column(db.String)
    longitude = db.Column(db.Integer)
    latitude = db.Column(db.Integer)
    incident_location = db.Column(db.String)
    initial_type_description = db.Column(db.String)
    intitial_type_subgroup = db.Column(db.String)
    initial_type_group = db.Column(db.String)
    at_scene_time = db.Column(db.DateTime)
    incident_location_state = db.Column(db.String)
    incident_location_address = db.Column(db.String)
    incident_location_zip = db.Column(db.String)
    incident_location_city = db.Column(db.String)

    
    def __init__(
            self,
            cad_cdw_id="",
            cad_event_number="",
            general_offense_number="",
            event_clearance_code="",
            event_clearance_description="",
            event_clearance_subgroup="",
            event_clearance_group="",
            event_clearance_date=datetime.now(),
            hundred_block_location="",
            district_sector="",
            zone_beat="",
            census_tract="",
            longitude=0.0,
            latitude=0.0,
            incident_location="",
            initial_type_description="",
            initial_type_subgroup="",
            initial_type_group="",
            at_scene_time=datetime.now(),
            incident_location_state="",
            incident_location_address="",
            incident_location_zip="",
            incident_location_city=""
    ):
        self.cad_cdw_id = cad_cdw_id
        self.cad_event_number = cad_event_number
        self.general_offense_number = general_offense_number
        self.event_clearance_code = event_clearance_code
        self.event_clearance_description = event_clearance_description
        self.event_clearance_subgroup = event_clearance_subgroup
        self.event_clearance_group = event_clearance_group
        self.event_clearance_date = event_clearance_date
        self.hundred_block_location = hundred_block_location
        self.district_sector = district_sector
        self.zone_beat = zone_beat
        self.census_tract = census_tract
        self.longitude = longitude
        self.latitude = latitude
        self.incident_location = incident_location
        self.initial_type_description = initial_type_description
        self.intitial_type_subgroup = intitial_type_subgroup
        self.initial_type_group = initial_type_group
        self.at_scene_time = at_scene_time
        self.incident_location_state = incident_location_state
        self.incident_location_address = incident_location_address
        self.incident_location_zip = incident_location_zip
        self.incident_location_city = incident_location_city
        
    def __str__(self):
        return "<cad_cdw_id: {}, cad_event_number:{}>".format(self.cad_cdw_id,self.cad_event_number)

