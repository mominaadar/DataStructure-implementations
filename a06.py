class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    # add rest of Tree Node functions here
    def dfs(self, co):
     
        if self.left:
            co.process(self.left)
            self.left.dfs(co)
        
        if self.right:
            co.process(self.right)
            self.right.dfs(co)


    def dfs_inorder(self):
        if self.left:
            self.left.dfs_inorder()

        print(self.val)

        if self.right:
            self.right.dfs_inorder()


    def dfs_postorder(self):
        if self.left:
            self.left.dfs_postorder()

        if self.right:
            self.right.dfs_postorder()

        print(self.val)


    def bfs(self):
        lst = [self]

        while lst:
            current = lst.pop(0)

            print(current.val)

            if current.left:
                lst.append(current.left)

            if current.right:
                lst.append(current.right)


    def dfs_apply(self,fn):
        fn(self)

        if self.left:
            self.left.dfs_apply(fn)

        if self.right:
            self.right.dfs_apply(fn)

class Person:
    def __init__(self,name):
        self.name = name

    def __str__(self):
        return self.name

class Collector:
    def __init__(self):
        self.lst = []
    
    def process(self,node):
        self.lst.append(str(node.val))
    
    def get_list(self):
        return self.lst
    
    def reset_list(self):
        self.lst = []


# Add the find_val function here ##########
def find_val(self, val):
    if str(self.val) == val:
        return self

    if self.left:
        var = self.left.find_val(val)
        
        if var is not None and str(var.val) == val:
            return var

    if self.right:
        var = self.right.find_val(val)
        
        if var is not None and str(var.val) == val:
            return var

    if str(self.val) != val:
        return None

# End of find_val function  ################
TreeNode.find_val = find_val


# Add the find_people_in_hierarchy function here ##########
def find_people_in_hierarchy(self, name):
    if str(self.val) == 'Director':
        coll = Collector()
        coll.process(self)
        self.dfs(coll)

        if name not in coll.get_list():
            raise ValueError('Expecting a ValueError when node is not found.')
    
    if str(self.val) == name:
        col = Collector()
        col.process(self)
        self.dfs(col)
        
        return col.get_list()
        
    else:
        
        if self.left:
            var = self.left.find_people_in_hierarchy(name)
            if var is not None:
                return var

        if self.right:
            var = self.right.find_people_in_hierarchy(name)
            if var is not None:
                return var

TreeNode.find_people_in_hierarchy = find_people_in_hierarchy
# End of find_people_in_hierarchy function  ################


if __name__ == "__main__":
    pass


    # Section 1: creating people
    print("Section 1: ")
    director = Person("Director")
    hod_1 = Person("HoD 1")
    hod_2 = Person("HoD 2")
    faculty_cs_1 = Person("CS 1")
    faculty_cs_2 = Person("CS 2")
    faculty_ee_1 = Person("EE 1")
    faculty_ee_2 = Person("EE 2")
    print(director) # should print: Director

    # Section 2: inserting people in the tree
    print("\nSection 2: ")
    t_d = TreeNode(director)
    t_d.left = TreeNode(hod_1)
    t_d.right = TreeNode(hod_2)

    t_d.left.left = TreeNode(faculty_cs_1)
    t_d.left.right = TreeNode(faculty_cs_2)

    t_d.right.left = TreeNode(faculty_ee_1)
    t_d.right.right = TreeNode(faculty_ee_2)
    t_d.dfs()


    # Section 3: try find_val individually
    print("\nSection 3: ")

    node = t_d.find_val("Director")
    print(node.val)  # should print the string: Director

    node = t_d.find_val("HoD 1")
    print(node.val)  # should print the string: HoD 1

    node = t_d.find_val("HoD 2")
    print(node.val)  # should print the string: HoD 2

    node = t_d.find_val("HoD 3")
    print(node)  # should print the string: None


    # Section 4: try the collector
    print("\nSection 4: ")
    c = Collector()
    t_d.dfs_apply(c.process)
    print(c.get_list()) # should print the list: ['Director', 'HoD 1', 'CS 1', 'CS 2', 'HoD 2', 'EE 1', 'EE 2']


    # Section 5: find hierarchy
    print("\nSection 5: ")
    people = t_d.find_people_in_hierarchy("HoD 1")
    print(people)    # Should print the list: ['HoD 1', 'CS 1', 'CS 2']
