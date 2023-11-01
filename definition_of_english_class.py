# This is an English dictionary

class Dictionary:
    def __init__(self, directory):
        self.directory = directory
        self.keys = []
        self.values = []

    def is_even(self, number):
        if number % 2 == 0:
            return True
        return False

    def dictionary(self):
        with open(self.directory, 'r') as file:
            content = file.read()
            content = content.split(':')
            #    print(content)
            for i in content:
                if self.is_even(content.index(i)):
                    self.keys.append(i)
                else:
                    self.values.append(i)
            del self.keys[-1]
            self.diction = {}
            count = 0
            for _ in self.keys:
                self.keys[count] = self.keys[count].replace('\n', '')
                count += 1
            count = 0
            for _ in self.values:
                self.values[count] = [j for j in self.values[count]]
                self.values[count][0] = ''
                self.values[count] = ''.join(self.values[count])
                count += 1
            count = 0
            for _ in self.keys:
                self.diction[self.keys[count]] = self.values[count]
                count += 1

    def look_for_word(self):
        self.dictionary()
        print(f'Existing words are : ')
        for i in self.keys:
            print(f'in [{self.keys.index(i) + 1}] : {i}')
        key = input('Enter the word that you want the definition : ')
        try:
            print(f'{key} : {self.diction[key + " "]}')
        except KeyError:
            key = int(key)
            key -= 1
            print(f'{self.keys[key]}: {self.diction[self.keys[key]]}')


if __name__ == '__main__':
    dictionary = Dictionary('C:/Users/poori/OneDrive/Desktop/definitions.txt')
    # file.dictionary()
    dictionary.look_for_word()
