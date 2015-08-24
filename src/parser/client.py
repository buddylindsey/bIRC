class ClientParser(object):

    command_map = {
        '/connect': '',
        '/join': 'JOIN',
        '/disconnect': 'QUIT',
        '/part': 'PART'
    }

    def __init__(self, text):
        self.text = text

    def parse(self):
        self.tokenize()
        final_text = ''
        if self.tokens[0].startswith('/'):
            pass
        else:
            return self.text

    def tokenize(self):
        self.tokens = self.text.split(' ')
