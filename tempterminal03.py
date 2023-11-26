user = open("users\\{0}.batdata".format("test"), "a+")
user.seek(0)
user_data_packets = user.readlines()
print (user_data_packets)
user.truncate(0)
user.seek(0)
print(user.readlines())
user.seek(0)
user_data_packets[0] = "username = test\n"
user_data_packets[1] = "password = hallelujah\n"
print(user.readlines())
user.writelines(user_data_packets)
user.close()