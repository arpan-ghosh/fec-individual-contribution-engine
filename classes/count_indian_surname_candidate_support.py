import os
import sys
import pandas

from tools.utility import Utility
from tools import rest


class count_indian_surname_candidate_support:
    def __init__(self):
        self.indian_surnames = pandas.read_csv(Utility.ROOT + Utility.INDIAN_SURNAME_FILE_PATH)
        self.utility = Utility()
        self.states = self.utility.__extract_abbreviations__(self.utility)

    @staticmethod
    def run(self, state, last_name):
        results = {}

        if state == 'getAllStates':
            for state in self.states:
                results[state] = {}
        else:
            # Demo: this code just does MD
            results['MD'] = {}

        # results = Utility.multi_dict(self.utility, 3, str)

        #   grab the contribution ID, total amount, and candidate, date
        for state in results:
            # self.utility.__get_pretty_printer__().pprint(last_name)

            contributor = rest.individualContributorSearchByState(rest.API_KEY, last_name, state)
            json_data = contributor.query()

            # Utility.__get_pretty_printer__().pprint(json_data)

            results[state][last_name] = json_data

        return results

    def parse_results(self, initial_results, last_name, recipient):
        for state,surname in initial_results.items():
            # self.utility.__get_pretty_printer__().pprint(state)
            # self.utility.__get_pretty_printer__().pprint(surname)
            count = 0
            results = {}
            values = list(surname.values())

            for value in values:
                # self.utility.__get_pretty_printer__().pprint(value['pagination'])
                # count = value['pagination']['count']
                if 'results' in value:
                    results = value['results']

            # self.utility.__get_pretty_printer__().pprint(count)
            # self.utility.__get_pretty_printer__().pprint(results)

            for result in results:
                # self.utility.__get_pretty_printer__().pprint(result)
                if result['contributor_last_name'] == last_name:
                    self.utility.parse_memo_text_for_candidate(self.utility, result['memo_text'], last_name, state, recipient)
                else:
                    results.remove(result)

        return results


if __name__ == '__main__':
    tool = count_indian_surname_candidate_support()

    recipient = {
        'sanders': {
            'MD': {
                'GHOSH': int(0)
            }
        },
        'bernie': {
            'MD': {
                'GHOSH': int(0)
            }
        },
        'biden': {
            'MD': {
                'GHOSH': int(0)
            }
        },
        'warren': {
            'MD': {
                'GHOSH': 0
            }
        },
        'yang': {
            'MD': {
                'GHOSH': int(0)
            }
        },
        'tulsi': {
            'MD': {
                'GHOSH': int(0)
            }
        },
        'trump': {
            'MD': {
                'GHOSH': int(0)
            }
        }
    }

    # initial_results = tool.run(tool, 'MD', 'PATEL')
    # # Utility.__get_pretty_printer__().pprint(initial_results)
    # final_results = tool.parse_results(initial_results, 'PATEL')
    # # Utility.__get_pretty_printer__().pprint(final_results)

    for last_name in tool.indian_surnames:
        Utility.__get_pretty_printer__().pprint("Last name: " + last_name)
        initial_results = tool.run(tool, 'getAllStates', last_name)
        # Utility.__get_pretty_printer__().pprint(initial_results)

        final_results = tool.parse_results(initial_results, last_name, recipient)
        Utility.__get_pretty_printer__().pprint(final_results)

        f = open("finalResults.txt", "a+")
        f.write(str(final_results))
        f.close()

    f = open("finalRecipient.txt", "a+")
    f.write(str(recipient))
    f.close()