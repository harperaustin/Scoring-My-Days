from datetime import datetime

day_scores = []

def check_valid_date(date):

    #First check if the date is even possible or in the correct format
    try:
        parsed_date = datetime.strptime(date, "%Y-%m-%d")
        #Checking if it is a future date
        if parsed_date > datetime.now():
            print("Date is in the future")
            return False
        
        print("format correct")
        return True
    except ValueError:
        print("Format incorrect")
        return False
    
    #Now need to check if that date has already been scored
    #I can just run a for loop through day_scores to see if that date is already there
    
def getting_date():
    
    curr_ans = input("Are you scoring today (0) or a prior date(1)? ")
    if curr_ans == '0':
        date = datetime.now().date().strftime("%Y-%m-%d")
        print(date)
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
            score += 335
        elif curr_ans == 'b':
            score += 300
        else:
            score += 250

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

        if input("Did you go outside for at least an hour? (y/n) ") == 'y':
            score += 25

        curr_ans = input("Did you scroll on social media NONE (a), under 30 minutes (b), or more than 30 minutes (c)? ")
        if curr_ans == 'a':
            score += 25
        elif curr_ans == 'b':
            score += 10

        if input("Did you do something productive (work, school, etc? (y/n) ") == 'y':
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

        curr_ans = input("Are you going to sleep before 11 (a), before 1 (b), or later(c)? ")
        if curr_ans == 'a':
            score += 10
        elif curr_ans == 'b':
            score += 5

        if input("Are you going to fall asleep with your phone on? (y/n) ") == 'n':
            score += 5

    #max score 335
    return score







        
         



def day_scorer():
    date = getting_date()
    print(date)
    score = get_score()
    note = input("Add a brief note about this day: ")
    day_scores.append([date, score, note])
    with open("day_scores.txt", "a" ) as file:
        file.write(str(date) + '\n' + str(score) + "\n" + str(note) +'\n\n')
        

day_scorer()