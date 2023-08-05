import os
import argparse

def parseArgs(**kwargs):
    top_parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    top_parser.add_argument("-d","--assgn_dir", default=os.getcwd(), help="Marking directory (Default: current)")
    top_parser.add_argument("-c","--config", default=None, help="Location of config file (Default: assgn_dir/config.yml)")
    top_parser.add_argument("-s","--src_dir", default=None, help="Location of source files (Default: assgn_dir)")

    args, unknown = top_parser.parse_known_args()
    args = vars(args)


    for key, value in kwargs.items():
        args[key] = value

    if args["config"] is None:
        args["config"] = os.path.join(args["assgn_dir"], "config.yml")
    if args["src_dir"] is None:
        args["src_dir"] = args["assgn_dir"]

    for key, val in args.items():
        args[key] = os.path.abspath(val)

    return args