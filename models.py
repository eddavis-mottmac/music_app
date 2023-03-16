from email.headerregistry import ParameterizedMIMEHeader
import json
import dateutil.parser
import babel
from flask import Flask, render_template, request, Response, flash, redirect, url_for
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
import logging
from logging import Formatter, FileHandler
from flask_wtf import FlaskForm, Form
from forms import *
from flask_migrate import Migrate
import pandas as pd
from forms import *
import logging
import sys


app = Flask(__name__)
app.debug=True
moment = Moment(app)
app.config.from_object('config')
app.app_context().push()
db = SQLAlchemy(app)
migrate = Migrate(app, db)
logging.basicConfig(level=logging.INFO)

class RoomComponent(db.Model):
    __tablename__ = 'room_components'

    area_id = db.Column(db.String(50), primary_key=True)
    room_type = db.Column(db.String(50))
    room_name = db.Column(db.String(50))
    room_function = db.Column(db.String(50))
    reference_documents = db.Column(db.String(100))
    min_room_area = db.Column(db.String(50))
    min_room_length = db.Column(db.Float)
    min_room_width = db.Column(db.Float)
    min_clear_height = db.Column(db.Float)
    adjacencies = db.Column(db.String(100))
    finishes = db.Column(db.String(100))
    comments = db.Column(db.String(100))
    created_on = db.Column(db.DateTime, default=datetime.utcnow)
    created_by = db.Column(db.String(50))
    modified_on = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    modified_by = db.Column(db.String(50))
    status = db.Column(db.String(50))

# TODO: These attributes need to be split into categories for the user to populate
# TODO: Foreign Key to be added
# TODO: Set Default parameters to ones inhertited from RoomComponent, these can be overwritten
# TODO: Set up necessary enums
class Room(db.Model):
    __tablename__ = 'rooms'

    id = db.Column(db.Integer, primary_key=True)
    master_room_id = db.Column(db.Integer)
    specific_room_id = db.Column(db.String(50))
    station_id = db.Column(db.String(50))
    room_type = db.Column(db.String(50))
    room_name = db.Column(db.String(100))
    room_type_acronym = db.Column(db.String(20))
    room_notes = db.Column(db.String(500))
    room_function = db.Column(db.String(100))
    occupied = db.Column(db.Boolean)
    security_rating = db.Column(db.Integer)
    min_length = db.Column(db.Float)
    min_width = db.Column(db.Float)
    min_height = db.Column(db.Float)
    wall_thickness = db.Column(db.Float)
    wall_tolerance = db.Column(db.Float)
    subfloor = db.Column(db.Boolean)
    min_subfloor_height = db.Column(db.Float)
    min_area = db.Column(db.Float)
    max_area = db.Column(db.Float)
    min_volume = db.Column(db.Float)
    max_volume = db.Column(db.Float)
    false_ceiling = db.Column(db.Boolean)
    min_false_ceiling_height = db.Column(db.Float)
    max_false_ceiling_height = db.Column(db.Float)
    min_required_height_above_false_ceiling = db.Column(db.Float)
    sump = db.Column(db.Boolean)
    min_sump_volume = db.Column(db.Float)
    min_sump_length = db.Column(db.Float)
    min_sump_width = db.Column(db.Float)
    min_sump_depth = db.Column(db.Float)
    location_floor = db.Column(db.Integer)
    located_below_ground = db.Column(db.Boolean)
    alternative_level = db.Column(db.Integer)
    screed_required = db.Column(db.Boolean)
    min_screed_depth = db.Column(db.Float)
    floor_flatness = db.Column(db.String(50))
    step_into_room_required = db.Column(db.Boolean)
    height_of_required_step = db.Column(db.Integer)
    step_into_room_allowed = db.Column(db.Boolean)
    skirting = db.Column(db.Boolean)
    wall_cladding_allowance_required = db.Column(db.Boolean)
    wall = db.Column(db.String(50))
    ceiling = db.Column(db.String(50))
    water_tightness = db.Column(db.String(50))
    other_materials_and_finishes = db.Column(db.String(500))
    delivery_route_width = db.Column(db.Float)
    delivery_route_height = db.Column(db.Float)
    delivery_route_depth = db.Column(db.Float)
    max_noise_level = db.Column(db.Integer)
    lifting_beam_required = db.Column(db.Boolean)
    max_temperature = db.Column(db.Float)
    min_temperature = db.Column(db.Float)
    design_temperature = db.Column(db.Float)
    min_relative_humidity = db.Column(db.Integer)
    max_relative_humidity = db.Column(db.Integer)
    ventilation_required = db.Column(db.Boolean)
    min_air_change_capacity = db.Column(db.Float)
    air_supply_rates = db.Column(db.String(50))
    min_air_change_capacity_units = db.Column(db.String(50))
    essential_supply = db.Column(db.Boolean)
    heat_dissipation_load_allowance = db.Column(db.Float)
    envelope_thermal_performance_requirement = db.Column(db.String(50))
    type = db.Column(db.String(50))
    diffuser = db.Column(db.String(50))
    lux = db.Column(db.String(50))
    uniformity = db.Column(db.String(50))
    ip_ik = db.Column(db.String(50))
    detection_type = db.Column(db.String(50))
    stroboscopic_alarm = db.Column(db.Boolean)
    suppression = db.Column(db.Boolean)
    extinguisher = db.Column(db.Boolean)
    separation = db.Column(db.Boolean)
    smoke_extract = db.Column(db.Boolean)
    min_fire_rating_integrity = db.Column(db.Integer)
    min_fire_rating_insulation = db.Column(db.Integer)
    max_escape_distance = db.Column(db.Float)
    max_live_floor_loading = db.Column(db.Float)
    max_wall_loadings = db.Column(db.Float)
    max_ceiling_loading = db.Column(db.Float)
    max_superimposed_dead_loads = db.Column(db.Float)
    exceptional_loads_1 = db.Column(db.Float)
    exceptional_load_area_1 = db.Column(db.Float)
    exceptional_loads_2 = db.Column(db.Float)
    exceptional_load_area_2 = db.Column(db.Float)
    exceptional_loads_3 = db.Column(db.Float)
    exceptional_load_area_3 = db.Column(db.Float)
    blast_loading_considered = db.Column(db.Boolean)
    blast_loading = db.Column(db.Float)
    air_path_loading_considered = db.Column(db.Boolean)
    air_path_loading = db.Column(db.Float)
    min_working_height = db.Column(db.Float)
    min_clearance_front_equipment = db.Column(db.Float)
    clear_width_switchboard_conductor = db.Column(db.Float)
    clear_width_high_pressure_switchboard_conductor = db.Column(db.Float)
    work_surface_height = db.Column(db.Float)
    desk_surface_thickness = db.Column(db.Float)
    clear_space_below_work_surface_width = db.Column(db.Float)
    clear_space_below_work_surface_depth = db.Column(db.Float)
    clear_space_below_work_surface_height = db.Column(db.Float)
    clear_space_in_front_workstation = db.Column(db.Float)
    created_on = db.Column(db.DateTime, default=datetime.utcnow)
    created_by = db.Column(db.String(50))
    modified_on = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    modified_by = db.Column(db.String(50))
    status = db.Column(db.String(50))

