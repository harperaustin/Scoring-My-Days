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
    if input("Was the day a special day? (y/n) ").lower() == "y":
        #DO SPECIAL DAY SCORING HERE
        print("Special day!")
        return 100
    else:
        print("Normal day scoring")
        



def day_scorer():
    date = getting_date()
    print(date)
    score = get_score()

day_scorer()