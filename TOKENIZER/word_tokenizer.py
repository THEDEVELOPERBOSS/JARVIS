import re
import json

with open("tokenizer.json", "r") as file:
    loaded_vocabulary = json.load(file)


if "[UNK]" not in loaded_vocabulary:
    raise ValueError("[UNK] is missing from the vocabulary") # value error actually stops the program if an error is detected

exists = []
for words in loaded_vocabulary:
    if words not in exists:
        exists.append(words)
    else:
        raise ValueError(f"Duplicate found{words}")
    
# Assing a unique ID to every token
token_to_id = {
    token: index
    for index, token in enumerate(loaded_vocabulary) # enumerate gives both the pos. and value of each item
}

# conversts text into numerical IDs
def encode(text): 
    
    tokens = re.findall(r"\w+|[,.!?]", text) # Splits the sentence into individual tokens using regex
    # Loop through those characters
    # Look up each character in token_to_id
    # Collect the resulting IDs
    token_ids = []
    for token in tokens: # generate a dictionary mapping token to IDs
        token_id = token_to_id.get( # searches for the word
            token, 
            token_to_id["[UNK]"] # retrieves fallback ID
        )
        token_ids.append(token_id)
        if token not in token_to_id:
            print(f"{token} is an unknown token")
    return token_ids # Return the numerical sequence

def decode(token_ids):
    decoded_text = ""
    for token in token_ids:
        token_text = loaded_vocabulary[token]
        
        if token_text in [",", ".", "!", "?"]:
            decoded_text = decoded_text + token_text
        else:
            if decoded_text == "":
                decoded_text = decoded_text + token_text
            else:
                decoded_text = decoded_text + " " + token_text
    return decoded_text
# testing 
test_sentences = [
    "Good morning, Sir!",
    "Good evening, Sir!",
    "Good afternoon, Sir"
]
for sentence in test_sentences:
    original = sentence
    encoded_text = encode(original)
    decoded_text = decode(encoded_text)
    if original == decoded_text:
        print(f"PASS: {sentence}")
    else:
        print(f"FAIL: {sentence}")
print(loaded_vocabulary)
print(type(loaded_vocabulary))
print(type(token_to_id))