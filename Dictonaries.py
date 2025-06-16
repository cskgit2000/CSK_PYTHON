#CRICKET
cricket={
    "Player001":{"name":"ABD","pickup":"South Africa","drop":"Bengaluru","IPL":"RCB"},
    "Player002":{"name":"MSD","pickup":"Ranchi","drop":"Chennai","IPL":"CSK"},
    "Player003":{"name":"FAF","pickup":"South Africa","drop":"Chennai","IPL":"CSK"}
}

for name,details in cricket.items():
    print("NAME = ",details["name"])
    print("IPL TEAM =",details["IPL"])
    print(details["pickup"],"→",details["drop"])
