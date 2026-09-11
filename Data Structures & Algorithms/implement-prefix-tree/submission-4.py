class TreeNode:

    def __init__(self):
        self.children = {}
        self.isWord = False

class PrefixTree:

    def __init__(self):
        self.root = TreeNode()

    def insert(self, word: str) -> None:
        curr = self.root

        for c in word:
            if c in curr.children:
                curr = curr.children[c]
            else:
                curr.children[c] = TreeNode()
                curr = curr.children[c]

        curr.isWord = True

    def search(self, word: str) -> bool:
        curr = self.root

        for c in word:
            if c in curr.children:
                curr = curr.children[c]
            else:
                return False
            
        return curr.isWord

    def startsWith(self, prefix: str) -> bool:
        curr = self.root

        for c in prefix:
            if c in curr.children:
                curr = curr.children[c]
            else:
                return False
            
        return True