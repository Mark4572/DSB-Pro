import requests, base64, json, gzip, datetime, uuid



DataURL = "https://app.dsbcontrol.de/JsonHandler.ashx/GetData"

current_time = datetime.datetime.now().isoformat()
# Cut off last 3 digits and add 'Z' to get correct format
current_time = current_time[:-3] + "Z"
# Parameters required for the server to accept our data request
params = {
    "UserId": 274583,
    "UserPw": "Johann",
    "AppVersion": "2.5.9",
    "Language": "de",
    "OsVersion": "28 8.0",
    "AppId": str(uuid.uuid4()),
    "Device": "SM-G930F",
    "BundleId": "de.heinekingmedia.dsbmobile",
    "Date": current_time,
    "LastUpdate": current_time
}
# Convert params into the right format
params_bytestring = json.dumps(params, separators=(',', ':')).encode("UTF-8")
params_compressed = base64.b64encode(gzip.compress(params_bytestring)).decode("UTF-8")

# Send the request
json_data = {"req": {"Data": params_compressed, "DataType": 1}}
timetable_data = requests.post(DataURL, json = json_data)

# Decompress response
data_compressed = json.loads(timetable_data.content)["d"]
data = json.loads(gzip.decompress(base64.b64decode(data_compressed)))

with open("Links.json", "w") as File:
    File.write(str(data))
