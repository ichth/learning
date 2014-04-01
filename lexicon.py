direction = ['north', 'south', 'east', 'west', 'down', 'up', 'left',
                         'right', 'back']
verb = ['go', 'stop', 'kill', 'eat']
stop = ['the', 'in', 'of', 'from', 'at', 'it']
noun = ['door', 'bear', 'princess', 'cabinet']

def convert_number(s):
    try:
        return(int(s))
    except ValueError:
        return(None)

def scan(words_list):
    try:
        words = words_list.split()
        meaning = []

        for word in words:
            if word in direction:
                meaning.append(('direction', word))
            elif word in verb:
                meaning.append(('verb', word))
            elif word in stop:
                meaning.append(('stop', word))
            elif word in noun:
                meaning.append(('noun', word))
            elif convert_number(word) != None:
                meaning.append(('number', convert_number(word)))
            else:
                meaning.append(('error', word))

        return(meaning)

    except ValueError:
        return(None)
