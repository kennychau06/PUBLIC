from hashlib import sha256
import praw


r = praw.Reddit(username='wsbgodbot',
                     password=sha256('password'.encode('utf-8')).hexdigest(),
                     client_id='JOQZ4WgNVr-7fw',
                     client_secret='UzxwUw6wzHI2omWmmGfMz9eiQUA',
                     user_agent="wsbgod's N.1 insider information provider")

print('Script running... please wait\n--\n')


batch_size = 25
runs = 0

subreddit = 'wallstreetbets'


puts_titles = 0
calls_titles = 0
puts_post_text = 0
calls_post_text = 0
puts_comments = 0
calls_comments = 0

while True:

    for post in r.subreddit(subreddit).hot(limit=batch_size):

        post.comments.replace_more(limit=0)

        st = post.selftext
        t = post.title

        if 'put' in t: puts_titles += 1
        if 'call' in t: calls_titles += 1

        if 'put' in st: puts_post_text += 1
        if 'call' in st: calls_post_text += 1

        for comment in post.comments:
            if 'put' in comment.body: puts_comments += 1
            if 'call' in comment.body: calls_comments += 1

    runs += 1

    points = (calls_titles+calls_post_text+puts_titles+puts_post_text)*2 + calls_comments+puts_comments
    sentiment = round(((calls_titles*2+calls_post_text*2+calls_comments) - (puts_titles*2+puts_post_text*2+puts_comments))/points*100, 2)

    txt = '(positive)' if sentiment > 0 else '(negative)'
    print(f'>> Calculated Sentiment: {sentiment}% {txt}\n\n'
        + f'Titles (weighted at 2 points):\n# of Postive titles: {calls_titles}\n# of Negative titles: {puts_titles}\n\n'
        + f'Post Text (also weighted at 2 points):\n# of Postive texts: {calls_post_text}\n# of Negative texts: {puts_post_text}\n\n'
        + f'Comments (1 point):\n# of Postive comments: {calls_comments}\n# of Negative comments: {puts_comments}\n\n\n'
        + f'Sampled {runs} batch(es); keep running to anaylse more posts\n--------\n\n')






