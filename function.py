def	cleanup_names(db):
	db['Name'] = db['Name'].str.replace('[a-z]', '', regex=True)
	db['Name'] = db['Name'].str.replace('[:-@]', '', regex=True)
	db['Name'] = db['Name'].str.replace('[!-/]', '', regex=True)
	db['Name'] = db['Name'].str.replace(' +', ' ', regex=True)
	db['Name'] = db['Name'].str.strip()