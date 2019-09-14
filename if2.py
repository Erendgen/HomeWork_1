def test(str1, str2):        
    if isinstance(str1, str) and isinstance(str2, str):
        if str1 == str2:
            return 1
        elif str1 != str2 and len(str1) > len(str2):
            return 2
        elif str1 != str2 and str2 == 'learn':
            return 3
        else:
            return '"В задаче не описано что возвращать"'
    else:
        return 0
def main():
    print(test('QWE','QWE'))
    print(test('QWE34','QWE'))
    print(test('QWE34','learn'))
    print(test(1,'asdasd'))
    print(test('zxc','asdasdasda'))

if __name__ == "__main__":    
    main()