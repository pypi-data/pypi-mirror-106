# Author: Christopher Paldino

import csv
import os
# import matplotlib.pyplot as pp

# Set up objects for each social network to hold data for the analysis
class OSN:
    def __init__(self, networkName):
        self.name = networkName  # social network name
    total = 0  # total number of users (age 25+)
    # number of users (age 25+) with at least a bachelor's degree
    gradTotal = 0
    # number of users (age 25+) with at least a bachelor's degree that are men
    gradMen = 0
    # number of users (age 25+) with at least a bachelor's degree that are women
    gradWomen = 0
    # number of users (age 25+) without at least a bachelor's degree
    unedTotal = 0
    # number of users (age 25+) without at least a bachelor's degree that are men
    unedMen = 0
    # number of users (age 25+) without at least a bachelor's degree that are women
    unedWomen = 0
    # percentage of users (age 25+) with at least a bachelor's degree
    gradPercent = 0
    # percentage of users (age 25+) with at least a bachelor's degree that are men
    gradMenPercent = 0
    # percentage of users (age 25+) with at least a bachelor's degree that are women
    gradWomenPercent = 0

# calculate data about each social network using its corresponding row/field number from the csv


def calculateData(row, osn, rowNum, degree, male):
    # checks respondents degree status and gender before being added to appropriate count
    osn.gradMen = osn.gradMen + \
        1 if int(row[rowNum]) == 1 and degree and male else osn.gradMen
    osn.gradWomen = osn.gradWomen + \
        1 if int(row[rowNum]) == 1 and degree and not(male) else osn.gradWomen
    osn.unedMen = osn.unedMen + \
        1 if int(row[rowNum]) == 1 and not(degree) and male else osn.unedMen
    osn.unedWomen = osn.unedWomen + \
        1 if int(row[rowNum]) == 1 and not(
            degree) and not(male) else osn.unedWomen


def main():
    # create each social network object
    twitter = OSN("Twitter")
    instagram = OSN("Instagram")
    facebook = OSN("Facebook")
    snapchat = OSN("Snapchat")
    linkedIn = OSN("LinkedIn")
    reddit = OSN("Reddit")
    osnList = [twitter, instagram, facebook, snapchat, linkedIn, reddit]
    # read the file and populate the counts
    path=os.path.abspath(os.path.dirname(__file__))
    os.chdir(path) 
    with open("Pew_Survey.csv") as csvFile:
        file = csv.reader(csvFile)
        next(file)  # skip first line
        for row in file:
            age = int(row[23])
            if age > 24 and age < 98:  # check that age is 25 or older
                # check degree is at least Bachelor's
                degree = int(row[25]) > 5 and int(row[25]) < 9
                # check gender
                male = int(row[22]) == 1
                # call the function to add to the counts for each social network
                calculateData(row, twitter, 4, degree, male)
                calculateData(row, instagram, 5, degree, male)
                calculateData(row, facebook, 6, degree, male)
                calculateData(row, snapchat, 7, degree, male)
                calculateData(row, linkedIn, 11, degree, male)
                calculateData(row, reddit, 12, degree, male)

    # calculate totals and percents for each social network
    for osn in osnList:
        osn.gradTotal = osn.gradMen+osn.gradWomen
        osn.unedTotal = osn.unedMen+osn.unedWomen
        osn.total = osn.gradTotal+osn.unedTotal
        osn.gradPercent = round(osn.gradTotal/osn.total*100, 2)
        osn.gradMenPercent = round(osn.gradMen/osn.gradTotal*100, 2)
        osn.gradWomenPercent = round(osn.gradWomen/osn.gradTotal*100, 2)

    # sort the list by the social networks with the highest percent of age 25+ users with at least a Bachelor's degree
    osnList = sorted(osnList, key=lambda x: x.gradPercent, reverse=True)
    print("Percentage of users (age 25+) that have at least a Bachelor's degree for each social network:")
    for osn in osnList:
        print(f"\t{osn.name}: {osn.gradPercent}% ({osn.gradMenPercent}% men and {osn.gradWomenPercent}% women)")
        print(
            f"\t\tTotal users: {osn.total} ({osn.gradMen+osn.unedMen} men and {osn.gradWomen+osn.unedWomen} women)")
        print(
            f"\t\tTotal users (age 25+) with at least a Bachelor's degree: {osn.gradTotal} ({osn.gradMen} men and {osn.gradWomen} women)")
    print(
        f"Conclusion: {osnList[0].name} has the highest percentage of users (age 25+) with at least a Bachelor's degree")

    # # create the bar graph showing the percentage of users (age 25+) with at least a Bachelor's degree for each social network
    # barLabels = [osn.name for osn in osnList]
    # heights = [osn.gradPercent for osn in osnList]
    # pp.bar(barLabels, heights)
    # pp.xlabel("Social networks")
    # pp.ylabel("Percentage of users (age 25+) with at least a Bachelor's degree")
    # pp.title("Social networks education data")
    # pp.show()

    # # create each social network pie chart and display it
    # for osn in osnList:
    #     labelList = ["Men (age 25+) \nwith at least a \nBachelor's degree", "Women (age 25+) \nwith at least a \nBachelor's degree",
    #                 "Men (age 25+) \nwithout a \nBachelor's degree", "Women (age 25+) \nwithout a \nBachelor's degree"]
    #     numbers = [osn.gradMen, osn.gradWomen, osn.unedMen, osn.unedWomen]
    #     pp.pie(numbers, labels=labelList, colors=[
    #         'blue', 'cyan', 'purple', 'magenta'], autopct=lambda p: f"{round(p,2)}% \n({int(round(p*sum(numbers)/100,0))} users)")
    #     pp.title(f"{osn.name} user education data")
    #     pp.show()
