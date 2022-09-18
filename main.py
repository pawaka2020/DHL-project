import pandas as _pandas
import function as func

db = _pandas.read_csv('names.csv')


print("\nValues before cleanup: \n" + str(db.values))
func.cleanup_names(db)
print("\nValues after cleanup : \n" + str(db.values))