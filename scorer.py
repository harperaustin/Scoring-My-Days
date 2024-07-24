from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

day_scores = []

def check_valid_date(date):

    #First check if the date is even possible or in the correct format
    try:
        parsed_date = datetime.strptime(date, "%Y-%m-%d")
        #Checking if it is a future date
        if parsed_date > datetime.now():
            print("Date is in the future")
            return False
        with open("day_scores.txt", "r" ) as file:
            count = 0
            for line in file:
                count += 1
                if count % 4 == 1:
                    if line.strip() == date:
                        print("Day already scored.")
                        return False

        print("format correct")
        return True
    except ValueError:
        print("Format incorrect")
        return False
    
    

    
    #Now need to check if that date has already been scored
    #I can just run a for loop through day_scores to see if that date is already there
    
def getting_date():
    
    curr_ans = input("Are you scoring today (0) or a prior date (1)? ")
    if curr_ans == '0':
        date = datetime.now().date().strftime("%Y-%m-%d")
        return date
    else:
        valid_date = False
        date = ""
        while not valid_date:
            date = input("Please enter a valid past date (YYYY-mm-dd): ")
            valid_date = check_valid_date(date)
        return date
    

def get_score():
    score = 0
    if input("Was the day a special day? (y/n) ").lower() == "y":
        curr_ans = input("Was today amazing (a), great (b), or good (c)? ")
        if curr_ans == 'a':
            score += 318
        elif curr_ans == 'b':
            score += 275
        else:
            score += 225

        return score
    else:
        print("Normal day scoring")
        curr_ans = input("Did you wake up before 8 (a), before 10 (b), or after 10 (c)? ")
        if curr_ans == 'a':
            score += 10
        elif curr_ans == 'b':
            score += 3

        if input("Did you make your bed in the morning? (y/n) ") == 'y':
            score += 5

        if input("Did you go on your phone when you woke up? (y/n) ") == 'n':
            score += 15

        if input("Did you brush teeth and wash face in the morning? (y/n) ") == 'n':
            score += 4

        if input("Did you do any stretching or mobility? (y/n) ") == 'y':
            score += 7

        if input("Did you go outside for at least an hour? (y/n) ") == 'y':
            score += 25
        
        if input("Read at least 10 pages of a book? (y/n) ") == 'y':
            score += 20
        
        if input("Did you do something fun? (y/n) ") == 'y':
            score += 20

        if input("Did you exercise? (y/n) ") == 'y':
            score += 25

        curr_ans = input("Did you eat super healthy (a), somewhat healthy (b), or not healthy (c)? ")
        if curr_ans == 'a':
            score += 25
        elif curr_ans == 'b':
            score += 10

        if input("Did you drink enough water? (y/n) ") == 'y':
            score += 15
        
        if input("Did learn something new? (y/n) ") == 'y':
            score += 12

        curr_ans = input("Did you scroll on social media NONE (a), under 30 minutes (b), or more than 30 minutes (c)? ")
        if curr_ans == 'a':
            score += 25
        elif curr_ans == 'b':
            score += 10

        if input("Did you do something productive (work or school) (y/n) ") == 'y':
            score += 20

        if input("Did you do something productive outside of school or work? (y/n) ") == 'y':
            score += 14

        if input("Did you go outisde of you comfort zone? (y/n) ") == 'y':
            score += 15

        if input("Did you compliment someone? (y/n) ") == 'y':
            score += 15

        if input("Did you hangout with friends? (y/n) ") == 'y':
            score += 15
        
        if input("Did you make any money or save money? (y/n) ") == 'y':
            score += 9
        
        if input("Did you pet an animal? (y/n) ") == 'y':
            score += 3

        if input("Did you brush teeth and wash face before bed? (y/n) ") == 'n':
            score += 4

        curr_ans = input("Are you going to sleep before 11 (a), before 1 (b), or later(c)? ")
        if curr_ans == 'a':
            score += 10
        elif curr_ans == 'b':
            score += 5

        if input("Are you going to fall asleep with your phone on? (y/n) ") == 'n':
            score += 5

    #max score 335
    return score



def insert_new_date(date, score, note):
    parsed_date = datetime.strptime(date, "%Y-%m-%d")
    days = []
    new_day = (parsed_date, score, note)

    with open("day_scores.txt", "r" ) as file:
        while True:
            date_line = file.readline().strip()
            if not date_line:
                break
            score_line = file.readline().strip()
            note_line = file.readline().strip()
            spacer_line = file.readline().strip()

            date_line = datetime.strptime(date_line, "%Y-%m-%d")
            days.append((date_line, score_line, note_line))

    days.append(new_day)
    days.sort(key=lambda x: x[0])

    with open("day_scores.txt", "w") as file:
        for day in days:
            file.write(str(day[0].strftime("%Y-%m-%d")) + "\n")
            file.write(str(day[1]) + "\n")
            file.write(str(day[2]) + "\n")
            file.write("\n")



def day_scorer():
    date = getting_date()
    score = get_score()
    note = input("Add a brief note about this day: ")
    insert_new_date(date, score, note)
        

#day_scorer()

def show_plot():
    dates = []
    scores = []
    with open("day_scores.txt", "r") as file:
        count = 0
        for line in file:
            count += 1
            if count % 4 == 1:
                #Gather date data
                dates.append(datetime.strptime(line.strip(), "%Y-%m-%d"))
            elif count % 4 == 2:
                #Gather score data
                scores.append(int(line.strip()))

    plt.style.use('dark_background')
    #Create the plot
    fig, ax = plt.subplots()

    #Plot the data
    #ax.plot(dates, scores)

    #Format the x-axis to show dates
    ax.xaxis.set_major_locator(mdates.DayLocator())
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))

    #Make x-axis labels look cleaner
    fig.autofmt_xdate()

    dashed = [25, 50, 75, 100, 125, 150, 175, 200, 225, 250, 275, 300, 325, 350]
    ax.hlines(y=dashed, xmin=dates[0], xmax=dates[-1], colors='gray', linestyles='dashed', linewidth=0.5)
    ax.set_ylim(100, 350)

    ax.plot(dates, scores, marker='o', linestyle='-', color='cornflowerblue',markersize=8, markerfacecolor='crimson')
    
    average = sum(scores)/len(scores)
    ax.hlines(y=average, xmin=dates[0], xmax=dates[-1], colors='lightcoral', linestyles='dashed')
    ax.text(dates[0], average - 15, "Average Score: " + str(int(average)), verticalalignment='bottom', color='lightcoral')

    ax.set_xlabel("Date")
    ax.set_ylabel("Score")
    ax.set_title("Day scores")

    
    
    plt.show()


def run_day_scorer():
    if input("Would you like to add a new day (0) or view the score data (1)? ") == '0':
        day_scorer()
    else:
        show_plot()

run_day_scorer()