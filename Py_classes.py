
class Authentication(object):
    def _init_(self,username = ''):
        self.username = username
        def lower(self):
            lower = any(c.islover() for c in self.username)
            return lower
            def upper(self):
                upper = any(c.isupper() for c in self.username)
                return upper
    def digit(self):
        digit = any(c.isdigit() for c in self.username)
        return digit
        def validate(self):
            lower = self.lower()
            upper = self.upper()
            digit = self.digit()
            length = len(self.username)
        report = lower and upper and digit and length >= 6
        if report:
            print("acess granted")
            return True