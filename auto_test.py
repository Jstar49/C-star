import subprocess
import random
import re
from tqdm import trange

test_time = 100
success_count = 0
err_seed_list = []
for i in trange(test_time):
  seed = i
  p = subprocess.Popen(f"python run.py --seed {seed}",shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
  py_output = str(p.stdout.read())
  py_result = re.search(r"result is (.*)\\n", py_output)
  if py_result==None:
    err_seed_list.append(seed)
    continue
  py_result = py_result.group(1)
  
  p = subprocess.Popen(f"gcc main.c -o a.out&& ./a.out",shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
  c_output = str(p.stdout.read())
  c_result = re.search(r"RESULT : (.*)\\n", c_output)
  if c_result==None:
    err_seed_list.append(seed)
    continue
  c_result = c_result.group(1)
  # print(f"case {seed}")
  # print(py_result)
  # print(c_result)
  if py_result!=c_result:
    err_seed_list.append(seed)
    continue
  
  success_count+=1
  
print("error_rate= ",(1-(success_count/test_time))*100,"%")
print("error_seeds:",err_seed_list) if len(err_seed_list)!=0 else print("win win all test case pass!")

  