class Description():
    def __init__(self, title, content, **kwargs):
        self.title = title
        self.content = content

    def set_title(self, new_title):
        self.title = new_title
        return self.title

    def add_content(self, addition):
        self.content += addition
        return self.content

    def overwrite_content(self, new_content):
        self.content = new_content
        return self.content

    def get(self):
        return {'content': self.content, 'title': self.title}

    def get_content(self):
        return self.content

    def get_title(self):
        return self.title
        
