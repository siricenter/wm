from gluon.storage import Storage
settings = Storage()

settings.migrate = True
settings.title = 'Windsor Manor'
settings.subtitle = 'Really Great Apartments'
settings.author = 'RBD-Center'
settings.author_email = 'info@rbdcenter.org'
settings.keywords = ''
settings.description = ''
settings.layout_theme = 'Default'
settings.database_uri = 'sqlite://storage.sqlite'
settings.security_key = 'dc2b091a-e8e9-4bf4-8e7e-6cd658ba98d3'
settings.email_server = 'localhost'
settings.email_sender = 'you@example.com'
settings.email_login = ''
settings.login_method = 'local'
settings.login_config = ''
settings.plugins = []
