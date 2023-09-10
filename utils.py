class utils:
    
    def reversed(num):
        if isinstance(num, int):
            tmp = str(num)[::-1]
            if(str(num)[0] == "-"):
                tmp = "-" + str(num)[:0:-1]
                return int(tmp)
            else:
                return int(str(num)[::-1])
        elif isinstance(num, str):
            return None
        elif isinstance(num, float):
            return None
        else:
            return None
        
    def formatter(num):
        if isinstance(num, int):
            return bin(num), oct(num)
        elif isinstance(num, str):
            return None
        elif isinstance(num, float):
            return None
        else:
            return None