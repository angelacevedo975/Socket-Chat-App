class Message:
    def __init__(self, name, message):
        self.message=message
        self.name=name
        
    def to_string(self):
        return f"{self.name}: {self.message}"


class Conversation:
    
    def __init__(self):
        self.messages=[]
        self.members=[]
        
    def validate_member(self, name):
        return name in self.members
    
    def add_message(self, name, message):
        mess= Message(name, message)
        self.messages.append(mess)
        
    def to_string(self):
        return [mess.to_string() for mess in self.messages]
        