# -*- coding: utf-8 -*-
### required - do no delete
def user(): return dict(form=auth())
def download(): return response.download(request,db)
def call(): return service()
### end requires

@auth.requires_login()
def index():
	username = auth.user.first_name;
	links = ['buildings','floors','rooms','parking','tenants']
	results = manageUsers()
	return locals()
	
import Admin
def displayQuery():
	myAdmin = AdminStuff(4,5)
	return dict(myAdmin = myAdmin)
	
def manageUsers():
	grid = SQLFORM.grid(db.auth_user)
	return locals()