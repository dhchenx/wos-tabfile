from wostabfile.core import WosTabFile
from collections import OrderedDict

root_path = "data/social network"

wos_fields = ["PY", "NR", "TC", "U1", "U2"]

wtf = WosTabFile(file_path=root_path)

table = wtf.generate_table_by_folder(wos_fields)

new_table=wtf.group_by(table,key_index=0,value_index=1,method="sum")

new_table = OrderedDict(sorted(new_table.items()))
print("Year\tNumber of citations")
for year in new_table:
    if year=='' or int(year)<2000:
        continue
    print(f'{year}\t{int(new_table[year])}')