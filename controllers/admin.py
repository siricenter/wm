# -*- coding: utf-8 -*-
### required - do no delete
def user(): return dict(form=auth())
def download(): return response.download(request,db)
def call(): return service()
### end requires

@auth.requires_login()
def index():
	username = auth.user.first_name;
	links = ['Builings','Floors','Rooms','Parking','Tenants']
	return locals()
	
import Admin
def displayQuery():
	myAdmin = AdminStuff(4,5)
	return dict(myAdmin = myAdmin)