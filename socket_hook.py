def SocketHook():
    """Get new messages in real time to check for commands to roll/refresh/print the table
    using the WebSocket API
    """

    def __init__(self, channel):
        #TODO give it a channel object, set up a websocket listening for new
        # messages- install 'on_command' as callback
        self.cmd_table = {}
        pass

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
