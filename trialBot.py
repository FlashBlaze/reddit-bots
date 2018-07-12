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
subreddit = reddit.subreddit('test')
redditor = reddit.redditor('spez')
submissionList = []
submissionList2 = []

"""
streamSubmissions streams the submissions till the 2nd last latest post and stores the submission ids in the submissionList list.
You can then access any submission by changeing the id value in submission.
"""


def streamSubreddit():
    count = 0
    for submission in subreddit.stream.submissions():
        count += 1
        if (count < 100):
            # sleep is used to
            time.sleep(1)
            print(submission.title)
            submissionList.append(submission.id)
        else:
            break

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
Yet to decide what to do with this one. 
WIP.
"""


def streamSubmissions():
    for submission in redditor.stream.submissions():
        print("Submission Post: " + submission.title)
        print(20 * '+')
        # time.sleep(3)
        # submissionList2.append(submission.id)
        subID = reddit.submission(id=str(submission))
        # subID.unsave()
        # for comment in subID.comments.list():
        #     print(20 * '-')
        #     print("Comment: " + comment.body)
        submission.reply("Beep beep! Comment from a bot!")


# saveSubmissions()
# streamSubmissions()
streamSubreddit()
