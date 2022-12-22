rd_file = open("C:/Users/gmass/Documents/UC Berk Bootcamp/Classes/W3_1_Python/YouTube Python Practice/ReadingFiles1.txt", "r")

print(rd_file.readable())

rd_file.close()


rd_file = open("C:/Users/gmass/Documents/UC Berk Bootcamp/Classes/W3_1_Python/YouTube Python Practice/ReadingFiles1.txt", "r")

print(rd_file.read())

rd_file.close()

rd_file = open("C:/Users/gmass/Documents/UC Berk Bootcamp/Classes/W3_1_Python/YouTube Python Practice/ReadingFiles1.txt", "r")

print(rd_file.readline())
print(rd_file.readline())

rd_file.close()

rd_file = open("C:/Users/gmass/Documents/UC Berk Bootcamp/Classes/W3_1_Python/YouTube Python Practice/ReadingFiles1.txt", "r")

print(rd_file.readlines()[1])

rd_file.close()

rd_file = open("C:/Users/gmass/Documents/UC Berk Bootcamp/Classes/W3_1_Python/YouTube Python Practice/ReadingFiles1.txt", "r")
for employee in rd_file.readlines():
    print(employee)

rd_file.close()

