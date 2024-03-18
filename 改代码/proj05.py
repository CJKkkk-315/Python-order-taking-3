STATES = ['Alaska', 'Alabama', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut',
          'Delaware', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa',
          'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan',
          'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire',
          'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio',
          'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota',
          'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia',
          'Wisconsin', 'Wyoming']
def open_file():
    print("Enter a file: ")
    return open(input())
def read_file(lines):
    datalist = {}
    lines = [x.split(",") for x in lines]
    for row in lines:
        name = row[0].strip()
        if name == "Missouri 2/":
            name = "Missouri"
        if name not in STATES:
            continue
        value = row[6]
        value = value[:-1]
        if value.isdigit():
            value = int(value)
        else:
            continue
        if "All GE varieties" not in row[3]:
            continue 
        year = int(row[4])
        crop = row[1]
        data = {"Max_Yr" : year, 
                "Max" : value,
                "Min_Yr" : year,
                "Min" : value}
        if crop not in datalist:
            datalist[crop] = {}
        if name not in datalist[crop].keys():
            datalist[crop][name] = data
        else:
            if value > datalist[crop][name]["Max"]:
               datalist[crop][name]["Max_Yr"] = year
               datalist[crop][name]["Max"] = value
            if value < datalist[crop][name]["Min"]:
               datalist[crop][name]["Min_Yr"] = year
               datalist[crop][name]["Min"] = value
            if value == datalist[crop][name]["Max"] and year < datalist[crop][name]["Max_Yr"]:
               datalist[crop][name]["Max_Yr"] = year
            if value == datalist[crop][name]["Min"] and year < datalist[crop][name]["Min_Yr"]:
               datalist[crop][name]["Min_Yr"] = year
    return datalist
    
def main():
    filename = input("Please enter file name: ")
    datalist = read_file(open(filename).readlines())
    for crop in sorted(datalist.keys()):
        print("Crop: " + crop)
        print("{:<20s}{:<8s}{:<6s}{:<8s}{:<6s}".format("State", "Max Yr", "Max", "Min Yr", "Min"))
        for states in sorted(datalist[crop].keys()):
            print("{:<20s}{:<8s}{:<6d}{:<8s}{:<6d}".format(states, str(datalist[crop][states]["Max_Yr"]),datalist[crop][states]["Max"],str(datalist[crop][states]["Min_Yr"]),datalist[crop][states]["Min"]))
        print()
if __name__ == "__main__":
    main()