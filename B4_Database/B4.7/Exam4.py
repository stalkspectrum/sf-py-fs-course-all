def parse_connection_string(connection_string):

    base = {
        "dialect": "", 
        "driver": "", 
        "username": "", 
        "password": "", 
        "host": "", 
        "port": "", 
        "database": ""
        }

    if "sqlite" in connection_string.split(':')[0]:
        base["dialect"] = connection_string.split(':')[0]
        base["database"] = connection_string.split(':///')[1]
    else:
        if "+" in connection_string.split(':')[0]:
            base["dialect"] = connection_string.split(':')[0].split("+")[0]
            base["driver"] = connection_string.split(':')[0].split("+")[1]
        else:
            base["dialect"] = connection_string.split(':')[0].split("+")[0]
        if "@" in connection_string.split('://')[1]:
            base["username"] = connection_string.split('://')[1].split(":")[0]
            base["password"] = connection_string.split('://')[1].split("@")[0].split(":")[1]
            base["host"] = connection_string.split('@')[1].split("/")[0].split(":")[0]
            base["port"] = connection_string.split(':')[3].split('/')[0]
            base["database"] = connection_string.split('@')[1].split("/")[1]  
        else:
            base["username"] = connection_string.split('://')[1].split(":")[0]
            base["password"] = connection_string.split('://')[1].split("/")[0].split(":")[1]
            base["database"] = connection_string.split('://')[1].split("/")[1]
    return base

print(parse_connection_string("postgresql+psycopg2://admin:1234@example.com:4321/test"))