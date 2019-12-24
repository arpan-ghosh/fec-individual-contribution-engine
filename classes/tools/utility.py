import os
import json
import pprint
import nltk
import pickle

from collections import defaultdict
from classes.tools import rest


class Utility:
    ROOT = '/Users/arpanghosh/Code/openFEC/'
    ABBREVIATIONS = []
    # INDIAN_SURNAME_FILE_PATH = 'classes/data/indian_surname_data.csv'
    INDIAN_SURNAME_FILE_PATH = 'classes/data/indian_surname_test.csv'

    def __init__(self):
        pass

    # Utility function to create dictionary
    @staticmethod
    def multi_dict(self, K, type):
        if K == 1:
            return defaultdict(type)
        else:
            return defaultdict(lambda: self.multi_dict(K - 1, type))

    @staticmethod
    def __get_pretty_printer__() -> object:
        return pprint.PrettyPrinter(indent=4)

    @staticmethod
    def __get_states__(self):
        with open(self.ROOT + 'classes/data/states.json') as json_file:
            states = json.load(json_file)

        return states

    @staticmethod
    def state_abbreviations(self):
        self.__extract_abbreviations__(self)

    @staticmethod
    def __extract_abbreviations__(self):
        name_and_abbrevs = self.__get_states__(self)

        for state in name_and_abbrevs:
            self.ABBREVIATIONS.append(state['abbreviation'])
            # self.__get_pretty_printer__().pprint(self.ABBREVIATIONS)

        return self.ABBREVIATIONS

    @staticmethod
    def parse_memo_text_for_candidate(self, memo_text, last_name, state, recipient):
        if memo_text is None:
            return

        if os.path.exists("recipient.txt"):
            os.remove("recipient.txt")

        f = open("recipient.txt", "w+")

        memo_text = memo_text.lower()

        tokens = nltk.word_tokenize(memo_text)
        self.__get_pretty_printer__().pprint(tokens)

        match_set_candidate = [i for i in tokens if i in rest.CANDIDATE_LIST]

        self.__get_pretty_printer__().pprint(match_set_candidate)

        if len(match_set_candidate) > 0:
            self.__get_pretty_printer__().pprint(match_set_candidate[0])
            if match_set_candidate[0] not in recipient:
                recipient[match_set_candidate[0]] = {match_set_candidate[0]: {}}
            if state not in recipient[match_set_candidate[0]]:
                recipient[match_set_candidate[0]][state] = {state: {}}
            if last_name not in recipient[match_set_candidate[0]][state]:
                recipient[match_set_candidate[0]][state][last_name] = 0

            recipient[match_set_candidate[0]][state][last_name] += 1
            f.write(json.dumps(recipient))
        else:
            self.__get_pretty_printer__().pprint("Candidate not found in :" + str(tokens))

        # Naive, slower implementation
        # for candidate in rest.CANDIDATE_LIST:
        #     if candidate in tokens:
        #         recipient[candidate][state][last_name] += 1
        #         # self.__get_pretty_printer__().pprint(recipient)
        #     else:
        #         self.__get_pretty_printer__().pprint("Candidate not found in :" + str(tokens))

        f.close()

        with open('recipient.pickle', 'a+b') as f:
            pickle.dump(recipient, f)

        self.__get_pretty_printer__().pprint(recipient)

        self.recipient = recipient
