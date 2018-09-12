class Tag():
    def __init__(self, tag_id, **kwargs):
        self.verbose = False
        self.information = {}
        self.information['ID'] = tag_id
        self.information.update(kwargs)

    def get(self, call='all'):
        if call == 'all':
            return self.information
        else:
            return self.information[call]

    def edit(self, edition, call='all'):
        if call == 'all':
            assert type(edition) == dict, 'If call-keyword is wanted, you have to pass a dictionary.'
            self.information = edition
            return self.information
        else:
            self.information[call] = edition
            return self.information

class Info(Tag):
    def __init__(self, **kwargs):
        self.id = 'Info'
        super().__init__(self.id, **kwargs)

class Idea(Tag):
    def __init__(self, **kwargs):
        self.id = 'Idea'
        super().__init__(self.id, **kwargs)

class History(Tag):
    def __init__(self, **kwargs):
        self.id = 'History'
        super().__init__(self.id, **kwargs)

class Note(Tag):
    def __init__(self, **kwargs):
        self.id = 'Note'
        super().__init__(self.id, **kwargs)

class FunFact(Tag):
    def __init__(self, **kwargs):
        self.id = 'FunFact'
        super().__init__(self.id, **kwargs)




        

def main():
    info = Info()
    idea = Idea()
    hist = History(**{'date': '20.5.1634'})
    note = Note()

    print(info.get())
    print(idea.get(call='ID'))
    print(hist.get(call='date'))
    print(note.edit('21.6.1984', call='EditDate'))

if __name__ == '__main__':
    main()
    
            
