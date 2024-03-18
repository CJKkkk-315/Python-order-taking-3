def readFreq(filename):
    frequencies = {}
    f = open(filename)
    lines = f.readlines()
    f.close()
    for line in lines:
        key,value = line.replace('\n','').split()
        frequencies[key] = int(value)
    return frequencies
def longSingleUseword(frequencies):
    result = []
    answer = []
    for key in frequencies.keys():
        if frequencies[key] == 1:
            result.append(key)
    result.sort(key=lambda x:len(x))
    max = len(result[-1])
    for i in result:
        if len(i) == max:
            answer.append(i)
    return answer