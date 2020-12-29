def _load_kv_conf(fn):
    """load config from a key-value file (each line is: key=value)"""
    conf={}
    with open(fn) as f:
        for l in f.readlines():
            if l.startswith('#'):
                continue
            toks = l.split('=')
            if len(toks) == 2:
                 conf[toks[0]] = toks[1].strip()
    return conf


def load_conf(secret_file="secrets.conf", discord_file="discord.conf"):
    """ load config from files, and return as dict"""
    c = {}
    # local conf filea
    try:
        c.update(_load_kv_conf(secret_file))
    except Exception:
        print("Error loading secrets")
    try:
        c.update(_load_kv_conf(discord_file))
    except Exception:
        print("Error loading secrets")

    return c


if __name__ == "__main__":
    d = load_conf()
    print(d)