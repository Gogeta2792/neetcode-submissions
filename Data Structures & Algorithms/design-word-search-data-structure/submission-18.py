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
            if c in cur.children:
                cur = cur.children[c]
            else:
                cur.children[c] = TrieNode()
                cur = cur.children[c]
        cur.isWord = True

    def search(self, word: str) -> bool:
        cur = self.root

        def dfs(node, idx):
            for i in range(idx, len(word)):
                c = word[i]

                if c == ".":
                    for child in node.children.values():
                        if dfs(child, i + 1):
                            return True
                    return False
                
                else:
                    if c not in node.children:
                        return False
                    node = node.children[c]
            
            return node.isWord
        
        return dfs(cur, 0)