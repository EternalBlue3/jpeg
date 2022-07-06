import sys

write, read = False, False
writeread = input("Write or read: ").lower()
filename = input("Enter the name of the jpeg: ")
if writeread == "write":
    write = True
    comment = input("Enter a comment: ")
    if comment == "makeitbig":
        comment = "LOLOLOLOLOL" * 70000000
elif writeread == "read":
    read = True
else:
    sys.exit()


if write:
    file = open(f"{filename}", "a+b")
    a = f"\xff\xfeCOMMENT:{comment}"
    file.write(a.encode())

if read:
    try:
        file = open('image.jpg',"rb")
        a = str(file.read())
        v = a.index("COMMENT:")
        out = ""
        for x in range(v,len(a)):
            out += a[x]

        out = out.replace('COMMENT:','')
        out = out.replace("'","")
        out = out.replace("\\xc3\\xbf\\xc3\\xbe","")
        print(out)
    except:
        pass

file.close()
