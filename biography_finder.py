# This file is responsible for extracting biographical data.
# You need to actively review the extraction results, which will then get saved in a Python array
# There is quite a long wait involved as all of the data is pre-loaded.

import pandas as pd
import wikipedia
import json

# This database is taken from the Vilna Troupe project and can be found at http://vilnatroupe.com
# It is not included in the current dataset for reasons of rights and updatability.
df = pd.read_excel("../current_database.xls")

# The code below parses the original file and saves it as members:
members = df.loc[:,["Full Name"]].values.tolist()
members = [x[0] for x in members if isinstance(x[0], str)]
wiki_biographies = {}
biographies = {}

# Geographies are then extracted as a Python dictionary.
# They can then be added to the data-set as a separate column and displayed.
for member in members:

    try:
        wiki_biography = wikipedia.summary(member)
    except:
        wiki_biography = ''

    if wiki_biography != '':
        wiki_biographies[member] = wiki_biography

for bio in wiki_biographies:
    test = input("\n" +  bio + "###" + "Include for (y/n): " + wiki_biographies[bio] + "\n" + "\n")
    if test == "y":
        biographies[bio] = wiki_biographies[bio]

with open('biographies.json', 'w') as convert_file:
    convert_file.write(json.dumps(biographies))