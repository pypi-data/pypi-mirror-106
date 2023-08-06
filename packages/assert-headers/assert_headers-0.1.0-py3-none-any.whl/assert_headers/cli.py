import argparse
import json
import sys

from enum import Enum
from assert_headers import assertHeadersFromUrl, getMeta, HeaderAssertionError

def getConfiguration(configurationPath):
    configuration = {}
    with open(configurationPath, "r") as f:
        configurationStr = f.read()
        configuration = json.loads(configurationStr)
        return configuration

class ExitCodes(Enum):
    AssertionFailed = 2
    ConfigurationError = 3
    Success = 0
    UncaughtError = 1

def main():
    meta = getMeta()

    if "--version" in sys.argv:
        print(f'assert-headers-py v{meta["__version__"]}')
        sys.exit(ExitCodes.Success.value)

    parser = argparse.ArgumentParser(
        prog = meta["__title__"],
        description = meta["__summary__"]
    )

    # parser.add_argument("--version",
    #                     action="store",
    #                     help="Just print the version",
    #                     type=bool,
    #                     default=False)

    parser.add_argument("--config",
                        action="store",
                        help="Relative path to configuration file",
                        metavar="configurationPath",
                        type=str,
                        default="headersSchema.json")

    parser.add_argument("--silent",
                        action="store_const",
                        help="Don't output errors or headers",
                        const=True,
                        default=False)

    parser.add_argument("url",
                        action="store",
                        help="URL to retrieve headers from for assertion",
                        type=str)

    args = parser.parse_args()

    config = {}
    try:
        config = getConfiguration(args.config)
    except BaseException as err:
        if not args.silent:
            print(err["message"])
        
        sys.exit(ExitCodes.ConfigurationError.value)

    headers = {}
    try:
      headers = assertHeadersFromUrl(args.url, config)

    except HeaderAssertionError as headerAssertionError:
        if not args.silent:
            print(headerAssertionError["message"])
        
        sys.exit(ExitCodes.AssertionFailed.value)

    except BaseException as err:
        if not args.silent:
            print(err["message"])
        
        sys.exit(ExitCodes.UncaughtError.value)

    if not args.silent:
        print("assert-headers success\n")
        print(headers)

    sys.exit(ExitCodes.Success.value)
