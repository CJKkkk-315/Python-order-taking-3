# This code is a starting point for your assignment 5.
# You have no need to change much of the main function or any of the supplied complete functions.
# Function headers for the ones you must write are supplied, as are their doc strings.

def readData(filename):
    '''Reads the weather data from the supplied filename. The function returns a list of
dictionaries, where each dictionary consists of the data for a particular month.'''
    # You can see the key names used by examining the code given below.
    fileIn = open(filename, 'r')
    allData = []
    line = fileIn.readline()
    while line != "":
        line = fileIn.readline().strip()
        if line != "":
            values = line.split(',')
            monthData = {}
            monthData['year'] = int(values[0])
            monthData['month'] = int(values[1])
            monthData['meanT'] = float(values[2])
            monthData['maxT'] = float(values[3])
            monthData['minT'] = float(values[4])
            monthData['rain'] = float(values[5])
            monthData['snow'] = float(values[6])
            allData.append(monthData)
    fileIn.close()
    return allData

def showSome(allData):
    '''A convenience function that prints the beginning and end portions of the supplied list.'''
    for i in range(10):
        print(allData[i])
    print("<snip>")
    for i in range(-10, 0):
        print(allData[i])

def getInt(prompt, lowLimit=None, highLimit=None):
    '''A robust function that is sure to return an int value between the two
supplied limits.'''
    numberOK = False
    while not numberOK:
        try:
            userNum = int(input(prompt))
            if lowLimit != None and userNum < lowLimit:
                print("The number must be higher than", lowLimit)
                print("Please try again.")
            elif highLimit != None and userNum > highLimit:
                print("The number must be lower than", highLimit)
                print("Please try again.")
            else:
                numberOK = True
        except ValueError:
            print("Your entry is not a valid integer, please try again.")
    return userNum

def addYearMonthKey(allData):
    '''Calculates and adds a key:value pair to each dictionary in the supplied list.
The key will be named 'yearmonth' and will have a value of (100 * year + month).'''
    for monthData in allData:
        monthData['yearmonth'] = monthData['year'] * 100 + monthData['month']

def insertionSort(allData, key):
    '''Sorts the supplied list of dictionaries in situ into increasing order
by the key name supplied.'''
    # You don't have to use insertion sort, but you should *not* use bubble sort and
    # cannot use any of the built-in Python sorts.  Remove the "pass" line and add your
    # own code:
    for i in range(1, len(allData)):
        k = allData[i]
        j = i - 1
        while j >= 0 and k[key] < allData[j][key]:
            allData[j+1] = allData[j]
            j -= 1
        allData[j+1] = k

def findRain(allData, target):
    '''Uses a binary search to locate rainfall amounts in mm from the supplied list of
dictionaries.  target is a date in the 'yearmonth' value format.  The function assumes
that the list has been sorted by increasing date.  The function will raise a ValueError
exception if the year and month in target do not exist in allData.'''
    # You must use a binary seach and cannot use any built-in searches.
    def binarySearch(arr, l, r, x):
        if r >= l:
            mid = int(l + (r - l) / 2)
            if arr[mid]['yearmonth'] == x:
                return mid
            elif arr[mid]['yearmonth'] > x:
                return binarySearch(arr, l, mid - 1, x)
            else:
                return binarySearch(arr, mid + 1, r, x)
        else:
            return -1
    result = binarySearch(allData, 0, len(allData) - 1, target)
    return allData[result]['rain']
def findMax(allData, key):
    '''Returns the record from allData that has the maximum value for the supplied key.'''
    # You cannot use any built-in searches including the max() BIF.
    res = -99999
    ans = {}
    for i in allData:
        if i[key] > res:
            res = i[key]
            ans = i
    return ans

def findMin(allData, key):
    '''Returns the record from allData that has the minimum value for the supplied key.'''
    # You cannot use any built-in searches including the min() BIF.
    res = 99999
    ans = {}
    for i in allData:
        if i[key] < res:
            res = i[key]
            ans = i
    return ans

