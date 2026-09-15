class TrieNode:
    
    def __init__(self):
        self.children = {}
        self.isWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root

        for c in word:
            if not c in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        
        cur.isWord = True

    def search(self, word: str) -> bool:
        cur = self.root
        
        def dfs(idx, node):
            for i in range(idx, len(word)):
                if word[i] == ".":
                    for child in node.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                else:
                    if word[i] not in node.children:
                        return False
                    node = node.children[word[i]]
            return node.isWord
        
        return dfs(0, cur)