from conf_loader import load_conf
import argparse

def get_args():
    """Return command Line arguments as a dict"""
    args = argparse.ArgumentParser("Run the Random table bot")
    args.add_argument("--test", action="store_true", default=False, help="add to run on test channel")
    # pop an "arg_" wart on the front of all variables
    return {"arg_"+k : v for k,v in vars(args.parse_args()).items()}

def main():
    # get config from command line + config files. let conf override CLI
    conf = get_args()
    conf.update(load_conf())
    print(conf)

if __name__ == "__main__":
    main()