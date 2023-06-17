class wholeResource:
    def __init__(self, start_resource):
        self._resource = start_resource
        pass

    @property
    def start_resource(self):
        return self.start_resource
    
    @start_resource.setter
    def add_resource(self, input_resource):
        if input_resource >= 0:
            resource = resource + input_resource
            return resource
        else:
            raise ValueError("Input value cannot be nagative")
        
class Resource:
    def __init__(self, resource):
        self._resource = resource
    
    @property
    def resource(self):
        return self._resource
    
    @resource.setter
    def add_resource(self, input_more_value):
        if input_more_value < 0:
            raise ValueError("cannot input negative")
        self._resource = self._resource + input_more_value
        return self._resource

if __name__ == "__main__":
    # Worst Code
    # entire_pie = wholeResource(80)
    # entire_pie.add_resource(30)
    # print(entire_pie.resource)
    # entire_pie.resource

    # Good Code
    whole_resource = Resource(10)
    print(whole_resource.resource)
    whole_resource.add_resource = 24
    print(whole_resource.resource)