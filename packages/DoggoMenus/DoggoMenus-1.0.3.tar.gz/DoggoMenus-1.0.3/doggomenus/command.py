from .errors import NotEnoughItemsError
from getch import pause

class Command:
    def __init__(self, title: str, function, **kwargs):
        self.function = function
        self.title = title

        # Options
        self.pause = kwargs.get("pause")

        self.args = kwargs.get("args", [])

    def _execute(self):
        self.function(*self.args)

        if self.pause: pause()

    def __str__(self):
        return self.title
        