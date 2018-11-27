dic1={1:10, 2:20} 
dic2={3:30, 4:40} 
dic3={5:50,6:60}

print dic1.get(3, "Key doesn't exist")

if not 3 in dic1:
    dic1.update({3: 30})

print dic1

