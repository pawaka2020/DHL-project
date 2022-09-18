import pandas as _pandas

db = _pandas.read_csv('names.csv')

def cleanup_names(db):
	db['Name'] = db['Name'].str.replace('[a-z]', '', regex=True)
	db['Name'] = db['Name'].str.replace('[!-@]', '', regex=True)
	db['Name'] = db['Name'].str.replace(' +', ' ', regex=True)
	db['Name'] = db['Name'].str.strip()

print("\nValues before cleanup: \n" + str(db.values))
cleanup_names(db)
print("\nValues after cleanup : \n" + str(db.values))