from .lexer import *
from .topython import *
from . import __version__
import argparse
from .tracker import Tracker
from traceback import print_exc
import os
def main():
    
    parser = argparse.ArgumentParser(description="ECP interpreter")
    parser.add_argument("inputfile", type=argparse.FileType("r", encoding="utf-8"), nargs="?")
    parser.add_argument("--debug", action="store_true", help="show debug information like token list")
    parser.add_argument("--trace", action="store", nargs="*", default=[], help="space seperated names of the variables to be traced")
    parser.add_argument("--tracecompact", action="store_true", help="trace compactly")
    parser.add_argument("--topython", action="store_true", help="Try to convert the ECP program to python source code")
    parser.add_argument("--pause", action="store_true", help="pause on completion")
    parser.add_argument('--version', action='version', version='%(prog)s v'+__version__)

    options = parser.parse_args()
    should_trace = len(options.trace) > 0
    #print(options)
    if options.inputfile:
        string = options.inputfile.read()
        loc = os.path.dirname(os.path.abspath(options.inputfile.name))
        name = os.path.basename(options.inputfile.name)
        options.inputfile.close()

        def debugOutput(result):
            table = []
            for i in result.tokens:
                table.append([i.value, i.type])
            print(tabulate(table, tablefmt="github", headers=["VALUE", "TYPE"]))

        if options.debug:
            pass
            #debugOutput(result)
        sys.path.insert(0, loc)
        if options.topython:
            print(to_py_source(string))
        else:
            ecp(string, name=name, scope=globals(), trace=options.trace, tracecompact=options.tracecompact)
        if options.pause:
            input("Press enter to exit...")

    else:
        # Live console
        print(f"ECP {__version__}")
        string = ""
        multiple_line = False
        prompt = ">>> "
        while True:
            if not multiple_line:
                string = input(">>> ")
                multiple_line = string.endswith("\\")
                if multiple_line:
                    string = string[:-1]
                    string += "\n"

            while multiple_line:
                string += input("... ")
                multiple_line = string.endswith("\\")
                if multiple_line:
                    string = string[:-1]
                    string += "\n"

            try:
                ecp(string, name="<stdin>", scope=globals())
            except:
                print_exc(0)

if __name__ == "__main__":
    main()