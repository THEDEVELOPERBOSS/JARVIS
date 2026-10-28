# intial vocabulary
vocabulary = ["J", "A", "R", "V", "I", "S"]
# Assing a unique ID to every token
token_to_id = {
    token: index
    for index, token in enumerate(vocabulary) # enumerate gives both the pos. and value of each item
}
# conversts text into numerical IDs
def encode(text): 
    
    tokens = list(text) # splits the string into individual charcters
    # Loop through those characters
    # Look up each character in token_to_id
    # Collect the resulting IDs
    token_ids = [
        token_to_id[token]
        for token in tokens
    ]
    
    return token_ids # Return the numerical sequence
# run with this to test encode function
print(encode("JARVIS")) 