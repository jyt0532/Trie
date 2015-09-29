class TrieNode:
    def __init__(self, count, depth):
        self.count = count
        self.depth = depth 
        self.children = Trie()
    def add_count(self, count):
        self.count = self.count+count

class Trie:
    def __init__(self):
        self.tree = {}
    def add_words(self, words, count, depth):
        if words[0] not in self.tree:
            self.tree[words[0]] = TrieNode(0, depth+1)

        if len(words) == 1:
            self.tree[words[0]].add_count(count)
        else:
            self.tree[words[0]].children.add_words(words[1:], count, depth+1)
    def print_trie(self):
        for key, value in self.tree.iteritems():
            tabs = ""
            for i in range(0, value.depth-1):
                tabs = tabs + "\t"
            print tabs + key + ":" + str(value.count)
            if bool(value.children):
                value.children.print_trie()
    def get_string_count(self, words):
        if words[0] not in self.tree:
            return 0
        else:
            if len(words) == 1:
                if self.tree[words[0]].count != 0:
                    return self.tree[words[0]].count
                else:
                    return 0
            else:
                return self.tree[words[0]].children.get_ngram_count(words[1:])

if __name__=="__main__":
    simple_trie = Trie()
    sentence1 = "apple ipad mini"
    sentence2 = "apple ipad"
    sentence3 = "apple"
    sentence4 = "apple ipad price"
    sentence5 = "banana"
    sentence6 = "banana ha ya"
    words1 = sentence1.split(" ")
    words2 = sentence2.split(" ")
    words3 = sentence3.split(" ")
    words4 = sentence4.split(" ")
    words5 = sentence5.split(" ")
    words6 = sentence6.split(" ")
    simple_trie.add_words(words1, 5, 0)
    simple_trie.add_words(words2, 4, 0)
    simple_trie.add_words(words3, 3, 0)
    simple_trie.add_words(words4, 2, 0)
    simple_trie.add_words(words5, 1, 0)
    simple_trie.add_words(words6, 6, 0)
    simple_trie.add_words(words4, 100, 0)
    simple_trie.print_trie()

    print simple_trie.get_ngram_count(["apple", "ipad", "bye"])
    print simple_trie.get_ngram_count(words4)
