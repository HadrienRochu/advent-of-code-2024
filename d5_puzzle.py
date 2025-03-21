



def parsing_puzzle5():
    """
    creates :
        - rules: a dictionary with the rules for each page
            {page: {'before': [pages:string], 'after': [pages:string]}}
        - an updates: a list of ordered list of pages, list[list[string]]
    """
    rules = {}
    updates = []
    with open('d5_puzzle_input.txt', 'r') as file:
        data = file.read().splitlines()
    for line in data:
        if '|' in line:
            page, after = line.split('|')
            page = page.strip()
            after = after.strip()
            if page not in rules:
                rules[page] = {'before': [], 'after': []}
            rules[page]['after'].append(after)
            if after not in rules:
                rules[after] = {'before': [], 'after': []}
            rules[after]['before'].append(page)
        elif ',' in line:
            update = line.split(',')
            updates.append(update)
    return rules, updates

def is_valid_update(rules:dict, update:list[str])->bool:
    for i in range(len(update)):
        page = update[i]
        if page in rules:
            for before in update[:i]:
                # if not after in rules[page]['after']:
                if before in rules[page]['after']:
                    # not after in rules[page]['after'] or 
                    return False
    return True

def solve_puzzle51(rules:dict, updates:list[list[str]])->int:
    # puzzle_solution = 0
    # for update in updates:
    #     if is_valid_update(rules, update):
    #         puzzle_solution += int(update[len(update)//2+1])
    # return puzzle_solution
    return sum([int(update[len(update)//2]) for update in updates if is_valid_update(rules=rules, update=update)])

def main1():
    rules,updates = parsing_puzzle5()
    puzzle_solution = solve_puzzle51(rules, updates)
    print(f"day 5 - puzzle 1 solution: {puzzle_solution}")


def correct_update(rules:dict, update:list[str])->list[str]:
    i = 0
    while i < len(update):
        page = update[i]
        flag_change = False
        if page in rules:
            for j in range(i):
                before = update[j]
                if before in rules[page]['after']:
                    update[i] = before
                    update[j] = page
                    return correct_update(rules, update)
        if not flag_change:
            i += 1
    return update



def solve_puzzle52(rules:dict, updates:list[list[str]])->int:
    puzzle_solution = 0
    for update in updates:
        if not is_valid_update(rules=rules,update=update):
            update = correct_update(rules, update)
            puzzle_solution += int(update[len(update)//2])
    return puzzle_solution

def main2():
    rules,updates = parsing_puzzle5()
    puzzle_solution = solve_puzzle52(rules, updates)
    print(f"day 5 - puzzle 1 solution: {puzzle_solution}")


if __name__ == '__main__':
    # main1()
    main2()