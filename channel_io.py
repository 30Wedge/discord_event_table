import discord
import logging
from commands import Commands

class EncouterClient(discord.Client):
    """interract with the channel from the resful API"""

    def __init__(self, guild, cmd_handlers : Commands):
        """
        :param guild:
        :param cmd_handlers: Commands object or none
        """
        self.target_guild = guild
        self.cmds = cmd_handlers
        super().__init__()

    async def on_ready(self):
        self.guild = discord.utils.find(lambda g: g.name == self.target_guild, self.guilds)
        logging.debug('Logged on as {0}!'.format(self.user))
        logging.info(f"{self.user} is connected to the following guild:\n "
              f"{self.guild.name} + {self.guild.id}")

    async def on_message(self, message):
        #no self-talk
        if message.author == self.user:
            return

        logging.info('Message from {0.author}: {0.content}'.format(message))

        # test for commands
        if "!" in message.content:
            # get command
            cmd = message.content.split('!')[0]
            cmd = cmd.split(' ')[-1]
            # get args
            args = '!'.join(message.content.split('!')[1:])
            args = args.split(' ')[1:]

            res = self.run_command(cmd, args)
            if res != '':
                await message.channel.send(res)

    def seed_encouter_table(self, num_encounters=100):
        """Get 100 messages that start with"""
        encounters = []
        while len(encounters) < num_encounters:
            break
            # TODO Call the Restful API until we have 100 messages starting with !
            pass
        return encounters

    def run_command(self, cmd, args):
        """
        call on new message from discord channel,
        check for command in cmd_table and dispatch it
        return string to respond with
        """
        return self.cmds.run_cmd(cmd, args)


    def install_command(self, label, fn):
        """Add a command to the table
        fn is a function that takes a json string as its only arg"""
        entry = {label: fn}
        self.cmd_table.update(entry)

if __name__ == "__main__":
    logger = logging.getLogger(__name__)
    logging.basicConfig(level=logging.DEBUG)
    from conf_loader import load_conf
    conf = load_conf()
    logging.debug("Created command dispatcher")
    cmds = Commands()

    logging.debug("Conecting to test....")
    c = EncouterClient("City of Dreams", cmds)
    c.run(conf['bot_token'])

    logging.debug("No Test yet")

