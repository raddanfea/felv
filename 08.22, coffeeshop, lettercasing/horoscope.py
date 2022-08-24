from random import choice, randrange

zodiacs = ['Capricorn', 'Aquarius', 'Pisces', 'Aries', 'Taurus', 'Gemini', 'Cancer', 'Leo', 'Virgo', 'Libra', 'Scorpio',
           'Sagittarius', 'Capricorn']
symbols = ['♑', '♒', '♓', '♈', '♉', '♊', '♋', '♌', '♍', '♎', '♏', '♐', '♑']
dates = [22, 20, 19, 21, 20, 21, 21, 23, 23, 23, 23, 22]


def get_zodiac_index(month, day):
    if day < dates[month - 1]:
        return month - 1
    else:
        return month


start = ["You are a", "Gifted with the sign of",
         "Born as a true", "You were born under the zodiac of",
         "The stars shone you"]

emotional_leadup = ["Your life is filled with", "Most of your days you are taken by",
                    "You are generally filled with", "You are no stranger to"]
emotion = ["happiness", "sadness", "grief", "nervousness", "curiosity", "optimism"]

colors = ["red", "white", "blue", "green", "yellow", "pink", "brown", "black"]

if __name__ == '__main__':
    month = int(input("Enter the number of your month of birth:"))
    day = int(input("Enter the number of your day of birth:"))

    z_index = get_zodiac_index(month, day)
    zodiac = zodiacs[z_index]
    symbol = symbols[z_index]

    print('-' * 8)
    print('  ', symbol)
    print('-' * 8)

    print(f'{choice(start)} {zodiac}. {choice(emotional_leadup)} {choice(emotion)}.')
    print(f'Your lucky number today is: {randrange(1, 16)}')
    print(f'Your lucky color today is: {choice(colors)}')
    print(f'You are most compatible with: {zodiacs[12 - month]}')
