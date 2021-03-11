from scipy import  stats

number = int(input())
data = input()
main_data = data.split()
# data.append(input())
# print(sum(data))

data =[]
for i in main_data:
    data.append(int(i))
print(sum(data)/number)
# mean = 0
# for i in range(len(data)):
#     mean = mean + int(data[i])
# print(mean/number)

median = sorted(data)
# print(median)
if len(data)%2==1:
    print(median[len(data)//2])
elif len(data)%2==0:
    print((int(median[(len(data)//2)-1])+int(median[(len(data)//2)]))/2)

print(stats.mode(median)[0][0])


