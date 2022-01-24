def get_data(path: str) -> list:
    result = []
    with open(path, 'r') as filetarget:
        for line in filetarget:
            result.append(list(map(int, line.split(' '))))
    return result

import math
def analyze_data(numbers: list, options: str) -> float:
    list = numbers[0]+numbers[1]

    if options == "average":
        print(sum(list)/ len(list))

    elif options == "standard deviation":
        mean = sum(list) / len(list)
        print(math.sqrt(sum([(x - mean)**2 for x in list])/len(list)))

    elif options == "covariance":
        mean_0 = sum(numbers[0]) / len(numbers[0])
        mean_1 = sum(numbers[1]) / len(numbers[1])
        sub_0 = [i - mean_0 for i in numbers[0]]
        sub_1 = [i - mean_1 for i in numbers[1]]
        numerator = sum([sub_0[i]*sub_1[i] for i in range(len(sub_0))])
        denominator = len(list[0])
        print(numerator / denominator)

    elif options == "correlation":
        mean_0 = sum(numbers[0]) / len(numbers[0])
        mean_1 = sum(numbers[1]) / len(numbers[1])
        sub_0 = [i - mean_0 for i in numbers[0]]
        sub_1 = [i - mean_1 for i in numbers[1]]
        numerator = sum([sub_0[i] * sub_1[i] for i in range(len(sub_0))])
        std_0 = sum(sub_0[i]**2 for i in range(len(sub_0)))
        std_1 = sum(sub_1[i]**2 for i in range(len(sub_1)))
        denominator = math.sqrt(std_0*std_1)
        print(numerator / denominator)
    
    else:
        print("Try again.")

