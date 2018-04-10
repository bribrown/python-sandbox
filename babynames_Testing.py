import re
import os

def get_year(filename):
    os.chdir('C:\\Users\\bbrownholtz\\PycharmProjects\\google-python-exercises\\babynames')
    f = open(filename, 'r')
    pop_year = re.search(r'Popularity in (\d\d\d\d)', f.read())

    if pop_year:
        return(pop_year.group(1))

def pick_last_element(tup):
    return tup[-1]

def main():

    # Extract the year and print it

    print(get_year('baby1990.html'))
    print()

    # Extract the names and rank numbers and just print them

    os.chdir('C:\\Users\\bbrownholtz\\PycharmProjects\\google-python-exercises\\babynames')
    f = open('baby1990.html', 'r')
    rank_name = re.findall(r'<tr align="right"><td>(\d+)</td><td>(\w+)</td><td>(\w+)</td>', f.read())

    i = 0

    while i < len(rank_name):
        print('Rank: {} Boy Name: {} Girl Name: {}'.format(rank_name[i][0], rank_name[i][1], rank_name[i][2]))
        i += 1

    # Get the names data into a dict and print it

    f = open('baby1990.html', 'r')
    rank_name = re.findall(r'<tr align="right"><td>(\d+)</td><td>(\w+)</td><td>(\w+)</td>', f.read())

    i = 0
    name_rank_dict = {}

    print()

    while i < len(rank_name):
        name_rank_dict[rank_name[i][0]] = [rank_name[i][1], rank_name[i][2]]
        i += 1

    print(name_rank_dict)
    print()

    # Build the [year, 'name rank', ... ] list and print it
    # ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', '...]

    year_name_rank = []
    alpha_name_rank = []
    final_name_rank = []
    final_list = []

    year_name_rank.append(get_year('baby1990.html'))

    for key, value in name_rank_dict.items():
        alpha_name_rank.append([key, value])

    i = 0
    while i < len(alpha_name_rank):
        rank_pair = (alpha_name_rank[i][0],alpha_name_rank[i][1][0])
        final_name_rank.append(rank_pair)
        rank_pair = (alpha_name_rank[i][0], alpha_name_rank[i][1][1])
        final_name_rank.append(rank_pair)
        i += 1

    sorted_list = sorted(final_name_rank, key=pick_last_element)

    final_list.append(year_name_rank[0])

    i = 0
    while i < len(sorted_list):
        rank_plus_name = (sorted_list[i][1] + ' ' + sorted_list[i][0])
        final_list.append(rank_plus_name)
        i += 1

    print(final_list)

    f.close()

if __name__ == '__main__':
  main()