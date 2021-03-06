# -*- coding: utf-8 -*-
### required - do no delete
from datetime import date

def user(): return dict(form=auth())
def download(): return response.download(request,db)
def call(): return service()
### end requires
def index():
	return dict()

def error():
    return dict()

@auth.requires_login()
def building_manage():
    return dict()

@auth.requires_login()
def floor_manage():
    return dict()

@auth.requires_login()
def apartment_manage():
    return dict()

@auth.requires_login()
def apartment_type_manage():
    return dict()

@auth.requires_login()
def user_info_manage():
    return dict()

@auth.requires_login()
def contract_manage():
    return dict()

@auth.requires_login()
def semester_manage():
    return dict()

@auth.requires_login()
def parking_manage():
    return dict()

@auth.requires_login()
def request_manage():
    return dict()

@auth.requires_login()
def request_comments_manage():
    return dict()

@auth.requires_login()
def request_type_manage():
    return dict()

@auth.requires_login()
def room_manage():
    return dict()

@auth.requires_login()
def room_type_manage():
    return dict()

def contract():
    #form = SQLFORM.factory(db.t_user_info)
    #form += SQLFORM.factory(db.t_apartment)
    #form += SQLFORM.factory(db.t_building)
    return dict(year=(date.today().year))

#  NOT FINISHED
# this function is to display a contract in a printable format
def display_full_contract(id):
    return

# About us page
def about():
	return dict()

# Contact page
def contact():
	return dict()

@auth.requires_login()
def t_building_manage():
    form = SQLFORM(db.t_building)
    if form.process().accepted:
        response.flash = 'form accepted';
    elif form.errors:
        response.flash = 'form has errors'
    else:
        response.flash = 'please fill out the form'
    return dict(form=form)

@auth.requires_login()
def t_floor_manage():
    form = SQLFORM(db.t_floor)
    if form.process().accepted:
        response.flash = 'form accepted';
    elif form.errors:
        response.flash = 'form has errors'
    else:
        response.flash = 'please fill out the form'
    return dict(form=form)

@auth.requires_login()
def t_apartment_manage():
    form = SQLFORM(db.t_apartment)
    # .smartgrid(db.t_t_building,onupdate=auth.archive)
    if form.process().accepted:
        response.flash = 'form accepted';
    elif form.errors:
        response.flash = 'form has errors'
    else:
        response.flash = 'please fill out the form'
    return dict(form=form)

@auth.requires_login()
def t_apartment_type_manage():
    form = SQLFORM(db.t_apartment_type)
    if form.process().accepted:
        response.flash = 'form accepted';
    elif form.errors:
        response.flash = 'form has errors'
    else:
        response.flash = 'please fill out the form'
    return dict(form=form)


@auth.requires_login()
def t_user_info_manage():
    form = SQLFORM(db.t_user_info)
    return form

@auth.requires_login()
def t_contract_manage():
    form = SQLFORM(db.t_contract)
    # .smartgrid(db.t_t_building,onupdate=auth.archive)
    if form.process().accepted:
        response.flash = 'form accepted';
    elif form.errors:
        response.flash = 'form has errors'
    else:
        response.flash = 'please fill out the form'
    return dict(form=form)

@auth.requires_login()
def t_semester_manage():
    form = SQLFORM(db.t_semester)
    # .smartgrid(db.t_t_building,onupdate=auth.archive)
    if form.process().accepted:
        response.flash = 'form accepted';
    elif form.errors:
        response.flash = 'form has errors'
    else:
        response.flash = 'please fill out the form'
    return dict(form=form)


@auth.requires_login()
def t_parking_manage():
    form = SQLFORM(db.t_parking)
    # .smartgrid(db.t_t_building,onupdate=auth.archive)
    if form.process().accepted:
        response.flash = 'form accepted';
    elif form.errors:
        response.flash = 'form has errors'
    else:
        response.flash = 'please fill out the form'
    return dict(form=form)

@auth.requires_login()
def t_request_manage():
    form = SQLFORM(db.t_request)
    # .smartgrid(db.t_t_building,onupdate=auth.archive)
    if form.process().accepted:
        response.flash = 'form accepted';
    elif form.errors:
        response.flash = 'form has errors'
    else:
        response.flash = 'please fill out the form'
    return dict(form=form)


@auth.requires_login()
def t_request_comments_manage():
    form = SQLFORM(db.t_request_comments)
    # .smartgrid(db.t_t_building,onupdate=auth.archive)
    if form.process().accepted:
        response.flash = 'form accepted';
    elif form.errors:
        response.flash = 'form has errors'
    else:
        response.flash = 'please fill out the form'
    return dict(form=form)


@auth.requires_login()
def t_request_type_manage():
    form = SQLFORM(db.t_request_type)
    # .smartgrid(db.t_t_building,onupdate=auth.archive)
    if form.process().accepted:
        response.flash = 'form accepted';
    elif form.errors:
        response.flash = 'form has errors'
    else:
        response.flash = 'please fill out the form'
    return dict(form=form)

@auth.requires_login()
def t_room_manage():
    form = SQLFORM(db.t_room)
    # .smartgrid(db.t_t_building,onupdate=auth.archive)
    if form.process().accepted:
        response.flash = 'form accepted';
    elif form.errors:
        response.flash = 'form has errors'
    else:
        response.flash = 'please fill out the form'
    return dict(form=form)


@auth.requires_login()
def t_room_type_manage():
    form = SQLFORM(db.t_room_type)
    # .smartgrid(db.t_t_building,onupdate=auth.archive)
    if form.process().accepted:
        response.flash = 'form accepted';
    elif form.errors:
        response.flash = 'form has errors'
    else:
        response.flash = 'please fill out the form'
    return dict(form=form)

def getAppartmentAvailables(apartmentNum):
    statement = "SELECT f_capacity FROM t_room WHERE f_apartment=\'"+str(apartmentNum)+"\'";
    rooms = db.executesql(statement);
    return rooms;

def getAvailables():
    # get avail in rooms for each apartment ?return: JSON?
    # returns it to view for processing
    request.vars.type
    request.vars.year
    request.vars.gender
    request.vars.semester
    return getAppartmentAvailables(405);

def submitContract():
    # check room availabilities first
    # then check to see if the desired room is available (function?)
    request.vars.type
    request.vars.year
    request.vars.gender
    request.vars.semester
    request.vars.firstName
    request.vars.lastName
    request.vars.city
    request.vars.state
    request.vars.zip
    request.vars.phone
    request.vars.email
    return request.vars.email;

def getSemesterDates():
    return request.vars.year + request.vars.semester;