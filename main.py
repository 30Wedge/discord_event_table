from conf_loader import load_conf
import argparse
import table_wrapper
import commands
import channel_io
import logging

logger = logging.getLogger(__name__)


def get_args():
    """Return command Line arguments as a dict"""
    args = argparse.ArgumentParser("Run the Random table bot")
    # TODO this is unused
    args.add_argument("--test", action="store_true", default=False, help="add to run on test channel")
    args.add_argument("-bucket", default="ericencountertable", help="AWS bucket name to use")
    # pop an "arg_" wart on the front of all variables
    return {"arg_"+k : v for k,v in vars(args.parse_args()).items()}


def main():
    # get config from command line + config files. let conf override CLI
    conf = get_args()
    conf.update(load_conf())

    # Create the AWS table instance
    t = table_wrapper.S3EventTable(conf['arg_bucket'])

    # create the command dispatcher
    cmds = commands.Commands(t)

    # create and start the discord listener
    c = channel_io.EncouterClient(conf['guild_name'], cmds)
    c.run(conf['bot_token'])


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    logging.info("Start")
    main()