def getAnnualSnow(allData):
    '''This function returns a list of dictionaries which consist of the total
snowfall for every year listed in allData.  Each record will consist of
{'year' : ####, 'totalsnow' : ###.#}, where # is a number.  There will be one record per year.
It does not matter if any month records are missing, the total snowfall is still calculated, by
assuminng zero snow for the missing months.'''
    res = {}
    ans = []
    for i in allData:
        if i['year'] not in res:
            res[i['year']] = i['snow']
        else:
            res[i['year']] += i['snow']
    for i,j in res.items():
        ans.append({'year':i,'totalsnow':j})
    return ans

def saveAnnualMeanTemp(allData, filename):
    '''This function calculates the mean temperatures for an entire year and saves this
data to the supplied file - one line in the file per year.
It is assumed that each year from 1938 to 2012 has 12 months.'''
    res = {}
    ans = []
    for i in allData:
        if i['year'] not in res:
            res[i['year']] = i['meanT']
        else:
            res[i['year']] += i['meanT']
    for i, j in res.items():
        ans.append({'year': i, 'meanT': round(j/12,2)})
    insertionSort(ans,'year')
    with open(filename,'w',encoding='utf-8') as f:
        for i in ans:
            f.write(f"{i['year']} {i['meanT']}\n")

def main():
    # Read the data
    db = readData("TorontoWeatherData.csv")
    # Un-comment these lines to make sure your sort has worked properly.
    #print("Before sorting, as read from file:")
    #showSome(db)
    addYearMonthKey(db)
    insertionSort(db, 'yearmonth')
    #print("\nAfter sorting by date:")
    #showSome(db)

    # Test your binary search by searching for the rainfall amount for a user-
    # supplied year and month.
    searchYear = getInt("Enter year for rainfall search: ", 1938, 2012)
    searchMonth = getInt("Enter month for rainfall search: ", 1, 12)
    searchYearMonth = 100 * searchYear + searchMonth
    try:
        rainfall = findRain(db, searchYearMonth)
        print("Rainfall was {0} mm.".format(rainfall))
    except ValueError as message:
        print(message)

    # Test your findMax and findMin functions by locating some extremes.
    # These two functions return a single record which is a dictionary.
    maxR = findMax(db, 'maxT')
    print("\nHighest temperature {0} deg C, in month {1}, {2}.".format(maxR['maxT'], maxR['month'], maxR['year']))
    minR = findMin(db, 'minT')
    print("Lowest temperature {0} deg C, in month {1}, {2}.".format(minR['minT'], minR['month'], minR['year']))
    maxR = findMax(db, 'rain')
    print("Highest rainfall {0} mm, in month {1}, {2}.".format(maxR['rain'], maxR['month'], maxR['year']))
    maxR = findMax(db, 'snow')
    print("Highest snowfall {0} cm, in month {1}, {2}.".format(maxR['snow'], maxR['month'], maxR['year']))

    # annualSnow is a list of dictionaries, where each dictionary holds the year and the total snowfall
    # for that year.
    annualSnow = getAnnualSnow(db)
    insertionSort(annualSnow, 'totalsnow')
    minR = annualSnow[0]
    print("\nLowest annual snowfall {0} cm, in {1}.".format(minR['totalsnow'], minR['year']))
    medR = annualSnow[len(annualSnow) // 2]
    print("Median annual snowfall {0} cm.".format(medR['totalsnow']))    
    maxR = annualSnow[len(annualSnow) - 1]
    print("Highest annual snowfall {0} cm, in {1}.".format(maxR['totalsnow'], maxR['year']))
    
    # Sort your data again, by mean temperature this time.  This is the only way you can get the median
    # value, which is defined as the middle of a sorted set of values.
    insertionSort(db, 'meanT')
    minR = db[0]
    print("\nLowest mean temperature {0} deg C, in month {1}, {2}.".format(minR['meanT'], minR['month'], minR['year']))
    medR = db[len(db) // 2]
    print("Median mean temperature {0} deg C.".format(medR['meanT']))
    maxR = db[-1]
    print("Highest mean temperature {0} deg C, in month {1}, {2}.".format(maxR['meanT'], maxR['month'], maxR['year']))

    # Look for Global Warming!
    saveAnnualMeanTemp(db, "YearMeans.txt")
    
main()
