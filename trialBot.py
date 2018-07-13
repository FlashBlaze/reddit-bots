import praw
import time
import config

reddit = praw.Reddit(client_id=config.client_id,
                     client_secret=config.client_secret,
                     username=config.username,
                     password=config.password,
                     user_agent=config.user_agent)

"""
Change the subreddit and redditor to your choice.
"""
subreddit = reddit.subreddit('politics')
redditor = reddit.redditor('spez')
keyWords = ["twitter", "government", "trump"]
submissionList = []
submissionList2 = []

"""
streamSubreddit streams particular subreddit and displays the submissions containing particular words from keyWords list
"""


def streamSubreddit():
    for submission in subreddit.stream.submissions():
        time.sleep(0.2)
        for word in keyWords:
            if word in submission.title.lower():
                print(submission.title)
            else:
                pass

    submission = reddit.submission(id=submissionList[-1])
    print(submission.title)


"""
saveSubmissions saves the new submissions posted by a redditor. 
"""


def saveSubmissions():
    count = 0
    for submission in redditor.submissions.new():
        # submissionList.append(submission.id)
        # submission = reddit.submission(id=submissionList[-0])
        count += 1
        if (count < 5):
            submission.save()
        else:
            pass


"""
replyToSubmissions replies to new submissions by a redditor in a particular subreddit
Currently there is an issue with the rate limit. I will look into it later on.
"""


def replyToSubmissions():
    for submission in redditor.submissions.new():
        for submit in subreddit.search(submission.title):
            if submission.title == submit.title:
                print(submission.title)
                submission.reply("Beep beep! Comment from a bot!")
            else:
                pass
    # submission = reddit.submission(id=submissionList2[1])
    # print(submission.title)
    # submission.reply("Badoop da badoop da! Reply from a bot!")


# saveSubmissions()
# streamSubmissions()
replyToSubmissions()
