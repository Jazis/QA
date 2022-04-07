def getFromConfig(record, configFile = "../../config.ini"):
    with open(configFile, "r") as file:
        for line in file:
            if "[" + record + "]" in line:
                out = line.split(" = ")[1]
    return out.replace("\n", "")