def parse_connection_string(connection_string):
    """
    Принимает на вход строку соединения connection_string и возвращает словарь с ее составными частями
    """
    db_dict = {"dialect": "", "driver": "", "username": "", "password": "", "host": "", "port": "", "database": ""}

    connection_string = connection_string.split("://")

    if "sqlite3" in connection_string[0]:
    	db_dict["dialect"] = "sqlite3"
    	part_two_db = connection_string[1].split("/")
    	db_dict["database"] = part_two_db[1]
    	return  db_dict
    elif "postgresql" in connection_string[0]:
    	db_dict["dialect"] = "postgresql"
    	part_one = connection_string[0].split('+')    	
    	if len(part_one) >= 2:
    		db_dict["driver"] = part_one[1]
    	part_two = connection_string[1].split("@")
    	part_two_user_list = part_two[0].split(":")
    	db_dict["username"] = part_two_user_list[0]
    	db_dict["password"] = part_two_user_list[1]
    	part_two_db_host = part_two[1]
    	part_two_db_host = part_two_db_host.split("/")
    	db_dict["host"] = part_two_db_host[0]
    	db_dict["database"] = part_two_db_host[1]    	    	
    	return db_dict
    elif "m2sql" in connection_string[0]: 
    	db_dict["dialect"] = "m2sql"
    	if "@" in connection_string[1]:
    		part_two = connection_string[1].split("@")
    		part_two_user_list = part_two[0].split(":")
    		db_dict["username"] = part_two_user_list[0]
    		db_dict["password"] = part_two_user_list[1]
    		part_two_db_host = part_two[1]
    		part_two_db_host = part_two_db_host.split("/")
    		db_dict["host"] = part_two_db_host[0]
    		db_dict["database"] = part_two_db_host[1] 
    	else:
    		part_two = connection_string[1].split("/")
    		part_two_user_list = part_two[0].split(":")
    		db_dict["username"] = part_two_user_list[0]
    		db_dict["password"] = part_two_user_list[1]
    		db_dict["database"] = part_two[1]
    	return db_dict