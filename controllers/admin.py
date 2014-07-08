# -*- coding: utf-8 -*-
### required - do no delete
def user(): return dict(form=auth())
def download(): return response.download(request,db)
def call(): return service()
### end requires

from datetime import date

@auth.requires_login()
def index():
	username = auth.user.first_name;
	links = ['buildings','floors','rooms','parking','tenants']
	return locals()

@auth.requires_login()	
def manageUsers():
	query = db.auth_user
	grid = SQLFORM.grid(query=query)
	return grid

def test():
	return request.vars.name