def build_AQI_dicts(filename):
    res = []
    with open(filename,'r') as f:
        data = [i.replace('\n','').split(', ') for i in f.readlines()]
    head = data[0]
    for row in data[1:]:
        d = {}
        for i in range(len(head)):
            value = None
            if not row[i]:
                value = None
            elif row[i].isdigit():
                value = int(row[i])
            else:
                value = str(row[i])
            d[head[i]] = value
        res.append(d)
    return res
def collect_info_per_month(info, L):
    res = {}
    for row in L:
        if info in row:
            if row[info]:
                date = '/'.join(row['date'].split('/')[:2])
                if date in res:
                    res[date].append(row[info])
                else:
                    res[date] = [row[info]]
    return res
def print_stats_per_month(limit, d):
    for key in d.keys():
        s = 0
        if len(d[key]) < 10:
            print(f'{key}:NOT ENOUGH DATA')
            continue
        for day in d[key]:
            if day <= limit:
                s += 1
        print(f'{key}: {s} good day(s)')




