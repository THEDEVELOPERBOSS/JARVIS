vocab = ['<blank>', ' '] + [chr(i) for i in range(97, 123)]  # <blank>, space, a-z

char_to_id = {ch: idx for idx, ch in enumerate(vocab)}
id_to_char = {idx: ch for ch, idx in char_to_id.items()}

def text_to_ids(text):
    """Convert text to a list of token IDs."""
    return [char_to_id[c] for c in text.lower() if c in char_to_id]
    # converts a string like Hello -> [8, 5, 12, 12, 15]
def ids_to_text(ids):
    """Convert a list of token IDs to string (removing blanks)."""
    return ''.join([id_to_char[i] for i in ids if i in id_to_char])
    # converts numeric ids back into readable text
    # ''.join(...) combines list of characters into full string