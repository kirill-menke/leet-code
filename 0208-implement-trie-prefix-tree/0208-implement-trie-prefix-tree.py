class TrieNode:

    def __init__(self):
        self.links = [None] * 26
        self.is_end = False


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        
        for char in word:
            if node.links[ord(char) - ord('a')]:
                node = node.links[ord(char) - ord('a')]
            else:
                new_node = TrieNode()
                node.links[ord(char) - ord('a')] = new_node
                node = new_node
            
        node.is_end = True


    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if node.links[ord(char) - ord('a')]:
                node = node.links[ord(char) - ord('a')]
            else:
                return False
        
        return node.is_end
        

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if node.links[ord(char) - ord('a')]:
                node = node.links[ord(char) - ord('a')]
            else:
                return False

        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)