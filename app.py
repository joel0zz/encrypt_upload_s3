import sys

from config import UI_CONFIG
from src.argutils import parse_args
from src.awsutils import Secret


def main(user_input_args):
    user_args = parse_args(UI_CONFIG, user_input_args)
    secret = Secret(user_args.secret, user_args.bucket, user_args.alias, user_args.profile, user_args.name)
    secret.upload_secret()
    

if __name__ == '__main__':
    main(sys.argv[1:])