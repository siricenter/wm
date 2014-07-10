# -*- coding: utf-8 -*-
### required - do no delete
def user(): return dict(form=auth())
def download(): return response.download(request,db)
def call(): return service()
### end requires

from datetime import date
from gluon.serializers import json


@auth.requires_login()
def index():
	username = auth.user.first_name;
	list = db.tables
	tables = []
	for x in range(len(list)):
		match = re.search('archive',list[x])
		if not match:
			list[x] = list[x].replace('auth_','')
			list[x] = re.sub('^t_', '', list[x])
			list[x] = list[x].replace('_',' ')
			tables.append(list[x].title())
			continue
	return locals()

@auth.requires_login()	
def manageUsers():
	query = db.auth_user
	grid = SQLFORM.grid(query=query)
	return grid

def test():
    return request.vars.tester

import re
def tables():
	list = db.tables
	tables = []
	for x in range(len(list)):
		match = re.search('archive',list[x])
		if not match:
			list[x] = list[x].replace('auth_','')
			list[x] = re.sub('^t_', '', list[x])
			list[x] = list[x].replace('_',' ')
			tables.append(list[x].title())
			continue
	return response.json(tables)
	
def testing():
	list = db.tables
	return response.json(list)
	