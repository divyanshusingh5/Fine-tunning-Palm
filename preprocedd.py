import pandas as pd
from io import StringIO

def preprocess_chat_data(text_data):
    # Read the data into a pandas DataFrame
    columns = ['Question', 'Answer', 'Recommendation']
    df = pd.read_csv(StringIO(text_data), sep='\t', header=None, names=columns, quoting=3, engine='python')

    # Remove unnecessary backslashes and newline characters
    df['Question'] = df['Question'].str.replace(r'\\N', '')
    df['Answer'] = df['Answer'].str.replace(r'\\N', '')
    df['Recommendation'] = df['Recommendation'].str.replace(r'\\N', '')

    return df

# Example usage
text_data = """Did you do your regular exercise today?\tNo\t\\N
How are you feeling today?\tGood\t\\N
Did you have a healthy breakfast?\tNo\t\\N
... (your remaining data)"""

preprocessed_data = preprocess_chat_data(text_data)

# Display the preprocessed data
print(preprocessed_data)
