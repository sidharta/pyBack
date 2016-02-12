class Item(object):

    def __init__(self, id):
        self.id = id
        # Additional fields

    def __repr__(self):
        return 'Item {}>'.format(self.id)
