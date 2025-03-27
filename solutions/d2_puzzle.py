# 7 6 4 2 1: Safe because the levels are all decreasing by 1 or 2.
# 1 2 7 8 9: Unsafe because 2 7 is an increase of 5.
# 9 7 6 2 1: Unsafe because 6 2 is a decrease of 4.
# 1 3 2 4 5: Unsafe because 1 3 is increasing but 3 2 is decreasing.
# 8 6 4 4 1: Unsafe because 4 4 is neither an increase or a decrease.
# 1 3 6 7 9: Safe because the levels are all increasing by 1, 2, or 3.

def parsing_puzzle2():
    """
    OUTPUT format:
        list[list[int]]: list of list of integers
    """
    parsed_data = []
    with open('d2_puzzle_input.txt', 'r') as file:
        data = file.read().splitlines()
    for line in data:
        splitted = line.split(' ')
        parsed_data.append([int(e) for e in splitted])
    return parsed_data

def is_monotone(report:list[int])->bool:
    return all(report[i] < report[i + 1] for i in range(len(report) - 1)) or all(report[i] > report[i + 1] for i in range(len(report) - 1))

def low_diff_level(report:list[int], diff:int=3)->bool:
    return all(abs(report[i] - report[i + 1]) <= 3 for i in range(len(report) - 1))

def is_safe(report:list[int])->bool:
    return is_monotone(report) and low_diff_level(report)

def count_safe(parsed:list[list[int]])->int:
    return sum([is_safe(report) for report in parsed])

def main1():
    parsed = parsing_puzzle2()
    print(f"len(parsed): {len(parsed)}")
    print(f"day 2 - puzzle 1 solution: {count_safe(parsed)}")


def dampener_problem(report:list[int])->bool:
    """
    is the report safe if one level is removed?
    """
    i = 0
    flag = False
    # print(f"report: {report}")
    while i < len(report) and not(flag):
        # print(f"new report {i} : {report[:i] + report[i+1:]}") 
        flag = flag or is_safe(report[:i] + report[i+1:])
        i += 1
    return flag

def count_safe_dampener(parsed:list[list[int]])->int:
    return sum([dampener_problem(report) for report in parsed])

def main2():
    parsed = parsing_puzzle2()
    print(f"len(parsed): {len(parsed)}")
    # count_safe_dampener(parsed[:5])
    print(f"day 2 - puzzle 2 solution: {count_safe_dampener(parsed)}")

if __name__ == '__main__':
    # main1()
    main2()