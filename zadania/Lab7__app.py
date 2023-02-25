import twint
from sentimentpl.models import SentimentPLModel

# load sentiment analysis model
model = SentimentPLModel(from_pretrained='latest')

# configure Twint search params
c = twint.Config()
c.Username = "AndrzejDuda"
c.Lang = "pl"
c.Limit = 10
c.Pandas = True
c.Pandas_clean = True
c.Hide_output = True

# run Twint
twint.run.Search(c)
df = twint.storage.panda.Tweets_df
df['sentiment'] = df.apply(lambda x: model(x['tweet']).item(), axis=1)

print(df[['tweet', 'hashtags', 'sentiment']])
