class WelcomeText:

    """Class for printing welcome text"""

    def __init__(self):
        """constructor of class WelcomeText"""
        self._line = "--------------------------------------------"
        self._text = "Hello! Welcome to Guess a number minigame!"


    def __str__(self):
        """String representation of WelcomeText"""
        return (f"{self._line}\n{self._text}\n{self._line}\n")