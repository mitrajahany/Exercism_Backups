def response(hey_bob):
    hey_bob = hey_bob.strip()

    if hey_bob.isupper() and (not hey_bob.endswith('?')):
        return "Whoa, chill out!"
    elif hey_bob.isupper():
        return "Calm down, I know what I'm doing!"
    elif hey_bob.endswith('?'):
        return "Sure."
    elif hey_bob == '':
        return "Fine. Be that way!"
    else:
        return "Whatever."
    