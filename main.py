import module
import fileManager
print("Test age")
age = 19
if age > 18:
    print("Eligible to vote")
else:
    print("Cant vote")

name=['Arjun','Nitheen','Rajesh','Baka']
for n in name:
    if n.__contains__("A") or n.__contains__("a"):
        continue
    print(n)

module.webscrapper()
fileManager.write('Test')