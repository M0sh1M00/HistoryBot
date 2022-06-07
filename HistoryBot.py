from urllib.request import urlopen
import datetime
import re

def getURL():
    today = datetime.date.today()
    monthAndDay = today.strftime("%B %d")
    monthAndDay = monthAndDay[:-3] + "_" + monthAndDay[-2:]
    
    return "https://en.wikipedia.org/wiki/" + monthAndDay
    

def getWebsite(url):
    # Very primitive timeout checker since my computer has issues
    # with urllib2 and its builtin timeout features
    while True:
        try:
            f = urlopen(url)
            break
        except:
            pass
    scrapedWebsite = f.read()
    scrapedWebsite = scrapedWebsite.decode("utf8")
    
    return scrapedWebsite

def splitIntoArray(website):
    birthIndex = website.index("id=\"Births")
    website = website[:birthIndex]
    websiteList = re.split(r"</?li>", str(website))
    
    return websiteList

def removeHTML(line):
    for i in range(line.count('<')):
        try:
            start = line.find('<')
            end = line.find('>', start+1)
            line = line[:start] + line[end+1:]
        except:
            pass
        
    return line

def removeGarbage(line):
    line = line.replace('&#8211;', ":")

    # This is an encoded phrase that makes the word italic
    line = line.replace('&#160;', " ")

    # These are the tags wikipedia uses to cite things, i.e: '[3]'
    try:
        endLineGarbageIndex = line.index("&#91;")
        line = line[:endLineGarbageIndex]
    except:
        pass

    # This part removes the arbitrary amount of spaces between the year and colon
    while True:
        colonIndex = line.index(":")
        if line[colonIndex-1] == ' ':
            line = line[0:colonIndex-1] + line[colonIndex:]
        else:
            break
        
    return line

def getEventList():
    website = getWebsite(getURL())
    websiteList = splitIntoArray(website)

    # &#8211 is an encoded version of -
    # This program works under the (sensible) assumption
    # that the dashes only appear for the yearly events
    regexPattern = re.compile(".*&#8211;")
    dirtyEventList = list(filter(regexPattern.match, websiteList))
    cleanEventList = list()
    for event in dirtyEventList:
        event = removeHTML(event)
        event = removeGarbage(event)
        cleanEventList.append(event)

    return cleanEventList;
        
if __name__ == "__main__":
    eventList = getEventList()
    for event in eventList:
        print(event)
    
