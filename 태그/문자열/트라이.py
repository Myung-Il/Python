class Node(object):
    def __init__(self, key, flag, child=None) -> None:
        self.key = key
        self.flag = flag
        self.child = {}

class Trie:
    def __init__(self) -> None:
        self.head = Node(None)
    
    def insert(self, string):
        current_node = self.head

        for char in string:
            if char not in current_node.child:
                current_node.child[char] = Node(char)
            current_node = current_node.child[char]

        current_node.child = string
    
    def search(self, string):
        current_node = self.head

        for char in string:
            if char in current_node.child:
                current_node = current_node.child[char]
            else: return False
        if current_node.data != None:
            return True
        

if __name__=="__main__":
    trie = Trie()
    word_list = ["frodo", "front", "firefox", "fire"]
    for word in word_list:
        trie.insert(word)

    print(trie.search("friend"))
    print(trie.search("front"))