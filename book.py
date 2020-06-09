class Book():
    def __init__(self, name='', authorName='', memberLegajo=''):
        self.name = name.upper()
        self.authorName = authorName.upper()
        self.memberLegajo = memberLegajo

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name.upper()

    @property
    def authorName(self):
        return self._authorName

    @authorName.setter
    def authorName(self, authorName):
        self._authorName = authorName.upper()

    @property
    def memberLegajo(self):
        return self._memberLegajo

    @memberLegajo.setter
    def memberLegajo(self, value):
        self._memberLegajo = value
