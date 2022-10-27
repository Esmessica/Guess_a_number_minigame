from option_texts import OptionTexts

class Range:
    
    """class for range specification"""

    def top_range(self):

        option = OptionTexts()
        self._range_limit = input("Type a number: ")
    
        if self._range_limit.isdigit():
            self._range_limit = int(self._range_limit)

            if self._range_limit <= 0 :
                print(option.larger_than_zero)
                input()
        else:
            print(option.wrong_type)
    def limit(self):
        return self._range_limit


