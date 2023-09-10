class utils:
    def reversed(num):
        if isinstance(num, int):
            return int(str(num)[::-1])
        elif isinstance(num, str):
            return print("input str")
        elif isinstance(num, float):
            return print("input flt")
        else:
            return print("inv input")
        
    def formatter(num):
        if isinstance(num, int):
            return bin(num), oct(num)
        elif isinstance(num, str):
            return print("input str")
        elif isinstance(num, float):
            return print("input flt")
        else:
            return print("inv input")