#it's only for testing some parts of pifagor.py

def data_request_and_check():
	c = 1
	while c:
		k = input("дата рождения в формате дд.мм.гггг: ")
		if len(k) == 10:
			if k[2] == "." and k[5] == ".":
				c = 0

	return k

i = data_request_and_check()
print(i)


