class C:

    def __index__(self):
        self._x = None

    @property
    def x(self):
        """Doc de la property x"""
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @x.deleter
    def x(self):
        del self._x