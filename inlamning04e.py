from asyncio.windows_utils import pipe
from sys import exit 
print("This program is made to calculate rectangeles/squares\n")

widthList = []
heightList = []
areaList = []
isasqaureList = []
def figure():
    print("Höjden | Volymen")
    print("-----------------")
    for i in range(1,10):
        print("  {}    |    {} ".format(i, area*i))

    
askAgain = 1
while askAgain != 2:
    askAgain = 0
    askHeight= int(input("How long is your one of your rectangles side from 1-10?: "))
    heightList.append(askHeight)
    askWidth = int(input("How long is one of the other side from 1-10?: "))
    widthList.append(askWidth)
    area = askWidth*askHeight
    areaList.append(area)
    if askHeight == askWidth:
        print("The figure is a square")
        isasqaureList.append(True)
    else:
        print("The figure is a rectangle")
        isasqaureList.append(False)
    figure()
    askAgain = int(input("Do you wanna calculate another figure? (Press 1 to continue or 2 to stop)"))

print("Your figures are:")
print("Width |  Height | Area | Square?")
print(*widthList, *heightList, *areaList, *isasqaureList)
exit()