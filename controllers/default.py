# -*- coding: utf-8 -*-
### required - do no delete
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
#This is the tenant registration form
def registration_form():
    form=FORM('First name:', INPUT(_name='fName', requires=IS_NOT_EMPTY()),
              'Last name:', INPUT(_name='lName', requires=IS_NOT_EMPTY()),
              'Gender:', INPUT(_name='gender', requires=IS_NOT_EMPTY()),
              'Current address:', INPUT(_name='cAddress', requires=IS_NOT_EMPTY()),
              'Current city:', INPUT(_name='cCity', requires=IS_NOT_EMPTY()),
              'Current state:', INPUT(_name='pState', requires=IS_NOT_EMPTY()),
              'Zip:', INPUT(_name='zip', requires=IS_NOT_EMPTY()),
              INPUT(_type='submit'))
    if form.accepts(request,session):
        response.flash = 'form accepted'
        process_registration(form)
    elif form.errors:
        response.flash = 'form has errors'
    else:
        response.flash = 'please fill the form'
    return dict(form=form)

# This function processes the registration form and add the data to the database
def process_registration(form):
    user_info_table = t_user_info_manage()
    user_info_table.vars.firstname = form.name
    response.flash = user_info_table.vars.firstname
    return

#@auth.requires_login()
def t_building_manage():
    form = SQLFORM(db.t_building)
    if form.process().accepted:
        response.flash = 'form accepted';
    elif form.errors:
        response.flash = 'form has errors'
    else:
        response.flash = 'please fill out the form'
    return dict(form=form)

#@auth.requires_login()
def t_floor_manage():
    form = SQLFORM(db.t_floor)
    if form.process().accepted:
        response.flash = 'form accepted';
    elif form.errors:
        response.flash = 'form has errors'
    else:
        response.flash = 'please fill out the form'
    return dict(form=form)

#@auth.requires_login()
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

#@auth.requires_login()
def t_apartment_type_manage():
    form = SQLFORM(db.t_apartment_type)
    if form.process().accepted:
        response.flash = 'form accepted';
    elif form.errors:
        response.flash = 'form has errors'
    else:
        response.flash = 'please fill out the form'
    return dict(form=form)


#@auth.requires_login()
def t_user_info_manage():
    form = SQLFORM(db.t_user_info)
    return form

#@auth.requires_login()
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

#@auth.requires_login()
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


#@auth.requires_login()
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

#@auth.requires_login()
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


#@auth.requires_login()
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


#@auth.requires_login()
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

#@auth.requires_login()
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


#@auth.requires_login()
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
