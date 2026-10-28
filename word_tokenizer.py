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
    # Loop through those characters
    # Look up each character in token_to_id
    # Collect the resulting IDs
    token_ids = []
    for token in tokens:
        token_id = token_to_id.get(
            token, 
            token_to_id["[UNK]"]
        )
        token_ids.append(token_id)
        if token not in token_to_id:
            print(f"{token} is an unknown token")
    return token_ids # Return the numerical sequence
def decode(token_ids):
    tokens = []
    for token in token_ids:
        token_id = vocabulary.get(
            token, 
            vocabulary["[UK]"]
        )
    tokens.join(token_id)

print(encode("Good morning, Sir!"))
print(encode("Good evening, Sir!"))
print(encode("Good afternoon, Sir"))