# fec-individual-contribution-engine
Query the FEC API of the United States government to perform individual contribution analysis and financial analysis on a grassroots level based on a corpus of last names, searching by state, zipcode, etc. 

Currently there is a script (`count_indian_surname_candidate_support.py`) that will take in a corpus of last names, which has been defaulted with surnames of South Asian (mostly Indian, Hindu) origin. The script will execute a search of each last name, for each state in the U.S. and read the memo of each result and tokenize the memo string. 

After the memo string is tokenized, there is a function that will search for a candidate name and increment the surname's and state's value for that candidate by one. Currently, the data structure holding all this data is a n=3 nested dictionary.

The script will also output a few files, the most important one being titled "`finalRecipient`" which is an entire print out of the data collected. There is also a pickle file that will get generated titled "`recipient.pickle`".

The `rest.py` class contains a couple API calls that will send a JSON GET request primarily using a date range, a contributor name, and a state or zip-code. There are *numerous* endpoints and parameters you can use, just modify the API call. https://api.open.fec.gov/developers

This is currently a work in progress and I am working on an extensive optimization, which could potentially allow me to run this on even larger datasets **within a few minutes**.

The `recipient` data structure looks like the following:
  - from a search of all individual political contributions in 2019-2020 by last names Ghosh, Patel, and Datta. (please note that the results in this example are heavily truncated...)

```
{   'bernie': {   'AL': {'PATEL': 1},
                  'AR': {'PATEL': 5},
                  'AZ': {'PATEL': 1},
                  ...
                  'MD': {'DATTA': 3, 'GHOSH': 2, 'PATEL': 3},
                  'MI': {'DATTA': 1, 'PATEL': 1},
                  'MN': {'DATTA': 1},
                  ...
                  'VT': {'PATEL': 1},
                  'WA': {'DATTA': 7, 'PATEL': 5},
                  'WI': {'PATEL': 2}},
    'biden': {   'AL': {'PATEL': 1},
                 'CA': {'DATTA': 2},
                 'DE': {'GHOSH': 2},
                 ...
                 'NV': {'PATEL': 5},
                 'OR': {'GHOSH': 2},
                 'WA': {'GHOSH': 2}},
    'dccc': {   'AZ': {'PATEL': 4},
                'CA': {'DATTA': 1, 'PATEL': 5},
                'CO': {'DATTA': 3},
                ...
                'UT': {'PATEL': 6},
                'VA': {'PATEL': 1},
                'WV': {'PATEL': 5},
                'dccc': {}},
    'julian': {   'NY': {'GHOSH': 1},
                  'TX': {'PATEL': 3},
                  'VA': {'DATTA': 2, 'PATEL': 1},
                  'WA': {'GHOSH': 1},
                  'WV': {'GHOSH': 4},
                  'julian': {}},
    'kamala': {   'AZ': {'PATEL': 1},
                  'CA': {'DATTA': 1, 'GHOSH': 1, 'PATEL': 2},
                  ...
                  'OR': {'PATEL': 3},
                  'PA': {'GHOSH': 1, 'PATEL': 2},
                  'SC': {'PATEL': 4},
                  'WA': {'GHOSH': 5},
                  'WI': {'PATEL': 1},
                  'kamala': {}},
    'sanders': {'MD': {'GHOSH': 0}},
    'trump': {'MD': {'GHOSH': 0}},
    'tulsi': {   'AR': {'PATEL': 2},
                 'AZ': {'PATEL': 1},
                 ...
                 'VA': {'PATEL': 1},
                 'VT': {'PATEL': 1},
                 'WA': {'GHOSH': 1, 'PATEL': 1},
                 'WI': {'DATTA': 1}},
    'warren': {   'CA': {'DATTA': 1, 'PATEL': 1},
                  'CO': {'PATEL': 1},
                  ...
                  'TX': {'PATEL': 2},
                  'VA': {'GHOSH': 1},
                  'WA': {'DATTA': 1}},
    'yang': {   'AL': {'PATEL': 1},
                'CA': {'GHOSH': 1},
                'CT': {'PATEL': 2},
                'DC': {'PATEL': 1},
                'HI': {'DATTA': 1},
                'IA': {'PATEL': 2},
                'IN': {'PATEL': 2},
                'MA': {'GHOSH': 2},
                'MD': {'GHOSH': 1},
                'MN': {'PATEL': 1},
                'NH': {'PATEL': 1},
                'NJ': {'DATTA': 2},
                'SC': {'PATEL': 1},
                'VA': {'DATTA': 1},
                'WA': {'PATEL': 1},
                'WI': {'PATEL': 2}}}
```
