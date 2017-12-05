# xp necessary for a certain level
total = [600, 550, 530, 500, 480, 460, 430, 420, 410, 390, 360, 340, 320]
red = [240, 230, 215, 200, 190, 180, 160, 155, 150, 140, 130, 120, 110]
green = red
blue = [75, 72, 70, 68, 66, 64, 62, 61, 60, 58, 55, 50, 45]
# grade associated with levels
grade = ["A+","A","A-","B+","B","B-","C+","C","C-","D+","D","D-","F"]

def getUserStats():
    # userStats is tuple formatted (total, red, blue, green, bonus)
    totalXp = int(input("Enter your total xp (as seen on scoreboard): "))
    redXp = int(input("Enter your RED xp: "))
    blueXp = int(input("Enter your BLUE xp: "))
    greenXp = int(input("Enter your GREEN xp: "))
    bonusXp = int(input("Enter your BONUS xp: "))
    return([totalXp, redXp, blueXp, greenXp, bonusXp])

def getMaxPositions(userXp):
        totalIndex = -1
        redIndex = -1
        blueIndex = -1
        greenIndex = -1

        for i,xp in enumerate(red):
            if userXp[1] >= xp:
                redIndex = i
                break;

        for i,xp in enumerate(blue):
            if userXp[2] >= xp:
                blueIndex = i
                break;

        for i,xp in enumerate(green):
            if userXp[3] >= xp:
                greenIndex = i
                break;

        xpIndicies = [redIndex, blueIndex, greenIndex]
        # find the colored xp that has the highest index.
        return xpIndicies


def findBestUseageOfBonus(userXp):
    bonusXpAmount = userXp[4]
    bonusDistribution = [0,0,0]
    while(bonusXpAmount != 0):
        # find the colored xp that has the highest index.
        xpIndicies = getMaxPositions(userXp)
        max_positions = [i for i, x in enumerate(xpIndicies) if x == max(xpIndicies)]
        # prioritize blue
        if 1 in max_positions:
            bonusDistribution[1] += 1
            userXp[2] += 1
        elif 2 in max_positions:
            bonusDistribution[2] += 1
            userXp[3] += 1
        elif 0 in max_positions:
            bonusDistribution[0] += 1
            userXp[1] += 1
        else:
            print("Something went wrong")
        userXp[4] -= 1
        bonusXpAmount -= 1

    maxGrade = grade[max(getMaxPositions(userXp))]
    print(f"Using your current xp and smartly distributing your bonus xp could net you a(n)\n{maxGrade}\nif you distribute your bonus xp as follows:")
    return bonusDistribution



def main():
    userXp = getUserStats()
    desiredGrade = input("Enter your desired grade (ex. A+): ")
    print("")
    # getting the index of the grade in the xp necessary lists
    indexOfGrade = 0
    for i,x in enumerate(grade):
        if x == desiredGrade:
            indexOfGrade = i
            break;
    # getting the amount of xp needed in each category
    totalDiff = 0
    redDiff = 0
    blueDiff = 0
    greenDiff = 0

    if userXp[0] < total[indexOfGrade]:
        totalDiff = total[indexOfGrade] - (userXp[0] + userXp[4])
        print(f"Need {totalDiff} more total")
    if userXp[1] < red[indexOfGrade]:
        redDiff = red[indexOfGrade] - userXp[1]
        print(f"Need {redDiff} more red")
    if userXp[2] < blue[indexOfGrade]:
        blueDiff = blue[indexOfGrade] - userXp[2]
        print(f"Need {blueDiff} more blue")
    if userXp[3] < green[indexOfGrade]:
        greenDiff = green[indexOfGrade] - userXp[3]
        print(f"Need {greenDiff} more green")
    if all(v == 0 for v in [totalDiff,redDiff,blueDiff,greenDiff]):
        print("You don't need any more points to get your desired grade!")

    print(f"\nBonus Xp is already calculated into your total xp NOT your colored categories.\n")

    bestUse = findBestUseageOfBonus(userXp)

    # print("My recomendation on where you should put your extra xp is:")
    print(f"{bestUse[0]} in red")
    print(f"{bestUse[1]} in blue")
    print(f"{bestUse[2]} in green")

    print(f"{bestUse[0]} in red ({redDiff - bestUse[0]})")
    print(f"{bestUse[1]} in blue ({blueDiff - bestUse[1]})")
    print(f"{bestUse[2]} in green ({greenDiff - bestUse[2]})")

main()
