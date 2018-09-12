import tags.tags as TT

class TagHandler():
    def __init__(self, tags):
        self.initialize_tags(tags)

    def add_tag(self, tag):
        if tag in [tag_obj.get(call='ID') for tag_obj in self.tags]:
            return self.tags
        else:
            self.tags.append(TT.__dict__[tag]())
            return self.tags

    def delete_tag(self, tag):
        for tag_obj in self.tags:
            if tag_obj.get(call='ID') == tag:
                self.tags.remove(tag_obj)
                return self.tags
        return self.tags

    def get(self):
        tagdict = {}
        for tag in self.tags:
            tagdict[tag.get(call='ID')] = tag.get() 
        return tagdict

    def initialize_tags(self, tags, **kwargs):
        # Check if tags are doubled:
        tags = list(set(tags))
        taglist = []
        for tag in tags:
            try:
                taglist.append(TT.__dict__[tag]())
            except KeyError:
                raise ReferenceError('Tag {} is not in TagList'.format(tag))
        self.tags = taglist
        return taglist




def main():
    th = TagHandler(['Info', 'History', 'Info'])
    th.add_tag('Info')
    th.add_tag('Note')
    th.delete_tag('History')

if __name__ == '__main__':
    main()
