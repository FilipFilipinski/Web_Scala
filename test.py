def round_to_half(i):
    i = str(round(i, 1))
    first_character = int(float(i))
    last_character = i[-1]
    if int(last_character) >= 5:
        last_character = 5
    else:
        last_character = 0
    return f'{first_character}.{last_character}'


round_to_half(5.6341341431434)
round_to_half(5.42142142143113)
round_to_half(5.49142142143113)
round_to_half(5.0)
