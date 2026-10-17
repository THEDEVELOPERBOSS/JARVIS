import re

vocabulary = [
    "Good",
    "morning",
    "evening",
    "Sir",
    ",",
    ".",
    "!",
    "[UNK]" # stands for Unknown. Used for anything not in vocab
]

# Assing a unique ID to every token
token_to_id = {
    token: index
    for index, token in enumerate(vocabulary) # enumerate gives both the pos. and value of each item
}

# conversts text into numerical IDs
def encode(text): 
    
    tokens = re.findall(r"\w+|[,.!?]", text) # Splits the sentence into individual tokens using regex
    if token_ids not in vocabulary:
        token = "UNK"
    # Loop through those characters
    # Look up each character in token_to_id
    # Collect the resulting IDs
    token_ids = [
        token_to_id[token]
        for token in tokens
    ]
    token_to_id.get("UNK", "default")
    return token_ids # Return the numerical sequence

sentence = "Good morning, Sir!"
# \w+ captures one or more word characters
# [,.!?] Any single character inside the brackets
# | is an OR operator 
words_regex = re.findall(r"\w+|[.!?]", sentence)

print(encode("Good morning, Sir!"))
print(encode("Good evening, Sir!"))
print(encode("Good afternoon, Sir"))