'''
Author: joessem jxxclj@gmail.com
Date: 2022-11-27 23:10:15
LastEditors: joessem jxxclj@gmail.com
LastEditTime: 2022-12-04 00:33:45
FilePath: \C-star\code_statements.py
Description: 
    Generate C statements

Copyright (c) 2022 by joessem jxxclj@gmail.com, All Rights Reserved. 
'''
import random
from pkg import MathematicalTypes, AssignementTypes, StatementsTypes
from CType import CVal

# binary tree  class
class ArithmeticsTree:
    def __init__(self) -> None:
        self.left = None
        self.right = None
        self.value = None
        # is leaf node ?
        self.is_leaf = False
        self.level = 0
        # real_node_cvalue,include value and type
        self.c_value = None
        
        self.zero_flag = False

# 
class RandomArithmetics:
    def __init__(self, left_var = None, right_var = None) -> None:
        # type of arithmetic, such as +,-,*,/
        self.arithmetic_type = None
        # need left var, and right var
        tmp = random.randint(0, 1)
        self.left_var = left_var if tmp == 0 else right_var
        self.right_var = right_var if tmp == 0 else left_var
    
    # get random Arithmetic
    def Gen_Arithmetic(self):
        self.arithmetic_type = random.choice(list(MathematicalTypes))
        # print(self.arithmetic_type, self.arithmetic_type.value)


# Generate assignements, need a parents var
class Assignement:
    def __init__(self, parents_var = None) -> None:
        # AssignementType
        self.assignement_type = None
        # need a parents var
        self.parents_var = parents_var
        # 赋值语句的右边，可以是计算，也可以是简单的赋值，或者是一个函数调用
        # 或者函数指针
        self.children = None
        self.children_type = None
        # statements C code
        self.state_c_code = ""
        self.state_c_code += self.parents_var.var_name + " "
        self.var_can_used = []
        
    
    # gen right
    def Gen_Assigned_And_children(self, var_can_used=[]):
        self.var_can_used = var_can_used
        self.assignement_type = random.choice(list(AssignementTypes))
        self.state_c_code += self.assignement_type.value + " "
        # gen random arithmetics
        self.Gen_RandomArithmetics()
        
        self.parents_var.val = self.root_node.c_value.ToValValue(self.parents_var.type_name)
        if self.parents_var.val==0:
          self.parents_var.val+=1
          self.state_c_code = self.state_c_code[:-1]+"+1;"
        
        if self.parents_var.var_name=="result":
          print(self.parents_var.var_name,"is")
          print(hex(self.parents_var.val))
    
    # gen random arithmetics
    def Gen_RandomArithmetics(self):
        self.root_node = ArithmeticsTree()
        self.root_node.value = random.choice(list(MathematicalTypes))
        self.Gen_RandomTree_By_Level(self.root_node, 5, 0)
        # inorder traversal to get a arithmetics statement
        self.Inorder_ArithmeticsTree(self.root_node)
        self.state_c_code += ";"
        # print(self.state_c_code)
        

    # Gen a binary tree, max level < max_level
    def Gen_RandomTree_By_Level(self, node, max_level, level):
        if node.is_leaf:
            node.value = random.choice(self.var_can_used)
            node.c_value = CVal(node.value)
            return
        # left node
        node.left = ArithmeticsTree()
        node.left.deep = level + 1
        node.left.value = random.choice(list(MathematicalTypes))
        node.right = ArithmeticsTree()
        # right node
        node.right.deep = level + 1
        node.right.value = random.choice(list(MathematicalTypes))
        # 33% chance to set next level is leaf
        random_leaf = random.randint(0,2)
        if level >= max_level or random_leaf == 1:
            node.left.is_leaf = True
            node.right.is_leaf = True
        self.Gen_RandomTree_By_Level(node.left, max_level, level + 1)
        self.Gen_RandomTree_By_Level(node.right, max_level, level + 1)
        
        # 对左右两端c_value进行计算
        if node.value==MathematicalTypes.DIV or node.value==MathematicalTypes.REM:
          if node.right.c_value.DetectZero():
            node.zero_flag = True
            node.right.c_value = node.right.c_value.NewAddOneCVal()
        node.c_value = node.left.c_value.Cal(node.right.c_value,node.value)
        

    def Inorder_ArithmeticsTree(self, node):
        if node.is_leaf:
            self.state_c_code += node.value.var_name
            return
        self.state_c_code += "("
        self.Inorder_ArithmeticsTree(node.left)
        self.state_c_code += node.value.value
        if node.zero_flag:
          self.state_c_code += "("
        self.Inorder_ArithmeticsTree(node.right)
        if node.zero_flag:
          self.state_c_code += "+1)"
        self.state_c_code += ")"
    
    # assignement statement to C code
    def Gen_Assignement_C_Code(self):
        self.state_c_code += self.parents_var.var_name
        self.state_c_code += " " + self.assignement_type.value

        self.state_c_code += " " + self.children.left_var.var_name
        self.state_c_code += " " + self.children.arithmetic_type.value
        self.state_c_code += " " + self.children.right_var.var_name
        self.state_c_code += ";"
        
# 生成 C 语句
class Statements:
    def __init__(self) -> None:
        # statements type, such as signed, if, while
        self.statement_type = None
        self.state = None
        # var has used in this statement
        self.var_used = []
        # the variables that can be used
        self.var_can_use = []
        self.c_code = ""
        
    # gen statements
    def Gen_Statements(self):
        self.Gen_Assignement()

    def Gen_Assignement(self):
        self.statement_type = StatementsTypes.Assignement
        self.state = Assignement(parents_var=random.choice(self.var_can_use))
        print("====== Gen_Assignement self.state.parents_var", self.state.parents_var)
        self.state.Gen_Assigned_And_children(self.var_can_use)
        self.c_code = self.state.state_c_code