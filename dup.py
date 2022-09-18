#merge two duplicates together
#the newer(bottom) merge to the top
#the newer will replace top rows if there are duplicates, or else just fill.
import pandas as _pandas

db = _pandas.read_csv('dup.csv')
print(db.values)
db_merge = db.groupby("Name").last().reset_index()
db_merge = db_merge.groupby("No").last().reset_index()
print(db_merge.values)