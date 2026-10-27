import sys
def main():
    data = sys.stdin.read()
    n = len(data)
    
    t = 0  # 0=不在字符串中，1=在字符串中
    i = 0
    while i < n:
        if data[i] == '"':
            if i == 0 or data[i-1] != '\\':
                t = 1 - t  
            print(data[i], end='')
            i += 1
        elif t == 0 and data[i] == '/' and i + 1 < n and data[i+1] == '*':
            j = i + 2
            found = False
            while j < n - 1:
                if data[j] == '*' and data[j+1] == '/':
                    i = j + 1
                    found = True
                    break
                j += 1
            if not found:
                print(data[i], end='')
            i += 1
        else:
            print(data[i], end='')
            i += 1
if __name__ == "__main__":
    main()