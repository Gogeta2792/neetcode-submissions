class TrieNode:

    def __init__(self):
        self.children = {}
        self.isWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root

        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]

        curr.isWord = True    

    def search(self, word: str) -> bool:
        curr = self.root

        def dfs(idx, node):
            for i in range(idx, len(word)):
                c = word[i]

                if c == ".":
                    for child in node.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                
                else:
                    if c not in node.children:
                        return False
                    node = node.children[c]
            
            return node.isWord
        
        return dfs(0, curr)