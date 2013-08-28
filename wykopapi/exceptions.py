__author__ = 'astrojek'

class WykopException(Exception):

    def __init__(self, message, code):
        super(WykopException, self).__init__(message)

        self.code = code
