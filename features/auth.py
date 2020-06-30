# read user and pass
with open(".config", "r") as configfile:
    userpass = configfile.read().replace('\n', ',')
configfile.close()