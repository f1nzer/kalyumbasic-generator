import markovify
import pandas as pd
import numpy as np

# Get raw text as string.
data1 = pd.read_csv('data.csv')

data1 = data1.replace(np.nan, '', regex=True)

text = '\n'.join(data1['text'].values.tolist())
text = text.replace(".", "\n")

# with open("pii/data.csv", "r") as f:
#     text = f.readlines()

# Build the model.
text_model = markovify.NewlineText(text)

# Print five randomly-generated sentences
for i in range(5):
    print(text_model.make_sentence())

# Print three randomly-generated sentences of no more than 280 characters
# for i in range(3):
#     print(text_model.make_short_sentence(280))
#     print()
