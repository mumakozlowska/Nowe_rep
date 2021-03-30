def convert_roman2arabic(roman):
    rom_arab = {
        "M": 1000,
        "D": 500,
        "C": 100,
        "L": 50,
        "X": 10,
        "V": 5,
        "I": 1
    }
    result = rom_arab[roman[-1]]
    for i in range(len(roman)-1,0, -1):
        if rom_arab[roman[i - 1]] < rom_arab[roman[i]]:
            result -= rom_arab[roman[i - 1]]
        else:
            result += rom_arab[roman[i - 1]]
    return result

    print(result)

    def test_converter2(fun):
        cases = {
            "IV": 4,
            "VII": 7,
            "XIX": 19,
            "XL": 40,
            "XCV": 95,
            "CM": 900,
            "MXXV": 1025,
            "MCMXCV": 1995,
            "MM": 2000,
            "MCMLVI": 1956,
            "MMXI": 2011,
            "MMMDCCCLXXXVIII": 3888,
        }
        for key, value in cases.items():
            print(f'{fun.__name__}("{key}") == {fun(key)}')
            assert fun(key) == value
