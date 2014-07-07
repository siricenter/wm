def manageUsers():
	query = db.auth_user
	grid = SQLFORM.grid(query=query)
	return locals()
	
def test(a):
	return a*a