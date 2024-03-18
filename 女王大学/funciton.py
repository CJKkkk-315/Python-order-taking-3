def load_file(filename):
    print(filename,':')
    with open(filename) as f:
        data = f.readlines()
    return ''.join(data)
def clean_data(data):
    data = data.replace('\n',' ')
    data = data.replace('-',' ')
    data = data.replace('  ',' ')
    data = data.lower()
    res = []
    for i in data:
        if i.isalpha() or i == ' ':
            res.append(i)
    data = ''.join(res)
    while data.count('  '):
        data = data.replace('  ',' ')
    return data
def count_sc(data):
    print(len(data),'characters')
    n = data.count('!') + data.count('.') + data.count('?')
    print(n,'sentences')
def count_else(data):
    words = data.split(' ')
    print(len(words),'words')
    d = {}
    for i in words:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    with open('../test.txt', 'w', encoding='utf8') as f:
        for i,j in d.items():
            f.write(str(i)+ ' ' + str(j) + '\n')
    max_len = 0
    max_words = []
    for i in words:
        if len(i) > max_len:
            max_len = len(i)
    for i in words:
        if len(i) == max_len:
            if i not in max_words:
                max_words.append(i)
    print(len(d),'unique words')
    print(round(len(d)/len(words)*100,1),'% of the words are unique.')
    if len(max_words) == 1:
        print('Longest word is: ',max_words[0])
    else:
        print('Longest words is: ',','.join(max_words))
def all(filname):
    data = load_file(filname)
    count_sc(data)
    data_clean = clean_data(data)
    count_else(data_clean)
all('PMHarperBerlinWall.txt')
