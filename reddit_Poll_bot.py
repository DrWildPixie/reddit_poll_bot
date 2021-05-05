reddit = praw.Reddit(
    client_id='' ,       #id from reddit
    client_secret='' ,	 #reddit secret phrase 	
    username='',	 #login
    password='',
    user_agent=''
    )


#choose ur subreddit and add u custom msg
subreddit = reddit.subreddit("Pick_ur_subreddit")
polls = []                        
for submission in subreddit.new():          #u can change hot to new or top
    if 'poll' in submission.selftext:
        polls.append(submission.url)
        submission.reply("Add ur custom msg"})


for poll in polls:
    print(poll)
