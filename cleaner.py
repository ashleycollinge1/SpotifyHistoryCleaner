import json
# import json file with streaming history

with open("Streaming_History_Audio_2021_10.json", "r", encoding="utf8") as jsonfile:
    data = json.load(jsonfile)

# filter through and print all of the records which have rain in them
data2 = data
"""
for i in data2:
    try:
        if "White Noise Rain Sound" in i["master_metadata_track_name"]:
            print(i["master_metadata_track_name"])
            print("Removing")
            print(type(i))
            data2.remove(i)
    except:
        print(i)

for i in data2:
    try:
        if "White Noise Rain Sound" in i["master_metadata_track_name"]:
            print(i["master_metadata_track_name"])
            print("still there")
    except:
        pass"""

def determine(song):
    """ return true is song equals rain """
    try:
        # master_metadata_track_name
        if "The Rain Library" in song["master_metadata_album_artist_name"]:
            return True
        else:
            return False   
    except Exception as e:
        print(e)
        return True

somelist = [x for x in data2 if not determine(x)]
#print(somelist)
for i in somelist:
    if not "The Rain Library" in i["master_metadata_album_artist_name"]:
        print(i["master_metadata_album_artist_name"])

with open("Streaming_History_Audio_2021_10_RainRemoved.json", "w") as fout:
    json.dump(somelist, fout)