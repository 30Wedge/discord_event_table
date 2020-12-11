"""
File holds all the commands
"""
import random

class Commands:
    ###### Commands
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
                self.encounter_table[evt] = val
        pass

    def print_table(self, args):
        s = ""
        for k, v in self.encounter_table.items():
            s += "[{}]: {}\n".format(k, v)
        return s

    def random_encounter(self, args):
        k = random.choice(list(self.encounter_table.keys()))
        # format [event]: Description
        s = "[{}]: \n\t{}\n".format(k, self.encounter_table[k])
        return s

    def roll(self, args):
        r = random.randrange(1, 20)
        if r == 20:
            return self.random_encounter
        else:
            return "No Encounter - Rolled [{}]".format(r)

    def __init__(self):
        """set up state required for commands"""
        self.encounter_table = {}
        self.cmd_table = {
            "build_table": self.build_table,
            "build": self.build_table,
            "print_table": self.print_table,
            "print": self.print_table,
            "roll_encounter": self.roll,
            "roll": self.roll,
            "random_encounter": self.random_encounter,
            "rand": self.random_encounter,
        }

    def get_cmd_table(self):
        return self.cmd_table


if __name__ == "__main__":
    # minimal message objets
    td = [{"content": "!DukesNewHat Duke finds a new hat"},
          {"content": "!tiberius dies from finger of death"},
          {"content": "!CrixusWizard A wizard from down the road appears"},
          {"content": "!malformed"},
          {"content": "not a command"},
          ]
    print("empty table:")
    c = Commands()
    print(c.print_table({}))
    print(c.roll({}))
    print(c.build_table(td))
    print("built table:")
    print(c.print_table({}))
    print("random encounter:")
    print(c.random_encounter({}))
    print("TEST DONE:")
