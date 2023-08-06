class Rock:
    def __init__(self, color='gray', location='USA', description='hard'):
        self.color = color
        self.location = location
        self.description = description
    
    def say_hi(self):
        return "rocks can't talk."

    def get_info(self):
        return "color: {}\nlocation: {}\ndescription: {}".format(self.color, self.location, self.description)
