#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os

def get_year(filename):
    os.chdir('C:\\Users\\bbrownholtz\\PycharmProjects\\google-python-exercises\\babynames')
    f = open(filename, 'r')
    pop_year = re.search(r'Popularity in (\d\d\d\d)', f.read())

    if pop_year:
        return(pop_year.group(1))

    f.close()

def pick_last_element(tup):
    return tup[-1]


# """Baby Names exercise
#
# Define the extract_names() function below and change main()
# to call it.
#
# For writing regex, it's nice to include a copy of the target
# text for inspiration.
#
# Here's what the html looks like in the baby.html files:
# ...
# <h3 align="center">Popularity in 1990</h3>
# ....
# <tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
# <tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
# <tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
# ...
#
# Suggested milestones for incremental development:
#  -Extract the year and print it
#  -Extract the names and rank numbers and just print them
#  -Get the names data into a dict and print it
#  -Build the [year, 'name rank', ... ] list and print it
#  -Fix main() to use the extract_names list
# """

def extract_names(filename):
  """
  Given a file name for baby.html, returns a list starting with the year string
  followed by the name-rank strings in alphabetical order.
  ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
  """
  # +++your code here+++
  os.chdir('C:\\Users\\bbrownholtz\\PycharmProjects\\google-python-exercises\\babynames')
  f = open(filename, 'r')
  rank_name = re.findall(r'<tr align="right"><td>(\d+)</td><td>(\w+)</td><td>(\w+)</td>', f.read())

  i = 0
  name_rank_dict = {}

  while i < len(rank_name):
      name_rank_dict[rank_name[i][0]] = [rank_name[i][1], rank_name[i][2]]
      i += 1

  year_name_rank = []
  alpha_name_rank = []
  final_name_rank = []
  final_list = []

  year_name_rank.append(get_year(filename))

  for key, value in name_rank_dict.items():
      alpha_name_rank.append([key, value])

  i = 0
  while i < len(alpha_name_rank):
      rank_pair = (alpha_name_rank[i][0], alpha_name_rank[i][1][0])
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

  printable_list = '\n'.join(final_list)
  return(printable_list)

  f.close()

def main():
  # This command-line parsing code is provided.
  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]

  if not args:
    print('usage: [--summaryfile] file [file ...]')
    sys.exit(1)

  # Notice the summary flag and remove it from args if it is present.
  summary = False
  if args[0] == '--summaryfile':
    summary = True
    del args[0]

  # +++your code here+++
  # For each filename, get the names, then either print the text output
  # or write it to a summary file

  i = 1
  while i <= len(args):
      filename = sys.argv[i]
      # print(extract_names(filename))
      # print()
      os.chdir('C:\\Users\\bbrownholtz\\Desktop')
      nameFile = open('nameFile' + filename + '.txt', 'a')
      nameFile.write(extract_names(filename))
      nameFile.close()
      i += 1
  
if __name__ == '__main__':
  main()
