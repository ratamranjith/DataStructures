'''
Trie Data Structure:
    A Trie (pronounced as "try") is a tree-like data structure that is used to efficiently store and retrieve keys in a dataset of strings.
    It is also known as a prefix tree because it can be used to search for prefixes of a given string.

Key Characteristics of a Trie:
- Nodes and Edges: Each node in the Trie represents a single character of the key. 
                   The root node is usually empty, and the edges between nodes represent the connection between character.
- Prefix Matching: Trie is very efficient for prefix matching. It allows for quick lookups, insertions, and deletions.
- End of Word Marker: Nodes may have a marker to indicate the end of a valid word or key.
- Space Efficiency: Tries can be more space-efficient than hash tables when dealing with large datasets, especially when keys share common prefixes.

Operations on a Trie:
- Insertion: To insert a word, traverse the Trie, creating nodes as needed for each character. 
             Mark the end of the word in the last node.
- Search: To search for a word, traverse the Trie following the nodes corresponding to each character in the word. 
          If you reach the end of the word and the end marker is present, the word exists in the Trie.
- Deletion: Deleting a word involves traversing the Trie to find the word and then removing the end marker. 
            If the word shares nodes with other words, only the end marker is removed; otherwise, unnecessary nodes are deleted.

Example Structure:
Consider inserting the words "cat", "car", "cart", and "dog" into a Trie:

In this Trie:

"cat" ends at the first "t" node.
"car" ends at the "r" node.
"cart" extends from "car" with an additional "t" node.
"dog" is in a separate branch under "d".
Examples of Tries with Different Strings:
Here are 20 different examples of Tries built with various sets of words:

Insert "apple", "ape", "bat", "ball", "bar":
Root → a → p → p → l → e (end)
Root → a → p → e (end)
Root → b → a → t (end)
Root → b → a → l → l (end)
Root → b → a → r (end)

Insert "hello", "help", "helmet", "hero":
Root → h → e → l → l → o (end)
Root → h → e → l → p (end)
Root → h → e → l → m → e → t (end)
Root → h → e → r → o (end)

Insert "ant", "anthem", "anchor", "angle":
Root → a → n → t (end)
Root → a → n → t → h → e → m (end)
Root → a → n → c → h → o → r (end)
Root → a → n → g → l → e (end)

Insert "rat", "rate", "ratify", "rattle":
Root → r → a → t (end)
Root → r → a → t → e (end)
Root → r → a → t → i → f → y (end)
Root → r → a → t → t → l → e (end)

Insert "sun", "sunny", "sunlight", "solar":
Root → s → u → n (end)
Root → s → u → n → n → y (end)
Root → s → u → n → l → i → g → h → t (end)
Root → s → o → l → a → r (end)

Insert "frog", "frost", "freeze", "frozen":
Root → f → r → o → g (end)
Root → f → r → o → s → t (end)
Root → f → r → e → e → z → e (end)
Root → f → r → o → z → e → n (end)

Insert "blue", "blush", "blow", "black":
Root → b → l → u → e (end)
Root → b → l → u → s → h (end)
Root → b → l → o → w (end)
Root → b → l → a → c → k (end)

Insert "tree", "trick", "trip", "train":
Root → t → r → e → e (end)
Root → t → r → i → c → k (end)
Root → t → r → i → p (end)
Root → t → r → a → i → n (end)

Insert "sky", "skate", "skill", "ski":
Root → s → k → y (end)
Root → s → k → a → t → e (end)
Root → s → k → i → l → l (end)
Root → s → k → i (end)

Insert "cat", "can", "candy", "cap":
Root → c → a → t (end)
Root → c → a → n (end)
Root → c → a → n → d → y (end)
Root → c → a → p (end)

Insert "star", "start", "stare", "stark":
Root → s → t → a → r (end)
Root → s → t → a → r → t (end)
Root → s → t → a → r → e (end)
Root → s → t → a → r → k (end)

Insert "jump", "jungle", "just", "juice":
Root → j → u → m → p (end)
Root → j → u → n → g → l → e (end)
Root → j → u → s → t (end)
Root → j → u → i → c → e (end)

Insert "king", "kite", "kind", "kick":
Root → k → i → n → g (end)
Root → k → i → t → e (end)
Root → k → i → n → d (end)
Root → k → i → c → k (end)

Insert "road", "roam", "rock", "root":
Root → r → o → a → d (end)
Root → r → o → a → m (end)
Root → r → o → c → k (end)
Root → r → o → o → t (end)

Insert "fish", "fit", "fix", "fist":
Root → f → i → s → h (end)
Root → f → i → t (end)
Root → f → i → x (end)
Root → f → i → s → t (end)

Insert "leaf", "learn", "leap", "least":
Root → l → e → a → f (end)
Root → l → e → a → r → n (end)
Root → l → e → a → p (end)
Root → l → e → a → s → t (end)

Insert "moon", "mood", "move", "mock":
Root → m → o → o → n (end)
Root → m → o → o → d (end)
Root → m → o → v → e (end)
Root → m → o → c → k (end)

Insert "pine", "pink", "pin", "pipe":
Root → p → i → n → e (end)
Root → p → i → n → k (end)
Root → p → i → n (end)
Root → p → i → p → e (end)

Insert "shine", "ship", "shirt", "shock":
Root → s → h → i → n → e (end)
Root → s → h → i → p (end)
Root → s → h → i → r → t (end)
Root → s → h → o → c → k (end)

Insert "gate", "gap", "game", "gain":
Root → g → a → t → e (end)
Root → g → a → p (end)
Root → g → a → m → e (end)
Root → g → a → i → n (end)
'''

class TrieNode:

    def __init__(self):
        self.children = {}
        self.is_end_of_word = False


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def add_word(self, word):

        current_node = self.root

        for character in word:
            if character not in current_node.children:
                current_node.children[character] = TrieNode()
            current_node = current_node.children[character]
        current_node.is_end_of_word = True

    def search_word(self, word):
      
        current_node = self.root
        
        for character in word:
          if character not in current_node.children:
            return False
          current_node = current_node.children[character]
        if current_node.is_end_of_word:
          return True
        return False

    def remove_word(self, word):
      
      stack = [] # need to apply LIFO/FILO
      
      if not self.search_word(word):
          return "Word not available, try again"

      current_node = self.root

      for character in word:
        stack.append(current_node)
        current_node = current_node.children[character]
      current_node.is_end_of_word = False

      length = len(stack) - 1
      while(length > 0):
        removeNode = stack.pop()
        char = word[length]
        
        if not removeNode.children[char].is_end_of_word and removeNode.children[char].children:
          del current_node.children[char]
          length -= 1
        else:
          break
      print("Word Removed")

trie = Trie()
trie.add_word("INTRUDER")
trie.add_word("RANJITH")
print(trie.search_word("INTRUDER")) # True
print(trie.search_word("RANJ")) # False
print(trie.remove_word("RANJITH")) # Word Removed
print(trie.remove_word("RANJITH")) # Word not available, try again