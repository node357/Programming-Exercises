dic1={1:10, 2:20} 
dic2={3:30, 4:40} 
dic3={5:50,6:60}

print dict(dic1.items() + dic2.items() + dic3.items())

dic0 = dict(dic1)
dic0.update(dic2)
dic0.update(dic3)

print dic0
