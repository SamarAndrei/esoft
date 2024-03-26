str = input()

def check(str):
    list = []
    for char in str:
        if char in '([{':
            list.append(char)
        elif char == ")" and (not list or list[-1] != "("):
            return False
        elif char == "]" and (not list or list[-1] != "["):
            return False
        elif char == "}" and (not list or list[-1] != "{"):
            return False
        elif char == ")" and list[-1] == "(":
            list.pop(-1)
        elif char == "]" and list[-1] == "[":
            list.pop(-1)
        elif char == "}" and list[-1] == "{":
            list.pop(-1)

    if list==[]:
        return True
    else:
        return False
print(check(str))
