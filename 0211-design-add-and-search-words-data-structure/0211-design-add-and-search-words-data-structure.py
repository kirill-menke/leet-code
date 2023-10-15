class WordDictionary:

    def __init__(self):
        self.root = {}

    def addWord(self, word: str) -> None:
        current = self.root

        for char in word:
            if char not in current:
                current[char] = {}
            current = current[char]
        
        current['$'] = True


    def search(self, word: str) -> bool:
        
        def search_helper(start_node, word):
            for i, char in enumerate(word):
                if char == '.':
                    for link in start_node:
                        if link != '$' and search_helper(start_node[link], word[i + 1:]):
                            return True
                    return False
                elif char not in start_node:
                    return False
                else:
                    start_node = start_node[char]
            
            return '$' in start_node

        return search_helper(self.root, word)



# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)