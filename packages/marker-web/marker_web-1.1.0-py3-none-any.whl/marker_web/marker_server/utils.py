import os
import argparse
from collections import defaultdict

def getArgsDefaults(**kwargs):
    args = defaultdict(lambda: None)

    for key, value in kwargs.items():
        args[key] = value

    if args["config"] is None:
        args["config"] = os.path.join(args["assgn_dir"], "config.yml")
    if args["src_dir"] is None:
        args["src_dir"] = args["assgn_dir"]

    for key, val in args.items():
        args[key] = os.path.abspath(val)

    return args