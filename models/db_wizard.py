### we prepend t_ to tablenames and f_ to fieldnames for disambiguity


########################################
db.define_table('t_semester',
    Field('f_start_date', type='date',
          label=T('Start Date')),
    Field('f_end_date', type='date',
          label=T('End Date')),
    Field('f_creation_date', type='date',
          label=T('Creation Date')),
    Field('f_last_updated_date', type='date',
          label=T('Last Updated Date')),
    auth.signature,
    format='%(f_start_date)s',
    migrate=settings.migrate)

db.define_table('t_semester_archive',db.t_semester,Field('current_record','reference t_semester',readable=False,writable=False))

########################################
db.define_table('t_request_comments',
    Field('f_comments', type='string',
          label=T('Comments'),notnull=True),
    Field('f_creations_date', type='date',
          label=T('Creation Date'),notnull=True),
    Field('f_created_by', type='references auth_user',
          label=T('Created By'),notnull=True),
    auth.signature,
    format='%(f_comments)s',
    migrate=settings.migrate)

db.define_table('t_request_comments_archive',db.t_request_comments,Field('current_record','reference t_request_comments',readable=False,writable=False))

########################################
db.define_table('t_apartment_type',
    Field('f_apartment_type', type='string',
          label=T('Apartment Type')),
    auth.signature,
    format='%(f_apartment_type)s',
    migrate=settings.migrate)

db.define_table('t_apartment_type_archive',db.t_apartment_type,Field('current_record','reference t_apartment_type',readable=False,writable=False))


########################################
db.define_table('t_apartment',
    Field('f_floor_id', type='string',
          label=T('Floor Id')),
    Field('f_apartment_type_id', type='references t_apartment_type',
          label=T('Apartment Type Id')),
    Field('f_apartment_number', type='string',
          label=T('Apartment Number')),
    auth.signature,
    format='%(f_floor_id)s',
    migrate=settings.migrate)

db.define_table('t_apartment_archive',db.t_apartment,Field('current_record','reference t_apartment',readable=False,writable=False))

########################################
db.define_table('t_contract',
    Field('f_user_id', type='references auth_user',
          label=T('User Id'),notnull=True),
    Field('f_apartment_id', type='references t_apartment',
          label=T('Apartment Id'),notnull=True),
    Field('f_semester_id', type='references t_semester',
          label=T('Semester Id'),notnull=True),
    Field('f_active', type='boolean',
          label=T('Active'),notnull=True),
    Field('f_creation_date', type='date',
          label=T('Creation Date'),notnull=True),
    Field('f_last_updated_date', type='date',
          label=T('Last Updated Date'),notnull=True),
    auth.signature,
    format='%(f_user_id)s',
    migrate=settings.migrate)

db.define_table('t_contract_archive',db.t_contract,Field('current_record','reference t_contract',readable=False,writable=False))

########################################
db.define_table('t_parking',
    Field('f_user_id', type='references auth_user',
          label=T('User Id')),
    Field('f_stall_number', type='string',
          label=T('Stall Number')),
    Field('f_car_make', type='string',
          label=T('Car Make')),
    Field('f_car_model', type='string',
          label=T('Car Model')),
    Field('f_license_plate_number', type='string',
          label=T('License Plate Number')),
    auth.signature,
    format='%(f_user_id)s',
    migrate=settings.migrate)

db.define_table('t_parking_archive',db.t_parking,Field('current_record','reference t_parking',readable=False,writable=False))

########################################
db.define_table('t_room_type',
    Field('f_type', type='string',
          label=T('Type')),
    Field('f_details', type='string',
          label=T('Details')),
    auth.signature,
    format='%(f_type)s',
    migrate=settings.migrate)

db.define_table('t_room_type_archive',db.t_room_type,Field('current_record','reference t_room_type',readable=False,writable=False))

########################################
db.define_table('t_request_type',
    Field('f_type', type='string',
          label=T('Type')),
    Field('f_details', type='string',
          label=T('Details')),
    auth.signature,
    format='%(f_type)s',
    migrate=settings.migrate)

db.define_table('t_request_type_archive',db.t_request_type,Field('current_record','reference t_request_type',readable=False,writable=False))



########################################
db.define_table('t_building',
    Field('f_building_name', type='string',
          label=T('Building Name')),
    Field('f_building_number', type='string',
          label=T('Building Number')),
    Field('f_building_type', type='string',
          label=T('Building Type')),
    auth.signature,
    format='%(f_building_name)s',
    migrate=settings.migrate)

db.define_table('t_building_archive',db.t_building,Field('current_record','reference t_building',readable=False,writable=False))

########################################
db.define_table('t_request',
    Field('f_user_id', type='string',
          label=T('User Id')),
    Field('f_request_type_id', type='references t_request_type',
          label=T('Request Type Id')),
    Field('f_request_comments_id', type='references t_request_comments',
          label=T('Request Comments Id')),
    Field('f_location', type='string',
          label=T('Location')),
    Field('f_details', type='string',
          label=T('Details')),
    Field('f_status', type='string',
          label=T('Status')),
    Field('f_creation_date', type='date',
          label=T('Creation Date')),
    Field('f_last_updated_date', type='date',
          label=T('Last Updated Date')),
    auth.signature,
    format='%(f_user_id)s',
    migrate=settings.migrate)

db.define_table('t_request_archive',db.t_request,Field('current_record','reference t_request',readable=False,writable=False))

########################################
db.define_table('t_floor',
    Field('f_building_id', type='references t_building',
          label=T('Building Id')),
    Field('f_floor_number', type='string',
          label=T('Floor Number')),
    auth.signature,
    format='%(f_building_id)s',
    migrate=settings.migrate)

db.define_table('t_floor_archive',db.t_floor,Field('current_record','reference t_floor',readable=False,writable=False))

########################################
db.define_table('t_room',
    Field('f_room_type_id', type='references t_floor',
          label=T('Room Type Id')),
    Field('f_apartment_id', type='references t_apartment',
          label=T('Apartment Id')),
    auth.signature,
    format='%(f_room_type_id)s',
    migrate=settings.migrate)

db.define_table('t_room_archive',db.t_room,Field('current_record','reference t_room',readable=False,writable=False))


########################################
db.define_table('t_user_info',
	Field('f_user_id', type='references auth_user',
          label=T('user_id')),
    Field('f_firstname', type='string',
          label=T('First Name')),
    Field('f_middlename', type='string',
          label=T('Middle Name')),
	Field('f_lastname', type='string',
          label=T('Last Name')),
    Field('f_phone', type='string',
          label=T('Phone')),
    Field('f_address1', type='string',
          label=T('Address1')),
    Field('f_address2', type='string',
          label=T('Address2')),
    Field('f_city', type='string',
          label=T('City')),
    Field('f_state', type='string',
          label=T('State')),
    Field('f_zip', type='string',
          label=T('Zip')),
    Field('f_country', type='string',
          label=T('Country')),
    Field('f_gender', type='string',
          label=T('Gender')),
    Field('f_creation_date', type='date',
          label=T('Creation Date')),
    Field('f_last_updated_date', type='date',
          label=T('Last Updated Date')),
    auth.signature,
    format='%(f_phone)s',
    migrate=settings.migrate)

db.define_table('t_user_info_archive',db.t_user_info,Field('current_record','reference t_user_info',readable=False,writable=False))
