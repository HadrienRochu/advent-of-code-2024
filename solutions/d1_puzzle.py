


def parsing_puzzle():
    parsed_data = {'ligne1':[], "ligne2":[]}
    with open('d1_puzzle_input.txt', 'r') as file:
        data = file.read().splitlines()
    for e in data:
        splitted = e.split('   ')
        if len(splitted) >= 1:            
            parsed_data['ligne1'].append(int(splitted[0]))
            parsed_data['ligne2'].append(int(splitted[1]))
    return parsed_data


def tri_fusion(tab):
    if len(tab) <= 1:
        return tab
    else:
        milieu = len(tab) // 2
        gauche = tri_fusion(tab[:milieu])
        droite = tri_fusion(tab[milieu:])
        return fusion(gauche, droite)

def fusion(gauche, droite):
    resultat = []
    i = 0
    j = 0
    while i < len(gauche) and j < len(droite):
        if gauche[i] < droite[j]:
            resultat.append(gauche[i])
            i += 1
        else:
            resultat.append(droite[j])
            j += 1
    return resultat + gauche[i:] + droite[j:]

def diff_list(list1, list2):
    return sum([abs(list1[i] - list2[i]) for i in range(len(list1))])


def main1():
    parsed_data = parsing_puzzle()
    sorted_data = {
        'ligne1':tri_fusion(parsed_data['ligne1']),
        'ligne2':tri_fusion(parsed_data['ligne2'])
    }
    # print(f"len ligne1: {len(sorted_data['ligne1'])}")
    # print(f"len ligne2: {len(sorted_data['ligne2'])}")
    print(f"puzzle solution : {diff_list(sorted_data['ligne1'], sorted_data['ligne2'])}")


def parsing_puzzle2():
    parsed_data = {'ligne1':{}, "ligne2":{}}
    with open('puzzle_input_1.txt', 'r') as file:
        data = file.read().splitlines()
    for e in data:
        splitted = e.split('   ')
        if len(splitted) >= 1:
            # ligne 1
            if splitted[0] in parsed_data['ligne1']:
                parsed_data['ligne1'][splitted[0]] += 1
            else:
                parsed_data['ligne1'][splitted[0]] = 1
            # ligne 2
            if splitted[1] in parsed_data['ligne2']:
                parsed_data['ligne2'][splitted[1]] += 1
            else:
                parsed_data['ligne2'][splitted[1]] = 1
    return parsed_data

def product_list(list1, list2):
    return sum([int(e) * list1[e] * list2[e] for e in list1 if e in list2])

def main2():
    parsed_data = parsing_puzzle2()
    print(f"puzzle 2 solution : {product_list(parsed_data['ligne1'], parsed_data['ligne2'])}")


if __name__ == '__main__':
    main1()
    main2()