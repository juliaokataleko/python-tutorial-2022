# read file
f = open('files/my_data.txt', 'r')
# print(f.read())
# print(f.readline(4), end="")
# print(f.readline())

### create new file ###
# f1 = open('files/abc.txt', 'w')
# f1.write("New file created with py")
# f1.write("Laptop")

# append content
f1 = open('files/abc.txt', 'w')
# f1.write("New Laptop")

# copy data from one file to another

for data in f:
    # print(data)
    # add data to new file
    f1.write(data)

# if is an img we have to use rb instead of r, or wb instead of w
file = open('files/IMG_20151019_105743.jpg', 'rb')
file1 = open('files/imgs/my_pic.jpg', 'wb')

for i in file:
    file1.write(i)