import discord


class EncouterClient(discord.Client):
    """interract with the channel from the resful API"""

    def __init__(self, guild):
        self.target_guild = guild
        super().__init__()

    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))
        for guild in self.guilds:
            if guild.name == self.target_guild:
                break
            print(f"{self.user} is connected to the following guild:\n "
                  f"{guild.name} + {guild.id}")

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))

    def seed_encouter_table(self, num_encounters=100):
        """Get 100 messages that start with"""
        encounters = []
        while len(encounters) < num_encounters:
            break
            # TODO Call the Restful API until we have 100 messages starting with !
            pass
        return encounters

    def run_command(self, msg):
        # TODO call on new message from discord channel,
        # TODO check for command in cmd_table and dispatch it
        pass

    def install_command(self, label, fn):
        """Add a command to the table
        fn is a function that takes a json string as its only arg"""
        entry = {label: fn}
        self.cmd_table.update(entry)

if __name__ == "__main__":

    from conf_loader import load_conf
    conf = load_conf()

    c = EncouterClient("City of Dreams")
    c.run(conf['bot_token'])
    print("No Test yet")

