# ciscoconfparser
Extract information from multiple cisco configuration files using specific search phrases

Instructions:

1. Update data_to_search dictionary in parse.py and specify the value you need to search for
2. Place all the cisco configuration files in the same directory (or within a subdirectory)
3. Run the script

Output:

This will automatically parse through ever file and search for the phrases, i.e.

- NTP information
- Username and passwords
- IOS versions

It will then generate a report that shows the paramater found for each device, and paramaters that
are missing to assist with auditing purposes.
