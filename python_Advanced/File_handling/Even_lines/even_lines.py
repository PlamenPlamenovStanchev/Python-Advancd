with open('text.txt') as f:
    for row, line in enumerate(f.readlines()):
        if row % 2 == 0:
            for character in '-,.!?':
                line = line.replace(character, '@')
            print(' '.join(reversed(line.split())))