class DoorComponent(db.Model):
    __tablename__ = 'door_components'

    door_id = db.Column(db.String(50), primary_key=True)
    door_type = db.Column(db.String(50))
    door_location = db.Column(db.String(50))
    door_width = db.Column(db.Float)
    door_height = db.Column(db.Float)
    door_material = db.Column(db.String(50))
    fire_rating = db.Column(db.String(50))
    acoustic_rating = db.Column(db.String(50))
    thermal_rating = db.Column(db.String(50))
    smoke_rating = db.Column(db.String(50))
    security_rating = db.Column(db.String(50))
    reference_documents = db.Column(db.String(100))
    comments = db.Column(db.String(100))
    created_on = db.Column(db.DateTime, default=datetime.utcnow)
    created_by = db.Column(db.String(50))
    modified_on = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    modified_by = db.Column(db.String(50))
    status = db.Column(db.String(50))

class Door(db.Model):
    __tablename__ = 'doors'

    door_number = db.Column(db.String(50), primary_key=True)
    door_type = db.Column(db.String(50))
    clear_opening_required = db.Column(db.String(50))
    direction_of_swing = db.Column(db.String(50))
    fire_resistance = db.Column(db.String(50))
    air_resistance = db.Column(db.String(50))
    stc_rating = db.Column(db.String(50))
    lock_function = db.Column(db.String(50))
    accessories_1 = db.Column(db.String(50))
    accessories_2 = db.Column(db.String(50))
    accessories_3 = db.Column(db.String(50))
    eacs_security_level = db.Column(db.String(50))
    room_space_id = db.Column(db.String(50))
    reference_documents = db.Column(db.String(100))
    comments = db.Column(db.String(100))
    created_on = db.Column(db.DateTime, default=datetime.utcnow)
    created_by = db.Column(db.String(50))
    modified_on = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    modified_by = db.Column(db.String(50))
    status = db.Column(db.String(50))

class EquipmentComponent(db.Model):
    __tablename__ = 'equipment_components'

    item_id = db.Column(db.String(50), primary_key=True)
    name = db.Column(db.String(50))
    category = db.Column(db.String(50))
    description = db.Column(db.String(100))
    datasheet_link = db.Column(db.String(100))
    reference_documents = db.Column(db.String(100))
    comments = db.Column(db.String(100))
    created_on = db.Column(db.DateTime, default=datetime.utcnow)
    created_by = db.Column(db.String(50))
    modified_on = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    modified_by = db.Column(db.String(50))
    status = db.Column(db.String(50))

class Equipment(db.Model):
    __tablename__ = 'equipment'
    asset_id = db.Column(db.String(50), primary_key=True)
    room_id = db.Column(db.String(50), db.ForeignKey('room.area_id'))
    item_id = db.Column(db.String(50), db.ForeignKey('equipment.item_id'))
    equipment_type = db.Column(db.String(50))
    created_on = db.Column(db.DateTime, default=datetime.utcnow)
    created_by = db.Column(db.String(50))
    modified_on = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    modified_by = db.Column(db.String(50))
    status = db.Column(db.String(50))

    room = db.relationship('Room', backref='equipment_assets')
    equipment_component = db.relationship('EquipmentComponent', backref='equipment_assets')