__version__ = "1.0"

import os
from ciscoconfparse import CiscoConfParse

# -----------------------------------------------
# Create the db dictionary to store all records
# -----------------------------------------------
db = {}
# ----------------------------------------------------------------
# Update the dictionary below to search for new search parameters
# ----------------------------------------------------------------
data_to_search = {"NTP"       : r"ntp server",
                  "SNMP"      : r"snmp server",
                  "USERNAME"  : r"username",
                  "AAA"       : r"aaa",
                  "VERSION"   : r"System image file"}

def read_data():
    print ("--------------------------------------------------------------------")
    print (" Searching current directory and sub-directories for .txt files....")
    print ("--------------------------------------------------------------------")
    for path, dirs, files in os.walk("."):
            for f in files:
                if f.endswith('.txt'):
                    hostname = f.replace(".txt","")
                    print ("Reading data from: {}".format(os.path.join(path, f)))

                    # Create an entry for the devices based on the hostname
                    db[hostname] = {}
                    for search_parameter in data_to_search:
                        db[hostname][search_parameter] = []

                    # Read the configuration file
                    parse = CiscoConfParse(os.path.join(path, f))
                    #----------------------------------------------------------
                    # Search for all relevant items and store findings in the
                    # db dictionary so that we can use later on
                    #----------------------------------------------------------
                    for search_parameter in data_to_search:
                        for obj in parse.find_objects(data_to_search[search_parameter]):
                            db[hostname][search_parameter].append(obj.text)

def generate_output():
    if (db):
        print ("-----------------------")
        print (" Configuration snapshot")
        print ("-----------------------")
        for device in sorted(db):
            print ("[{}]".format(device))
            for search_parameter in data_to_search:
                if db[device][search_parameter]:
                    for line in db[device][search_parameter]:
                        print ("  {}: {}".format(search_parameter.ljust(10),line))
                else:
                    print ("  {}: NOT FOUND".format(search_parameter.ljust(10)))
            print ("")
    else:
        print ('- No data was found')

def show_devices_with_missing_entries():
    if (db):
        print ("-------------------------------")
        print (" Devices with missing entries  ")
        print ("-------------------------------")
        for device in sorted(db):
            for entry in data_to_search:
                if not db[device][entry]:
                    print ("[{}] has no entry defined for '{}'".format(device.ljust(25),entry))
    else:
        print ('- No devices with missing entries')


read_data()
generate_output()
show_devices_with_missing_entries()
