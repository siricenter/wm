# -*- coding: utf-8 -*-
### required - do no delete
def user(): return dict(form=auth())
def download(): return response.download(request,db)
def call(): return service()
### end requires

crud = Crud(db)
crud.settings.controller = 'admin'

@auth.requires_login()
def index():
	return dict()

@auth.requires_login()
def cruds():
	return dict(form=crud())
