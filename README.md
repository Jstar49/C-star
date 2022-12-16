# C-star
Generate C source code, by python.

# Install

> \> git clone https://github.com/Jstar49/C-star.git  
> \> cd C-star  
> \> pip install -r requirements.txt  
> \> python3 ./setup.py  

# How to use 

It will generate a C file, default filename is main.c. You can use argment `--o` to change the out filename. Such as:  
> \> python run.py --o test.c  

You can use set argment `--complexity=<n>` to control program size and complexity, it default 1, max is 100.

# Check outfile

> \> gcc main.c  
> \> ./a.out  
> RESULT : 7F9F8E97  