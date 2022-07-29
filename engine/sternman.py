from engine.engine import Engine


class Sternman(Engine):
    def __init__(self, has_warning):
        self.has_warning = has_warning

    def service_needed(self):
        return self.has_warning
