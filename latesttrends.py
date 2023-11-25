import pytrends
from pytrends.request import TrendReq
import pandas as pd

import openai

openai.api_key = ''

pytrends = TrendReq(hl='en-US', tz=360)



kw_list = ["machine learning"]
pytrends.build_payload(kw_list, cat=0, timeframe='today 12-m')

data  = pytrends.related_queries()

print(data['machine learning']['top'])


keywords = pytrends.suggestions(keyword='Business Intelligence')
df = pd.DataFrame(keywords)
print(df['query'][0])






print(pytrends.trending_searches(pn='united_states'))
pytrends.trending_searches(pn='japan') # Japan

