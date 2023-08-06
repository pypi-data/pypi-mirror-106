import argparse
import os
import sys

from .server import app
from .auth import generate_auth_token
from .marker_server import setupMarker, getArgsDefaults
from . import PORT as DEFAULTPORT
import textwrap

def main():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument("-d","--assgn_dir", default=os.getcwd(), help="Marking directory (Default: current)")
    parser.add_argument("-c","--config", default=None, help="Location of config file (Default: assgn_dir/config.yml)")
    parser.add_argument("-s","--src_dir", default=None, help="Location of source files (Default: assgn_dir)")
    parser.add_argument("-p","--port", type=int, default=DEFAULTPORT, help="Port to use (local/remote)")
    parser.add_argument("-a", "--auth", action='store_const', const=True, default=False, help="Require authentication")
    parser.add_argument("-r","--remote", default=None, help="Remote host")
    parser.add_argument("-v", "--verbose", action='store_const', const=True, default=False, help="Enable logging for server")
    
    args = vars(parser.parse_args())

    marker_args = {}
    for key in ['assgn_dir', 'config', 'src_dir']:
        if key in args:
            marker_args[key] = args[key]

    verbose = args.get('verbose', False)
    PORT = args["port"]

    # Run on remote machine
    if args["remote"] is not None:
        cmd = f"ssh -t -t -L {PORT}:localhost:{PORT} {args['remote']} marker-web -p {PORT} -a"
        if verbose:
            cmd += " -v"

        os.system(cmd)
        sys.exit(0)

    if not verbose:
        import logging
        log = logging.getLogger('werkzeug')
        log.setLevel(logging.ERROR)


    # Otherwise, we are running locally....

    if args["auth"]:
        token = generate_auth_token(32)
        print(""*80)
        print("Generated token: ", token)
        print("-"*80)
        print(f"Running at: http://localhost:{PORT}/#/?auth={token}")
        print("-"*80)
    else:
        print("-"*80)
        print(f"Running at: http://localhost:{PORT}/")
        print("-"*80)

    marker_args = getArgsDefaults(**marker_args)
    setupMarker(marker_args)

    app.run(port=PORT)

if __name__ == '__main__':
    main()