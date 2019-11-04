def parse_connection_string(connection_string):
    str_dict = dict(dialect="",
                    driver="",
                    username="",
                    password="",
                    host="",
                    port="",
                    database="")
    i = connection_string.split(':')[0].strip().strip('"')
    if i == "sqlite3":
        str_dict["dialect"] = i
        str_dict["database"] = connection_string.split('/', maxsplit=3)[-1]
    elif i.startswith("postgresql"):
        str_dict["dialect"] = "postgresql"
        x = i[11:].strip()
        if x:
            str_dict["driver"] = x
        y = connection_string.split('/', maxsplit=3)
        str_dict["database"] = y[-1]
        z1 = y[-2]
        str_dict["host"] = z1.split('@')[-1]
        z = z1[:len(str_dict["host"])]
        str_dict["username"] = z.split(":")[0]
        str_dict["password"] = z.split(":")[1]
    elif i == "m2sql":
        str_dict["dialect"] = i
        y = connection_string.split('/', maxsplit=3)
        str_dict["database"] = y[-1]
        z = y[-2]
        str_dict["username"] = z.split(":")[0]
        str_dict["password"] = z.split(":")[1]

    return str_dict