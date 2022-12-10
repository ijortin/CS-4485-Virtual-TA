class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 1
 
# AVL tree class which supports the
# Insert operation
class AVL_Tree(object):
    def __init__(self):
        self._data = []
        
    # Recursive function to insert key in
    # subtree rooted with node and returns
    # new root of subtree.
    def insert(self, root, key):
     
        # Step 1 - Perform normal BST
        if not root:
            return TreeNode(key)
        elif key < root.val:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)
 
        # Step 2 - Update the height of the
        # ancestor node
        root.height = 1 + max(self.getHeight(root.left),
                           self.getHeight(root.right))
 
        # Step 3 - Get the balance factor
        balance = self.getBalance(root)
 
        # Step 4 - If the node is unbalanced,
        # then try out the 4 cases
        # Case 1 - Left Left
        if balance > 1 and key < root.left.val:
            return self.rightRotate(root)
 
        # Case 2 - Right Right
        if balance < -1 and key > root.right.val:
            return self.leftRotate(root)
 
        # Case 3 - Left Right
        if balance > 1 and key > root.left.val:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)
 
        # Case 4 - Right Left
        if balance < -1 and key < root.right.val:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)
 
        return root
 
    def leftRotate(self, z):
 
        y = z.right
        T2 = y.left
 
        # Perform rotation
        y.left = z
        z.right = T2
 
        # Update heights
        z.height = 1 + max(self.getHeight(z.left),
                         self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),
                         self.getHeight(y.right))
 
        # Return the new root
        return y
 
    def rightRotate(self, z):
 
        y = z.left
        T3 = y.right
 
        # Perform rotation
        y.right = z
        z.left = T3
 
        # Update heights
        z.height = 1 + max(self.getHeight(z.left),
                        self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),
                        self.getHeight(y.right))
 
        # Return the new root
        return y
 
    def getHeight(self, root):
        if not root:
            return 0
 
        return root.height
 
    def getBalance(self, root):
        if not root:
            return 0
 
        return self.getHeight(root.left) - self.getHeight(root.right)
 
    def preOrder(self, root):
 
        if not root:
            return
 
        self._data.append(root.val)
        self.preOrder(root.left)
        self.preOrder(root.right)

class patricia():
    def __init__(self):
        self._data = {}

    def addWord(self, word):
        data = self._data
        i = 0
        while 1:
            try:
                node = data[word[i:i+1]]
            except KeyError:
                if data:
                    data[word[i:i+1]] = [word[i+1:],{}]
                else:
                    if word[i:i+1] == '':
                        return
                    else:
                        if i != 0:
                            data[''] = ['',{}]
                        data[word[i:i+1]] = [word[i+1:],{}]
                return

            i += 1
            if word.startswith(node[0],i):
                if len(word[i:]) == len(node[0]):
                    if node[1]:
                        try:
                            node[1]['']
                        except KeyError:
                            data = node[1]
                            data[''] = ['',{}]
                    return
                else:
                    i += len(node[0])
                    data = node[1]
            else:
                ii = i
                j = 0
                while ii != len(word) and j != len(node[0]) and \
                      word[ii:ii+1] == node[0][j:j+1]:
                    ii += 1
                    j += 1
                tmpdata = {}
                tmpdata[node[0][j:j+1]] = [node[0][j+1:],node[1]]
                tmpdata[word[ii:ii+1]] = [word[ii+1:],{}]
                data[word[i-1:i]] = [node[0][:j],tmpdata]
                return

    def isWord(self,word):
        data = self._data
        i = 0
        while 1:
            try:
                node = data[word[i:i+1]]
            except KeyError:
                return False
            i += 1
            if word.startswith(node[0],i):
                if len(word[i:]) == len(node[0]):
                    if node[1]:
                        try:
                            node[1]['']
                        except KeyError:
                            return False
                    return True
                else:
                    i += len(node[0])
                    data = node[1]
            else:
                return False

    def isPrefix(self,word):
        data = self._data
        i = 0
        wordlen = len(word)
        while 1:
            try:
                node = data[word[i:i+1]]
            except KeyError:
                return False
            i += 1
            if word.startswith(node[0][:wordlen-i],i):
                if wordlen - i > len(node[0]):
                    i += len(node[0])
                    data = node[1]
                else:
                    return True
            else:
                return False

    def removeWord(self,word):
        data = self._data
        i = 0
        while 1:
            try:
                node = data[word[i:i+1]]
            except KeyError:
                return "Word is not in trie."

            i += 1
            if word.startswith(node[0],i):
                if len(word[i:]) == len(node[0]):
                    if node[1]:
                        try:
                            node[1]['']
                            node[1].pop('')
                        except KeyError:
                            return "Word is not in trie."
                        return
                    data.pop(word[i-1:i])
                    return
                else:
                    i += len(node[0])
                    data = node[1]
            else:
                return "Word is not in trie."
            
def matching_prefix_index(word1, word2):
    max_len = min(len(word1),len(word2))
    for i in range(max_len):
        if word2[i] != word1[i]:
            return i
    return max_len

class PatriciaTrie():
    def __init__(self):
        self._storage = {}
        self._complete_prefix_flag = False

    def _find_storage_key(self, word):
        for key in self._storage:
            prefix_index = matching_prefix_index(key, word)
            if prefix_index > 0:
                return (key, prefix_index)
        return (None, None)

    def add(self, word):
        if word == '':
            self._complete_prefix_flag = True
            return True

        key, prefix_index = self._find_storage_key(word)
        if key is not None:
            if prefix_index == len(key):
                return self._storage[key].add(word[len(key):])
            else:
                new_tree = PatriciaTrie()
                new_tree._storage[key[prefix_index:]] = self._storage.pop(key)
                self._storage[key[0:prefix_index]] = new_tree
                return new_tree.add(word[prefix_index:])
        else:
            self._storage[word] = PatriciaTrie()
            self._storage[word].add('')
            return True

    def remove(self, word):
        if word == '':
            self._complete_prefix_flag = False
            return True

        key, prefix_index = self._find_storage_key(word)
        if key is None or prefix_index != len(key):
            return False

        subword = word[prefix_index:]
        subtrie = self._storage[key]
        if subtrie.remove(subword):
            if (not subtrie._complete_prefix_flag) and len(subtrie._storage) == 0:
                self._storage.pop(key)
            return True
        else:
            return False

    def __contains__(self, word):
        if word == '':
            return self._complete_prefix_flag

        key, prefix_index = self._find_storage_key(word)
        if key is None or prefix_index != len(key):
            return False
        else:
            return (word[prefix_index:] in self._storage[key])

    def has_prefix(self, word):
        if word == '':
            return True

        key, prefix_index = self._find_storage_key(word)
        if key is None:
            return False
        elif len(key) > len(word):
            return (prefix_index == len(word))
        elif len(key) != prefix_index:
            return False
        else:
            return self._storage[key].has_prefix(word[prefix_index:])