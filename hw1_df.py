
def get_data(path):
    result = []
    with open(path, 'r') as filetarget:
        for line in filetarget:
            result.append(list(map(int, line.split(' '))))
    return result

import math
def analyze_data(numbers, options):
    list = numbers[0]+numbers[1]
    
#find the average
    if options == "average":
        print(sum(list)/ len(list))
#find standard deviation
    elif options == "standard deviation":
        mean = sum(list) / len(list)
        print(math.sqrt(sum([(x - mean)**2 for x in list])/len(list)))
        
#find covariance
    elif options == "covariance":
        mean_0 = sum(list[0]) / len(list[0])
        mean_1 = sum(list[1]) / len(list[1])
        sub_0 = [i - mean_0 for i in list[0]]
        sub_1 = [i - mean_1 for i in list[1]]
        numerator = sum([sub_0[i]*sub_1[i] for i in range(len(sub_0))])
        denominator = len(list[0])
        print(numerator / denominator)

#find correlation
    elif options == "correlation":
        mean_0 = sum(list[0]) / len(list[0])
        mean_1 = sum(list[1]) / len(list[1])
        sub_0 = [i - mean_0 for i in list[0]]
        sub_1 = [i - mean_1 for i in list[1]]
        numerator = sum([sub_0[i] * sub_1[i] for i in range(len(sub_0))])
        std_0 = sum(sub_0[i]**2 for i in range(len(sub_0)))
        std_1 = sum(sub_1[i]**2 for i in range(len(sub_1)))
        denominator = math.sqrt(std_0*std_1)
        print(numerator / denominator)
    
    else:
        print("Try again.")


