class OptionTexts:
    """
    Class to return different options
    """

    def __init__(self):
        self._larger_than_zero = "Please type a number larger than 0 next time ;p "
        self._wrong_type = "Please enter a number next time!"
        self._coment_1 = "You got it!"

    def coment(self):
        return self._coment_1

    def larger_than_zero(self):
        return self._larger_than_zero

    def wrong_type(self):
        return self._wrong_type