def write(fileName):
    fw= open(fileName+".txt",'w')
    fw.write("Trying file write\n")
    fw.write("Yaaahhh biatch, it's done")
    fw.close()
