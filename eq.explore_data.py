import json

#探索数据的结构
filename='eq_data_1_day_m1.json'
with open(filename) as f:
    all_eq_data=json.load(f)
readable_file='readable_eq_data.json'
# with open(readable_file,'w') as f:
#     json.dump(all_eq_data,f,indent=4)
all_eq_dicts=all_eq_data['features']
mags,titles,lons,lats=[],[],[],[]
for eq_dicts in all_eq_dicts:
    mag=eq_dicts['properties']['mag']
    title=eq_dicts['properties']['title']
    lon=eq_dicts['geometry']['coordinates'][0]
    lat=eq_dicts['geometry']['coordinates'][1]
    mags.append(mag)
    titles.append(title)
    lons.append(lon)
    lats.append(lat)
print(mags[:10])
print(titles[:2])
print(lons[:5])
print(lats[:5])
