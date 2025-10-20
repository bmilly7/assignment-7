class DoctorNode:
    def __init__(self,name):
        self.name = name
        self.left = None
        self.right = None
   



class DoctorTree:
    def __init__(self):
        self.root = None

    
    def insert(self, parent_name: str, employee_name: str, side: str, current_node=None) -> bool:
        
        if self.root is None: 
            print("tree is empty")
            return

        if current_node is None:
            current_node = self.root

        if current_node.name == parent_name:
            #add on left
            if side == 'left' and current_node.left is None: 
                current_node.left = DoctorNode(employee_name)
                print(f"added {employee_name} under {parent_name} on the left")
                return True
            #add on right
            elif side == 'right' and current_node.right is None:
                current_node.right = DoctorNode(employee_name)
                print(f"{employee_name} added under {parent_name} to the right")
                return True
            else: 
                print(f"{parent_name} already has a {side} sub unit")
                return True
            

        found_left = False
        found_right = False

        if current_node.left:
            found_left = self.insert(parent_name, employee_name, side, current_node.left)
            if found_left:
                return True

        if current_node.right and not found_left:
            found_right = self.insert(parent_name, employee_name, side, current_node.right)
            if found_right:
                return True
        if not (found_left or found_right):
            if current_node == self.root:
                print(f"{parent_name} not found in tree")
            return False


    def preorder_traversal(self, node):

        if node is None:
            return []
        result = [node.name]
        result += self.preorder_traversal(node.left)
        result += self.preorder_traversal(node.right)
        return result

    def inorder_traversal(self,node):
        if node is None:
            return []
        result = []
        result += self.inorder_traversal(node.left)
        result.append(node.name)
        result += self.inorder_traversal(node.right)
        return result

        

    def postorder_traversal(self,node):
        if node is None:
            return []
        result = []
        result += self.postorder_traversal(node.left)
        result += self.postorder_traversal(node.right)
        result.append(node.name)
        return result





        





        







# Test your DoctorTree and DoctorNode classes here
tree = DoctorTree()
tree.root = DoctorNode("Dr. Smith")
tree.insert("Dr. Smith", "Dr. Adams", "left")
tree.insert("Dr. Smith", "Dr. Clark", "right")
tree.insert("Dr. Adams", "Dr. Lee", "left")

print("Preorder:", tree.preorder_traversal(tree.root))
print("Inorder:", tree.inorder_traversal(tree.root))
print("Postorder:", tree.postorder_traversal(tree.root))
