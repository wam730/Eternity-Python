p1 = [3,1,4,2,5,3,2,3,3,2,2,0,3,3,2,5,0,0,3,1,3,4,3,3,5,2,3,4,4,0,1,2,0,1,3,0,\
      2,0,3,2,3,0,0,0,4,3,1,0,4,2]
p = dict()
temp = 0
for i in range(0,10):
     for j in range(0,5):
               p[(i,j)] = int(p1[temp])
               temp += 1

Time = float('inf')
for x1 in range(0,11):
     for y1 in range(0,6):
          for x2 in range(x1,11):
               for y2 in range(y1,6):
                    T = 0
                    for i in range(0,10):
                         for j in range(0,5):
                              t1 = 15*abs(x1-i-0.5)+20*abs(y1-j-0.5)-17.5
                              t2 = 15*abs(x2-i-0.5)+20*abs(y2-j-0.5)-17.5
                              t = min(t1,t2)*int(p[(i,j)])
                              T = T + t
                    print('({:2},{:2}) 与 ({:2},{:2}) 所对应的响应时间是 {}'\
                          .format(x1,y1,x2,y2,T))
                    if T < Time:
                         Time = T
                         Place1 = (x1,y1)
                         Place2 = (x2,y2)
                    else:
                         continue
                    

print('{} 和 {} 是最佳建设地点，其响应时间最小，为 {}'.format(Place1,Place2,Time))
                                   
