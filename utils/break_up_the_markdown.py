#!python3
'''
Takes long markdown files and chops them up into shorter ones, for ease of reading on mobile devices and faster 'search result to eyeball recognition of content' time.
'''

import os
import shutil
import sys


def process_doc(name, doc: list) -> dict:
    '''
    create a new filename with this format: x-x-x... where each represents the number of new files that were created from the original.
        if the original file has this structure, capture it so you can add another -x series to the front of the filename
        The # Words becomes the filename after the x series
    for all instances of ## more words, convert to # words
    '''
    new_doc = []
    title = name
    answer = {}
    for line in doc:
        cut_octo, new_line = one_less_octothorp(line)
        if cut_octo is False:
            new_doc.append(new_line)
        else:
            cut_octo, _ = one_less_octothorp(new_line)
            if cut_octo is False:
                new_title = title.strip()
                title = new_line[1:]
                answer[new_title] = new_doc
                new_doc = []
            else:
                new_doc.append(new_line)
    answer[title] = new_doc
    return answer


def one_less_octothorp(line: str) -> tuple:
    '''
    removes an octothorp from a line, and returns:
    (T/F, line)
    True if cut an octothorp, false otherwise
    '''
    if line[0] != '#':
        return (False, line)
    else:
        return (True, line[1:])


def numbering(total):
    result = []
    if total > 9:
        multiples = round(total / 9)
        for i in range(1, multiples+2):
            for j in range(1, 10):
                result.append(f'{i}-{j}')
        return result
    else:
        for j in range(1, 10):
            result.append(f'{j}')
    return result


# process the files in the folder:
for folderName, subfolders, filenames in os.walk(os.getcwd()):
    for filename in filenames:
        if filename.endswith(".md"):
            name, ext = filename.split('.')
            shutil.move(f'{name}.md', f'{name}.txt')
            with open(f'{name}.txt', 'r') as f:
                orig = f.readlines()
            shutil.move(f'{name}.txt', f'{name}.md')
            processed_sections = process_doc(name, orig)
            num_files = numbering(len(processed_sections.keys()))
            os.mkdir(name)
            os.chdir(name)
            for title in processed_sections.keys():
                file_title = '-'.join(title.split())
                file_num = num_files.pop(0)
                with open(f'{file_num}-{file_title}.md', 'w') as f:
                    f.write('---\n')
                    f.write(f'title: "{title}"\n')
                    f.write(f'metaTitle: "{title}"\n')
                    f.write(f'metaDescription: "{title}"\n')
                    f.write('---\n')
                    f.write(''.join(processed_sections[title]))
            os.chdir('..')
            sys.exit()