class entirePie:
    def __init__(self, start_resource):
        self._resource = start_resource
        pass

    @property
    def resource(self):
        return self._resource