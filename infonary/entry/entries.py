from tags import taghandler
from content import description

class InfotionaryEntry():
    def __init__(self, title, content, tags):
        self.description = description.Description(title, content)
        self.tags = taghandler.TagHandler(tags)

    def change_description(self, new_content):
        self.description.overwrite_content(new_content)
        return self.description.get()

    def change_title(self, new_title):
        self.description.set_title(new_title)
        return self.description.get()

    def change_tags(self, new_tags):
        self.tags.initialize_tags(new_tags)
        return self.tags.get()

    def add_description(self, addition):
        self.description.add_content(addition)
        return self.description.get()

    def delete_tag(self, tag):
        self.tags.delete_tag(tag)
        return self.tags.get()

    def add_tag(self, new_tag):
        if type(new_tag) == str:
            self.tags.add_tag(new_tag)
        elif type(new_tag) == list:
            for tag in new_tag: self.tags.add_tag(tag)
        return self.tags.get()

    def get_description(self):
        return self.description.get()

    def get_tags(self):
        return self.tags.get()


def main():
    info = InfotionaryEntry('FunFact #1', 'Avokados sind giftig für Vögel.', ['Info', 'FunFact'])
    print(info.get_description())
    print(info.get_tags())
    print(info.change_description('Nee, das stimmt so nicht ganz.'))
    print(info.change_title('NotFunFact #1'))
    print(info.add_description(' Oder etwa doch?'))
    print(info.add_tag('Note'))
    print(info.delete_tag('Note'))

if __name__ == '__main__':
    main()
