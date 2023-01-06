import random
import pdb

from config import args
from code_statements import *
from code_blocks import  CodeBlock
from pkg import *
from Types import *

class FunctionClass:
    def __init__(self) -> None:
        self.function_name = None
        self.function_type = None
        self.function_blocks = []
        self.function_code = []
        self.var_can_used_function = []
        # 可用的函数调用
        self.function_can_called = []
        self.function_var_backup = []
        self.funtion_ret = None
        # function args
        self.function_arg_num = 0
        self.function_args = []
    
    def main(self):
        # function return type
        self.function_type = random.choice(list(VarTypes))
        tmp = self.function_type.value + " " + self.function_name + "("
        self.function_arg_num = random.randint(0,3)
        arg_ = []
        for i in range(self.function_arg_num):
            tmp_var = Get_Random_Type_Var()
            tmp_var.var_name = f'arg_{i}'
            self.function_args.append(tmp_var)
            # add var_can_used_function
            self.var_can_used_function.append(tmp_var)
            # choice add to function_var_backup list
            if random.randint(0, 1):
                self.function_var_backup.append(tmp_var)
            arg_.append(f"{tmp_var.type_name.value} {tmp_var.var_name}")
        
        self.function_code.append(tmp + ", ".join(arg_)+ ") {")
        
        # build a variable for rets
        rets_var = Get_Var_By_Type(self.function_type.value)
        rets_var.var_name = "ret"
        self.funtion_ret = rets_var
        tmp = f"{INDENT}{rets_var.type_name.value} {rets_var.var_name} = {rets_var.val};"
        self.function_code.append(tmp)
        self.var_can_used_function.append(rets_var)

        # generate code blocks
        self.block_num = random.randint(1,5)
        for i in range(self.block_num):
            self.Gen_code_block()
        # block => c code
        self.FunCode_Translation()
        self.Function_end_code()
        self.function_code.append("}")
    
    # build main function
    def Build_main_function(self):
        self.function_name = "main"
        self.function_type = VarTypes.INT32
        tmp = self.function_type.value + " " + self.function_name + "() {"
        self.function_code.append(tmp)
        self.min_block = (args.complexity) * 5
        self.max_block = (args.complexity + 1) * 5
        self.block_num = random.randint(self.min_block, self.max_block)
        for i in range(self.block_num):
            self.Gen_code_block()
        # block => c code
        self.FunCode_Translation()
        # print result
        self.Function_end_code()
        self.function_code.append("}")
    
    # generate code block
    def Gen_code_block(self):
        block = CodeBlock(block_id=Get_BLOCKID())
        block.Generate_Code_Blocks_var()
        block.var_can_used_block += self.var_can_used_function
        self.var_can_used_function += block.block_new_var_list
        block.func_can_called_block = self.function_can_called[:]
        block.Gen_Block_statements()
        block.Generate_C_Source_CodeBlock()
        self.function_blocks.append(block)
        # if self.function_name == "main":
        self.function_var_backup.append(random.choice(block.block_new_var_list))

    # function ending code, return or printf
    def Function_end_code(self):
        tmp_c = Assignement(parents_var=self.funtion_ret)
        tmp_c.Gen_Assigned_And_children(self.function_var_backup)
        self.function_code.append(INDENT + tmp_c.state_c_code)
        if self.function_name == "main":
            tmp_c = f'''printf("RESULT : %lld\\n", result);'''
            self.function_code.append(INDENT + tmp_c)
        else:
            tmp_c = f'''return ret;'''
            self.function_code.append(INDENT + tmp_c)

    # generate c source code.
    def FunCode_Translation(self):
        # pdb.set_trace()
        for block in self.function_blocks:
            for j in range(len(block.block_code)):
                self.function_code.append(INDENT + block.block_code[j])
        

        # print function code
        # for item in self.function_code:
        #     print(item)

