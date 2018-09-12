from entry import entries

import json

class Infotionary():
    def __init__(self, load_path='./info_save.json', file_type='json'):
        self.entries = self.load_entries(load_path, file_type=file_type)

    def load_entries(self, path, file_type='json'):
        if file_type == 'json':
            fobj = open(path, 'r')
            data = json.load(fobj)
            fobj.close()
            entries = self.__setup_entries_from_data(data['Entries'],
                                                     file_type=file_type)
            return entries

    def save_entries(self, path, file_type='json'):
        if file_type == 'json':
            data = [{'description': entry.get_description(), 'tags': entry.get_tags()}
                    for entry in self.entries.values()]
            fobj = open(path, 'w')
            json.dump({'Entries': data}, fobj, indent=4, sort_keys=True)
            fobj.close()
            return self.entries

    def add_entry(self, title, content, tags):
        if title in self.entries:
            print('Warning: You overwrote entry of title {}'.format(title))
        self.entries[title] = entries.InfotionaryEntry(title, content, tags)
        return self.entries

    def delete_entry(self, title):
        del self.entries[title]
        return self.entries

    def edit_entry(self, title, edition, type_of_change='title', overwrite_attribute=False):
        if type_of_change == 'title':
            entry_to_edit = self.entries[title]
            entry_to_edit.change_title(edition)
            del self.entries[title]
            self.entries[edition] = entry_to_edit
            return self.entries

        elif type_of_change == 'description':
            if overwrite_attribute:
                self.entries[title].change_description(edition)
                return self.entries
            else:
                self.entries[title].add_description(edition)
                return self.entries

        elif type_of_change == 'tags':
            if overwrite_attribute:
                self.entries[title].change_tags(edition)
                return self.entries
            else:
                self.entries[title].add_tag(edition)
                return self.entries
                

    def __setup_entries_from_data(self, data, file_type='json'):
        entry_dict = {}
        if file_type == 'json':
            for entry in data:
                description = entry['description']
                tags = entry['tags']

                entry_dict[description['title']] = entries.InfotionaryEntry(description['title'],
                                                                            description['content'],
                                                                            tags.keys())
            return entry_dict            


        
def main():
    info = Infotionary()
    info.save_entries('./info_save.json')
    info.load_entries('./info_save.json')
    print(info.add_entry('FunFact #2', 'Nahaa', ['Info']))
    print(info.delete_entry('FunFact #2'))
    print(info.edit_entry('FunFact #1', ['Info', 'Note'], type_of_change='tags'))
    print(info.entries['FunFact #1'].get_tags())
    

if __name__ == '__main__':
    main()
