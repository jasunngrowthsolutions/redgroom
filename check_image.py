with open("Ram Hanuman - CSO.jpeg","rb") as f: header=f.read(10)
print("JPEG start:", header[:2]==b'\xff\xd8')
