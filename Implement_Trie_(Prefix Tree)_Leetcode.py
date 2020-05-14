class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._endofword = "N"
        self.trie = dict()
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        cur = self.trie
        
        for i in word:
            if i not in cur:
                cur[i] = {"endofword": self._endofword}
            cur = cur[i]
            
        cur["endofword"] = "Y"
        # print(self.trie)

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        cur = self.trie
        
        for i in word:
            if i not in cur:
                return False
            cur = cur[i]
        if "endofword" in cur and cur["endofword"] == "Y":
            return True
        else:
            return False
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        cur = self.trie
        
        for i in prefix:
            if i in cur:
                cur = cur[i]
            else:
                return False
        return True
        