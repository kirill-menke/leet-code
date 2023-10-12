class TrieNode:
    def __init__(self):
        self.links = [None] * 26
        self.is_end = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            if not curr.links[ord(char) - ord('a')]:
                curr.links[ord(char) - ord('a')] = TrieNode()
            curr = curr.links[ord(char) - ord('a')]    
    
        curr.is_end = True

    def search(self, word: str) -> bool:
        def search_helper(word, start_node):
            curr = start_node
            for i, char in enumerate(word):
                if char == '.':
                    for node in curr.links:
                        if node and search_helper(word[i + 1:], node):
                            return True
                    return False
                if not curr.links[ord(char) - ord('a')]:
                    return False
                curr = curr.links[ord(char) - ord('a')]
            
            return curr.is_end

        return search_helper(word, self.root)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)