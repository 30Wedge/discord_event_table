"""
File holds all the commands
"""
import random
import logging
from table_wrapper import Table

class Commands:
    ###### Commands - take list of string args, return string to send to chat
    def hello(self, args):
        return 'Hello!'

    def help(self, args):
        return 'commands: ' + ''.join(["\n\t" + k for k in self.cmd_table.keys()])

    def add_to_table(self, args):
        self.encounter_table.set(args[0], ' '.join(args[1:]))
        return "Added to table"

    def get_from_table(self, args):
        k = args[0]
        val = self.encounter_table.get(k)
        s = "[{}]: {}\n".format(k, val)
        return s

    def build_table(self, args):
        """build the epic encounter table from an array of message objects
        new epic enocunters follow the format: "!encounterName Contents..."
        """
        for m in args:
            content = m['content']
            # validate a little bit
            if content.startswith("!") and len(content.split(' ')) >= 2:
                # push into the table
                evt = content.split(' ')[0][1:]
                val = ' '.join(content.split(' ')[1:])
                self.encounter_table.set(evt, val)
        return "Table Built"

    def print_table(self, args):
        s = "---\n"
        for k in self.encounter_table.keys():
            s += "  [{}]\n".format(k)
        s += "---\n"
        return s

    def random_encounter(self, args):
        k, val = self.encounter_table.random_get()
        # format [event]: Description
        s = "[{}]: \n\t{}\n".format(k, val)
        return s

    def roll(self, args):
        r = random.randrange(1, 20)
        if r == 20:
            return self.random_encounter
        else:
            return "No Encounter - Rolled [{}]".format(r)

    # Higher level stuff
    def __init__(self, table: Table):
        """set up state required for commands"""
        # TODO make this threadsafe?
        self.encounter_table = table
        # commented out commands that just aren't ready
        self.cmd_table = {
            #"build_table": self.build_table,
            #"build": self.build_table,
            "add": self.add_to_table,
            "get": self.get_from_table,
            "print": self.print_table,
            #"roll_encounter": self.roll,
            #"roll": self.roll,
            #"random_encounter": self.random_encounter,
            "rand": self.random_encounter,
            "hello": self.hello,
            "help": self.help,
        }

    def get_cmd_table(self):
        return self.cmd_table

    def run_cmd(self, command, args):
        """Dispatch a command"""
        if command in self.cmd_table:
            return self.cmd_table[command](args)
        else:
            logging.info(f"Command: {command} not found")
            return ''


if __name__ == "__main__":
    # minimal message objets
    td = [{"content": "!DukesNewHat Duke finds a new hat"},
          {"content": "!tiberius dies from finger of death"},
          {"content": "!CrixusWizard A wizard from down the road appears"},
          {"content": "!malformed"},
          {"content": "not a command"},
          ]
    print("empty table:")
    from table_wrapper import TestingTable
    tt = TestingTable("n")
    c = Commands(tt)
    print(c.print_table({}))
    print(c.roll({}))
    print(c.build_table(td))
    print("built table:")
    print(c.print_table({}))
    print("random encounter:")
    print(c.random_encounter({}))
    print("TEST DONE:")
    print(c.run_cmd("hello", ['']))
    print(c.run_cmd("add", ['EVENT', 'ACTION']))
    print(c.run_cmd("help", ['EVENT', 'ACTION']))
