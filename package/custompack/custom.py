
class PackageTest():
    msg = None
    def __init__(self, msg):
        self.msg = msg
    def __str__(self):
        return "Message: " + self.msg
