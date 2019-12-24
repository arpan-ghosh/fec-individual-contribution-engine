import json
import sys
import time
import uuid
import requests
import pandas

from classes.tools.utility import Utility


API_URL = "https://api.open.fec.gov/v1/schedules/schedule_a/"
API_HOST = "api.open.fec.gov"

# API KEY GOES HERE as variable API_KEY
# API_KEY = abc123

CANDIDATE_LIST = ['sanders', 'bernie', 'biden', 'warren', 'yang', 'tulsi', 'trump', 'buttigieg', 'steyer', 'klobochur', 'dccc', 'rnc', 'julian', 'castro', 'kamala']
STATE_ABBREVIATIONS = Utility.__extract_abbreviations__(Utility)

pprinter = Utility.__get_pretty_printer__()


class individualContributorSearchByState:
    def __init__(self, api_key, last_name, state):
        self.apiKey = api_key
        self.id = uuid.uuid4()
        self.lastName = last_name
        self.state = state

        return

    def __registerAPICall__(self):
        return

    def query(self):
        query_string = self.generateStateQueryStringFor2019()

        response = requests.request("GET", API_URL, headers=get_headers(), params=query_string)

        json_data = json.loads(response.text)

        return json_data

    def generateStateQueryStringFor2019(self):
        return {"api_key": self.apiKey,
                "sort_hide_null": "false",
                "sort_nulls_last": "false",
                "contributor_name": self.lastName + ',',
                "contributor_state": self.state,
                "two_year_transaction_period": "2020",
                "min_date": "2019-01-01",
                "max_date": "2019-12-31",
                "is_individual": "true"}

    def __hash__(self):
        return hash(self.apiKey + self.id)

    def __str__(self):
        return "%s|%s" % (self.apiKey, self.id)


class individualContributorSearchByZipCode:
    def __init__(self, api_key, last_name, first_name, zip_code):
        self.apiKey = self.api_key()
        self.id = uuid.uuid4()
        self.lastName = last_name
        self.firstName = first_name
        self.zipCode = zip_code

        return

    def __registerAPICall__(self):
        return

    def query(self):
        query_string = self.generateZipCodeQueryStringFor2019()

        response = requests.request("GET", API_URL, headers=get_headers(), params=query_string)

        json_data = json.loads(response.text)

        return json_data

    def generateZipCodeQueryStringFor2019(self):
        return {"api_key": self.apiKey,
                "sort_hide_null": "false",
                "sort_nulls_last": "false",
                "contributor_name": self.lastName + ',',
                "contributor_zip": self.zipCode,
                "two_year_transaction_period": "2020",
                "min_date": "2019-01-01",
                "max_date": "2019-12-31",
                "sort": "-contribution_receipt_date",
                "per_page": "30",
                "is_individual": "true"}

    def __hash__(self):
        return hash(self.apiKey + self.id)

    def __str__(self):
        return "%s|%s" % (self.apiKey, self.id)


@staticmethod
def get_api_url():
    return API_URL


def api_key(self):
    # Your api key goes here
    return 'abc123'


def get_headers():
    headers = {
        'Accept': "*/*",
        'Cache-Control': "no-cache",
        'Host': API_HOST,
        'Accept-Encoding': "gzip, deflate",
        'Connection': "keep-alive",
        'cache-control': "no-cache"
    }

    return headers


def bail():
    print("Error: ")
    exit()


def run_with_args(self):
    # get arguments
    argerror = False
    print(len(sys.argv))
    if len(sys.argv) == 2 and sys.argv[1] == '-E':
        print(sys.argv[1])
        print("arg 1 -E")
        # doeJane = individualContributorSearchByZipCode(API_KEY, LAST_NAME, FIRST_NAME, ZIP_CODE)
        # doeJane.query()
    elif len(sys.argv) == 4:
        apiKey = sys.argv[1]
        lastName = sys.argv[2]
        firstName = sys.argv[3]
        zipCode = sys.argv[4]

        # check arguments
        if len(apiKey) == 0:
            argerror = True

# lastName = individualContributorSearchByZipCode(API_KEY, LAST_NAME, FIRST_NAME, ZIP_CODE)
