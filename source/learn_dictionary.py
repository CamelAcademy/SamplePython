print("Key value pair - Key are unique")
monthConversions = {
    "Jan":"Janury",
    "Mar":"March",
    "Apr":"April",
    "May":"MAY",
    2:"Feb"
}

print(monthConversions["May"])
print(monthConversions.get("Feb","Not a valid Key"))
print(monthConversions.get(2,"Not a valid Key"))