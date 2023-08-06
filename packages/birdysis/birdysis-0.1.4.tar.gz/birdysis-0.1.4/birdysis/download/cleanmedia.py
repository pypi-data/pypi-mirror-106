from os import listdir, remove, rename
from os.path import isfile, join
import re
from sys import exit

r = re.compile(r'^(.*?)_')

photo_path = "media/photo"
video_path = "media/video"
gif_path = "media/animated_gif"

def clean_dir(dirpath):

    files = [f for f in listdir(dirpath) if isfile(join(dirpath, f))]
    fsize = len(files)
    print('Checking photo files for duplicate IDs...')

    print('Scrubbing away the indices...')

    scrub = []

    for idx, i in enumerate(files):
        filename = i
        match = r.search(i)
        if (match):
            index = i.split('_')[0]
            filename = filename.replace(match.group(0), '')
            scrub.append({'id': index, 'name': filename})
        
    if (len(scrub) == len(files)):
        print('All files were scrubbed!')

    elif (len(scrub) == 0):
        print('All files are already clean! Exiting...')
        return

    elif (len(scrub) <= len(files)):
        print('Some files were scrubbed, others are already clean!')
    print('Scrubbing complete.')

    print('Checking for duplicates...')

    seen = {}
    dups = []

    for i in scrub:
        if i['name'] not in seen:
            seen[i['name']] = 1
        else:
            if seen[i['name']] == 1:
                filename = str(i['id']) + '_' + i['name']
                dups.append(filename)

            seen[i['name']] += 1

    print(f'Found {len(dups)} duplicates.')

    if (len(dups) == 0):
        print('No further action is required, exiting...')
        return

    print('Removing duplicates from directory...')

    c = 0

    for i in dups:
        if i in files:
            path = join(dirpath + '/', i)
            remove(path)
            print(f'{i} removed.')
            c += 1
            

    print(f'All files found? {c == len(dups)}')

    final_size = fsize - c
    print(f'Check directory, there should be {final_size} files! Exiting...')


def rename_files(dirpath):

    files = [f for f in listdir(dirpath) if isfile(join(dirpath, f))]
    fsize = len(files)

    print('Cleaning out the IDs...')

    print('Scrubbing away the indices...')

    scrub = []

    for idx, i in enumerate(files):
        filename = i
        match = r.search(i)
        if (match):
            index = i.split('_')[0]
            filename = filename.replace(match.group(0), '')
            
            # old_path = join(dirpath + '/', i)
            # new_path = join(dirpath + '/', filename)
            # rename(old_path, new_path)
            scrub.append({'id': index, 'name': filename})
        
    if (len(scrub) == len(files)):
        print('All files were scrubbed!')
    elif (len(scrub) == 0):
        print('All files are already clean! Exiting...')
        return
    elif (len(scrub) <= len(files)):        
        print('Some files were scrubbed, others are already clean!')

    print('Scrubbing complete.')

while 1:
    
    choice = input('Which directory do you want to delete? [1]: photo, [2]: video, [3]: gif ')

    if choice == '1':
        clean_dir(photo_path)
        if(input('Do you want to scrub? y/n ').lower() == 'y'):
            rename_files(photo_path)
        break
    elif choice == '2':
        clean_dir(video_path)
        if(input('Do you want to scrub? y/n ').lower() == 'y'):
            rename_files(video_path)
        break
    elif choice == '3':
        clean_dir(gif_path)
        if(input('Do you want to scrub? y/n ').lower() == 'y'):
            rename_files(gif_path)
        break
    else:
        print('Wrong value, try again.')

exit()
        
