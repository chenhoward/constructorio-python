import sys
import os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')
# hack for easy import of the library

import csv
from constructorio import ConstructorIO

if __name__ == "__main__":
    api_token = raw_input("enter api token (enter q to quit) : ")
    if api_token == "q":
        print "toodles!"
        sys.exit(0)
    autocomplete_key = raw_input("enter autocomplete key (enter q to quit) : ")
    if autocomplete_key == "q":
        print "toodles!"
        sys.exit(0)
    autocomplete_section = raw_input("enter autocomplete section (enter q to quit) : ")
    if autocomplete_section == "q":
        print "toodles!"
        sys.exit(0)
    constructor = ConstructorIO(api_token, autocomplete_key) # is that right?
    with open("example.csv") as csv_file:
        example_csv = csv.DictReader(csv_file)
        for row in example_csv:
            print "row: ", row
            print "sending this row over to your Constructor.io account..."
            constructor.add(row["term"],
                            autocomplete_section,
                            score=row["score"])