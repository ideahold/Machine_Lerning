from textblob import TextBlob

msg = "I'm feel sad yesterday"
# msg1 = "A wonderful bird is the pelican, His bill will hold more than his belican, He can take in his beak Enough food for a week"

analysis = TextBlob(msg)
print(analysis.sentiment)
