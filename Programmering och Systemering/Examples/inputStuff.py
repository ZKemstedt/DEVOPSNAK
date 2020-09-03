# Om ni vill hantera fel i input

def float_input(message, retries = 3):
    try:
        return float(input(message))
    except ValueError:
        if(retries > 0):
            retries -= 1
            return float_input(f'[Försök ingen med en float] {message}', retries)
        raise

salary = float_input("Önskad lön: ")