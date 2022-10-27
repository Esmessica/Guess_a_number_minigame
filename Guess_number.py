from option_texts import OptionTexts

class Range:
    
    """class for range specification"""

    def top_range(self):

        option = OptionTexts()
        _range_limit = input("Type a number: ")
    
        if _range_limit.isdigit():
            _range_limit = int(_range_limit)

        else:
            print(option.wrong_type)


