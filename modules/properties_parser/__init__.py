def parse(properties=str):
    properties = properties.split("\n")
    result = {}
    for i in properties:
        if not i.startswith("#"):
            try:
                result[i.split("=", 1)[0]] = int(i.split("=", 1)[1])
            except:
                result[i.split("=", 1)[0]] = i.split("=", 1)[1]
    return result