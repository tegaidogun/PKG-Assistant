from colorama import Fore

dash = '-'
comma = ','


def parse_ranges(ranges_num):
    comma = ","
    dash = "-"

    if comma in ranges_num:
        range_list = ranges_num.split(comma)
    else:
        range_list = [ranges_num]
    line_numbers = []
    for rng in range_list:
        if dash in rng:
            start, end = [int(x) for x in rng.split(dash)]
            line_numbers.extend(range(start, end + 1))
        else:
            line_numbers.append(int(rng))
    return sorted(line_numbers)

def parse_tsv_file(tsv_file, ranges):
    pkg_data = []

    with open(tsv_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    for i in ranges:
        data = lines[i].strip().split('\t')
        pkg_url = data[3]
        zrif = data[4]
        pkg_name = data[2]

        if pkg_url == "MISSING" or zrif == "MISSING":
            print(f"{Fore.RED}The {pkg_name} was skipped due to an missing link/zRIF key...{Fore.RESET}")
            continue

        pkg_data.append((pkg_url, zrif, pkg_name))

    return pkg_data
