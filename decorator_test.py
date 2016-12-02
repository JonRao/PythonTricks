'''
#!/usr/bin/python
Using env in the shebang of a script

Python scripts are not different from scripts in any other language on this.

Either the usage of #!/usr/bin/env python or #!/usr/bin/python plays a role if the script is executable, and called without the preceding language. The script then calls the language's interpreter to run the code inside the script, and the shebang is the "guide" to find, in your example, python.

Using #!/usr/bin/env python instead of the absolute (full path) #!/usr/bin/python makes sure python (or any other language's interpreter) is found, in case it might not be in exactly the same location across different Linux- or Unix -like distributions, as explained e.g. here.

Although #!/usr/bin/python will work on a default Ubuntu system, it is therefore good practice to use  #!/usr/bin/env python instead.

About env

env is an executable in /usr/bin, or, as mentioned by @hvd (thanks for the hint!), available as a compatibility symlink in /usr/bin to env, in pretty much all Linux distributions.
'''

def handle_exceptions(print_msg_flag):
    def inner_handle_exceptions(func):
        def inner(*args, **kargs):
            #  The single asterisk form (*args) is used to pass a non-keyworded, variable-length argument list, and the double asterisk form is used to pass a keyworded, variable-length argument list.
            try:
                return func(*args, **kargs)
            except Exception as ex:
                if print_msg_flag:
                    print "An exception was thrown: ", ex
                return 'n/a'
        return inner
    return inner_handle_exceptions

@handle_exceptions(True)
#inner_handle = handle_exceptions(False)(divide)
#divide = inner_handle()
def divide(x,y):
    return x/y

print divide(8,0)



