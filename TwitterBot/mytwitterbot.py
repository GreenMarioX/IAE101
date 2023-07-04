# mytwitterbot.py
# IAE 101, Fall 2021
# Project 04 - Building a Twitterbot
# Name: Steven Tung
# netid: stetung
# Student ID: 114437192
import datetime
import sys
import time, random
import simple_twit

# Assign the string values that represent your developer credentials to
# each of these variables; credentials provided by the instructor.
# If you have your own developer credentials, then this is where you add
# them to the program.
# Consumer Key also known as API key
CONSUMER_KEY = "b37NODAQBwDTT7QqLcM6gZMsR"
# Consumer Secret also known as API Key Secret
CONSUMER_SECRET = "luCsdclCIafY3qu1LaWM2OoUpuwZ4tKPIU4AI0Q0UIIDWkriQg"

# Project 04 Exercises
    
# Exercise 1 - Get and print 10 tweets from your home timeline
# For each tweet, print the tweet ID, the author's name,
# the author's screen_name, the tweet creation date, and the
# tweet full_text
def exercise1(api):
    homeTimeLine = simple_twit.get_home_timeline(api, 10)
    for status in homeTimeLine:
        print("---Twitter-Tweet---------------------------"
              + "\nTweet ID: " + str(status.id)
              + "\nAuthor: " + status.author.name
              + "\nAuthor Screen Name: " + status.author.screen_name
              + "\nCreation Date: " + str(status.created_at)
              + "\nFull text: \n" + status.full_text
              + "\n-------------------------------------------")

# Exercise 2 - Get and print 10 tweets from another user's timeline
# For each tweet, print the tweet ID, the author's name,
# the author's screen_name, the tweet creation date, and the
# tweet full_text
def exercise2(api):
    otherTimeLine = simple_twit.get_user_timeline(api, "NCIS_CBS", 10)
    for status in otherTimeLine:
        print("---Twitter-Tweet---------------------------"
              + "\nTweet ID: " + str(status.id)
              + "\nAuthor: " + status.author.name
              + "\nAuthor Screen Name: " + status.author.screen_name
              + "\nCreation Date: " + str(status.created_at)
              + "\nFull text: \n" + status.full_text
              + "\n-------------------------------------------")

# Exercise 3 - Post 1 tweet to your timeline.
def exercise3(api):
    simple_twit.send_tweet(api, "Greetings! This is a test of our systems!")

# Exercise 4 - Post 1 media tweet to your timeline.
def exercise4(api):
    simple_twit.send_media_tweet(api, "Hello World!", "media/hello-wave.gif")

# End of Project 04 Exercises


# YOUR BOT CODE GOES IN HERE
def twitterbot(api):
    while True:
        daysInMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        dateDay = datetime.date.today().day
        dateMonth = datetime.date.today().month
        dateYear = datetime.date.today().year

        daysElapsed = dateDay
        for num in range(dateMonth - 1):
            daysElapsed += daysInMonth[num]
        percent = round(daysElapsed / 365 * 100, 2)
        daysLeft = 365 - daysElapsed
        phrases = ["What a year to remember!", "What a fast year!", "Oh how time just seems to speed by!",
                   "It feels like the new year just started!", "This just reminds us of how fast time is!",
                   "Treasure your time because it is only limited!", "Time just flies!"]
        randomNum = random.randint(0, len(phrases) - 1)
        phrase = phrases[randomNum]
        tweet = "As of " + str(dateMonth) + '/' + str(dateDay) + "/" + str(dateYear) + ", we are " \
                + str(percent) + "% of the way through the year! Only " + str(daysLeft) + " days left in the year! " \
                + str(phrase)
        simple_twit.send_tweet(api, tweet)
        print(tweet)
        # Sleep for 3 days
        time.sleep(259200)


if __name__ == "__main__":
    # This call to simple_twit.create_api will create the api object that
    # Tweepy needs in order to make authenticated requests to Twitter's API.
    # Do not remove or change this function call.
    # Pass the variable "api" holding this Tweepy API object as the first
    # argument to simple_twit functions.
    simple_twit.version()
    api = simple_twit.create_api(CONSUMER_KEY, CONSUMER_SECRET)

    # Once you are satisified that your exercises are completed correctly
    # you may comment out these function calls.
    # print("Exercise 1")
    # exercise1(api)
    # print("\nExercise 2")
    # exercise2(api)
    # print("\nExercise 3 and 4")
    # exercise3(api)
    # exercise4(api)
    # print("Tweets have been sent!")

    # This is the function call that executes the code you defined above
    # for your twitterbot.
    twitterbot(api)
