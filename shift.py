def shift(letter, value, alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
    N = len(alphabet)
    idx = alphabet.index(letter.upper())
    new_idx = idx + value
    while new_idx < 0 or new_idx > N-1:
        if new_idx < 0:
            new_idx += N
        if new_idx > N-1:
            new_idx -= N
    return alphabet[new_idx]
