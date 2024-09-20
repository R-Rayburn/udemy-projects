# SRP SOC
class Journal:
    def __init__(self):
        self.entries = []
        self.count = 0

    def add_entry(self, text):
        self.count += 1
        self.entries.append(f'{self.count}: {text}')
    
    def remove_entry(self, pos):
        del self.entries[pos]

    def __str__(self):
        return '\n'.join(self.entries)

    # Secondary responsibility added to Journal
    #  keeping persistance
    # def save(self, filename):
    #     file = open(filename, 'w')
    #     file.write(str(self))
    #     file.close()
    
    # def load(self, filename):
    #     pass

    # def load_from_web(self, uri):
    #     pass

class PersistanceManager:
    @staticmethod
    def save_to_file(journal, filename):
         file = open(filename, 'w')
         file.write(str(journal))
         file.close()
    
    @staticmethod
    def load(self, filename):
        pass

j = Journal()
j.add_entry('Reviewing Design Prinicples.')
j.add_entry('SRP Review.')
print(f'Journal entires:\n{j}')

file = r'~/journal.txt'
PersistanceManager.save_to_file(j, file)

with open(file) as f:
    print(f.read())

# Anti-pattern we see
# GOD OBJ
# - Puts everyting into a single class
# - Dumps everything into one class and give it many responsibilities