from wostabfile.core import WosTabFile
from collections import OrderedDict

# data source
root_path = "data/social network"
file_path = root_path + "/part1.txt"

# header fields in the text file
# Tag from: https://images.webofknowledge.com/images/help/WOS/hs_wos_fieldtags.html
wos_fields = ["PY", "NR", "TC", "U1", "U2"]
# load data by specific keys
wtf = WosTabFile(file_path=file_path)

table = wtf.generate_table(wos_fields)

print()
# group by year using count for numbers of publications per year
new_table=wtf.group_by(table,key_index=0,value_index=1,method="count")
new_table = OrderedDict(sorted(new_table.items()))

print("Year\tNumber of publication")
for year in new_table:
    print(f'{year}\t{new_table[year]}')


