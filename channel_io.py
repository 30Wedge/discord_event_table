import discord

class EncouterClient(discord.Client):
    """interract with the channel from the resful API"""
    def __init__(self, channelId):
        #TODO - call GET method to get channel objects
        self.chan_obj
        pass

    def seed_encouter_table(self, num_encounters=100):
        """Get 100 messages that start with"""
        encounters = []
        while len(encounters) < num_encounters:
            break
            # TODO Call the Restful API until we have 100 messages starting with !
            pass
        return encounters

    def on_command(self, msg):
        # TODO call on new message from discord channel,
        # TODO check for command in cmd_table and dispatch it
        pass

    def install_command(self, label, fn):
        """Add a command to the table
        fn is a function that takes a json string as its only arg"""
        entry = {label: fn}
        self.cmd_table.update(entry)


if __name__ == "__main__":
    print("No Test yet")

