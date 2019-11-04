def parse_connection_string(connection_string):


	dict_ = {
		"dialect": "",
		"driver": "",
		"username": "",
		"password": "",
		"host": "",
		"port": "",
		"database": ""
	}

	a = connection_string.split(":")
	if a[0].startswith("sqlite") == True:
		dict_["dialect"] = a[0]
		dict_["database"] = a[1].lstrip("///")
	else:
		if "+" in a[0] and "@" in a[2]:
			b = a[0].split("+")
			dict_["dialect"] = b[0]
			dict_["driver"] = b[1]
			dict_["username"] = a[1].lstrip("//")
			c = a[2].split("@")
			d = c[1].split("/")
			dict_["password"] = c[0]
			dict_["host"] = d[0]
			dict_["database"] = d[1]
		else:
			dict_["dialect"] = a[0]
			dict_["username"] = a[1].lstrip("//")
			d1 = a[2].split("/")
			dict_["password"] = d1[0]
			dict_["database"] = d1[1]

	return(dict_)