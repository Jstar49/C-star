import random
import pdb

from Types import *
from pkg import *
from base_op_func import base_op_c
# from CType import CVal

# Function called class
class Function_Called_Class:
    def __init__(self) -> None:
        self.func = None
        self.func_name = None
        self.func_args = []

        self.func_called_code = ""
    
    def Build_func_called(self, func_avail, var_avail):
        var_table = {}
        for i in range(len(var_avail)):
            if var_avail[i].type_name not in var_table:
                var_table[var_avail[i].type_name] = []
            var_table[var_avail[i].type_name].append(var_avail[i])
        # print(var_table, func_avail)
        # TODO: 取出一个随机的可用函数，要求有满足函数所需的所有参数类型的变量
        # print(func_avail)
        if len(func_avail) < 1:
            return False
        
        while len(func_avail):
            self.func_args = []
            func = random.choice(func_avail)
            # pdb.set_trace()
            self.func = func
            self.func_name = func.function_name
            can_use = True
            for par in func.function_args:
                if par.type_name in var_table:
                    self.func_args.append(random.choice(var_table[par.type_name]))
                else:
                    can_use = False
                    self.func_args = []
            func_avail.remove(func)
            if can_use:
                # print(f"{len(func.function_args)}")
                # print(f"函数调用 {self.func_name} 参数个数{len(self.func_args)}")
                break
        return can_use
    
    def Build_func_code(self):
        self.func_called_code = f"{self.func_name}("
        arg_ = []
        for par in self.func_args:
            arg_.append(par.var_name)
        self.func_called_code += f"{', '.join(arg_)})"

# binary tree  class
class ArithmeticsTree:
    def __init__(self) -> None:
        self.left = None
        self.right = None
        self.value = None
        self.type = None
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
        self.var_can_used = []
        # 可引用的函数
        self.func_can_called = []
    
    # gen right
    def Gen_Assigned_And_children(self, var_can_used=[]):
        self.var_can_used = var_can_used
        self.assignement_type = random.choice(list(AssignementTypes))
        
        # gen random arithmetics
        self.Gen_RandomArithmetics()
    
    # gen random arithmetics
    def Gen_RandomArithmetics(self):
        self.root_node = ArithmeticsTree()
        self.root_node.value = random.choice(list(MathematicalTypes))
        treeDeep = 5
        max_deep = random.randint(0, 5)
        if max_deep == 0:
            self.root_node.is_leaf = True
        # TODO : set treeDeep relate to complexity
        self.Gen_RandomTree_By_Level(self.root_node, 5, 0)
        # inorder traversal to get a arithmetics statement
        tmp = []
        # self.Inorder_ArithmeticsTree(self.root_node, tmp)
        # print("Gen_RandomArithmetics c_state", "".join(tmp))
        
        self.state_c_code += self.parents_var.var_name + " "
        self.state_c_code += self.assignement_type.value + " "
        if max_deep > 0:
            root_arith_func = f"_func_{base_op_c.base_ops[self.root_node.value]}_"
            root_arith_func += f"{self.parents_var.type_name.value}_"
            base_op_c.Mark_func_used(root_arith_func)
            # print(root_arith_func)
            self.state_c_code += root_arith_func
            self.state_c_code += "("
        else:
            node_codes = []
            self.Inorder_ArithmeticsTree(self.root_node, node_codes)
            self.state_c_code += "".join(node_codes)

        # left node
        if self.root_node.left:
            left_nodes = []
            self.Inorder_ArithmeticsTree(self.root_node.left, left_nodes)
            self.state_c_code += "".join(left_nodes) + ", "

        # right node
        if self.root_node.right:
            right_nodes = []
            self.Inorder_ArithmeticsTree(self.root_node.right, right_nodes)
            self.state_c_code += "".join(right_nodes) + ")"

        self.state_c_code += ";"
        # print("self.state_c_code", self.state_c_code)
        # print(self.state_c_code)
        

    # Gen a binary tree, max level < max_level
    def Gen_RandomTree_By_Level(self, node, max_level, level):
        if node.is_leaf:
            # choice in variable, constant, function call, 
            method_allowd = 1
            if args.complexity>2:
                method_allowd = 2
            method_allowd = [i for i in range(method_allowd+1)]
            while 1:
                i = random.choice(method_allowd)
                # i == 0, set variable
                if i == 0:
                    node.value = random.choice(self.var_can_used)
                    # node.c_value = CVal(node.value)
                    node.type = "variable"
                # i == 1, set constant
                elif i == 1:
                    tmp = Constant_t()
                    tmp.random_const()
                    node.value = tmp
                    node.type = "constant"
                # i == 2, function called
                elif i == 2:
                    node.type = "func_called"
                    tmp = Function_Called_Class()
                    if not tmp.Build_func_called(self.func_can_called, self.var_can_used):
                        method_allowd.remove(i)
                        continue
                    node.value = tmp
                return
        # left node
        node.left = ArithmeticsTree()
        node.left.deep = level + 1
        node.left.value = random.choice(list(MathematicalTypes))
        
        # right node
        node.right = ArithmeticsTree()
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
        # if node.value==MathematicalTypes.DIV or node.value==MathematicalTypes.REM:
        #   if node.right.c_value.DetectZero():
        #     node.zero_flag = True
        #     node.right.c_value = node.right.c_value.NewAddOneCVal()
        # node.c_value = node.left.c_value.Cal(node.right.c_value,node.value)
        

    def Inorder_ArithmeticsTree(self, node, c_state):
        
        if node.is_leaf:
            if node.type == "variable":
                c_state.append(node.value.var_name)
            elif node.type == "constant":
                tmp = ""
                if node.value.value < 0:
                    tmp = f"({str(node.value.value)})"
                else:
                    tmp = f"{str(node.value.value)}"
                c_state.append(tmp)
            elif node.type == "func_called":
                node.value.Build_func_code()
                tmp = f"{node.value.func_called_code}"
                c_state.append(tmp)
            return

        # print()
        arith_func_name = f"_func_{base_op_c.base_ops[node.value]}_"
        arith_func_name += random.choice(list(VarTypes)).value + "_"
        base_op_c.Mark_func_used(arith_func_name)
        # print(node.value, arith_func_name)
        c_state.append(arith_func_name)
        c_state.append("(")

        self.Inorder_ArithmeticsTree(node.left, c_state)
        c_state.append(", ")
        # c_state.append(node.value.value)
        self.Inorder_ArithmeticsTree(node.right, c_state)
        c_state.append(")")
    
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
        # 可调用的函数
        self.func_can_called_stat = []
        self.c_code = ""
        
    # gen statements
    def Gen_Statements(self):
        self.Gen_Assignement()

    def Gen_Assignement(self):
        self.statement_type = StatementsTypes.Assignement
        self.state = Assignement(parents_var=random.choice(self.var_can_use))
        # print("====== Gen_Assignement self.state.parents_var", self.state.parents_var)
        # print(f"{__file__} line 238 {self.func_can_called_stat}")
        self.state.func_can_called = self.func_can_called_stat[:]
        self.state.Gen_Assigned_And_children(self.var_can_use)
        self.c_code = self.state.state_c_code