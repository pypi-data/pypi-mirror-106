import sys
import argparse

from uncle_ben.repository import Repository
from uncle_ben.results import Results
from uncle_ben.logging import enable_debug

parser = argparse.ArgumentParser()
parser.add_argument("targets", nargs='+')
parser.add_argument("-o", "--output", default=None,
                    help="File to write output.")
output_format = parser.add_mutually_exclusive_group()

output_format.add_argument("--table", action="store_true", default=True,
                           help="Write results to a formatted table (default)")
output_format.add_argument("--csv", action="store_true", default=False,
                           help="Write results into a CSV format")
output_format.add_argument("--json", action="store_true", default=False,
                           help="Write results to json")
parser.add_argument("--debug", action="store_true", default=False,
                    help="Enable debug logging")

arguments = parser.parse_args()
if arguments.debug:
    enable_debug()
results = Results()
for target in arguments.targets:
    repository = Repository(target)
    results.add(target, repository.complete_analysis())

if arguments.output:
    output = open(arguments.output, "w")
else:
    output = sys.stdout

if arguments.json:
    print(results.json(), file=output)
elif arguments.csv:
    print(results.csv(), file=output)
elif arguments.table:
    print(results.string(), file=output)
output.close()
