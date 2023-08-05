KEYRING_SERVICE = "vivotek-focus"

import argparse, keyring
from . import focus

parser = argparse.ArgumentParser()

parser.add_argument("netloc")
parser.add_argument("focus", type=int)

parser.add_argument("--no-https", action="store_true")
parser.add_argument("--no-https-verify", action="store_true")

args = parser.parse_args()


credentials = keyring.get_credential(KEYRING_SERVICE, None)

if credentials is None:
    import getpass

    username = input("Username: ")
    password = getpass.getpass("Password: ")
else:
    username = credentials.username
    password = credentials.password

success:bool = focus(args.netloc, args.focus, username, password, https=(not args.no_https), verify=(not args.no_https_verify))

if success:
    print("Success")
else:
    print("Failure")