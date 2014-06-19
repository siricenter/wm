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

@auth.requires_login()
def t_building_manage():
    form = SQLFORM.smartgrid(db.t_t_building,onupdate=auth.archive)
    return locals()

@auth.requires_login()
def t_floor_manage():
    form = SQLFORM.smartgrid(db.t_t_floor,onupdate=auth.archive)
    return locals()

@auth.requires_login()
def t_apartment_manage():
    form = SQLFORM.smartgrid(db.t_t_apartment,onupdate=auth.archive)
    return locals()

@auth.requires_login()
def t_apartment_type_manage():
    form = SQLFORM.smartgrid(db.t_t_apartment_type,onupdate=auth.archive)
    return locals()

@auth.requires_login()
def t_user_info_manage():
    form = SQLFORM.smartgrid(db.t_t_user_info,onupdate=auth.archive)
    return locals()

@auth.requires_login()
def t_contract_manage():
    form = SQLFORM.smartgrid(db.t_t_contract,onupdate=auth.archive)
    return locals()

@auth.requires_login()
def t_semester_manage():
    form = SQLFORM.smartgrid(db.t_t_semester,onupdate=auth.archive)
    return locals()

@auth.requires_login()
def t_parking_manage():
    form = SQLFORM.smartgrid(db.t_t_parking,onupdate=auth.archive)
    return locals()

@auth.requires_login()
def t_request_manage():
    form = SQLFORM.smartgrid(db.t_t_request,onupdate=auth.archive)
    return locals()

@auth.requires_login()
def t_request_comments_manage():
    form = SQLFORM.smartgrid(db.t_t_request_comments,onupdate=auth.archive)
    return locals()

@auth.requires_login()
def t_request_type_manage():
    form = SQLFORM.smartgrid(db.t_t_request_type,onupdate=auth.archive)
    return locals()

@auth.requires_login()
def t_room_manage():
    form = SQLFORM.smartgrid(db.t_t_room,onupdate=auth.archive)
    return locals()

@auth.requires_login()
def t_room_type_manage():
    form = SQLFORM.smartgrid(db.t_t_room_type,onupdate=auth.archive)
    return locals()

