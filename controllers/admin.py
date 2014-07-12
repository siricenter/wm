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
	username = auth.user.first_name
	tables = test()
	return locals()

@auth.requires_login()	
def manageUsers():
	query = db.t_building
	grid = SQLFORM.grid(query=query)
	return grid

def test():
	list = db.tables
	tables = []
	for x in range(len(list)):
		match = re.search('archive',list[x])
		if not match:
			list[x] = list[x].replace('auth_','')
			list[x] = re.sub('^t_', '', list[x])
			list[x] = list[x].replace('_',' ')
			if list[x] not in ('event','cas'):
				tables.append(list[x].title())
			continue
		continue
	return tables

import re
def tables():
	tableNames = db.tables
	tableList = []
	for x in range(len(tableNames)):
		match = re.search('archive',tableNames[x])
		if not match:
			val = tableNames[x].replace('auth_','')
			val = re.sub('^t_', '', val)
			val = val.replace('_',' ')
			tableList.append({tableNames[x]:val.title()})
			continue
	return response.json(tableList)
	
def testing():
	list = db.tables
	return response.json(list)
	