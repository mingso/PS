### 1. a~z 알파벳 dictionary 만드는 법
```python
atoz = "abcdefghijklmnopqrstuvwxyz"
alphabet = {}

for alpha in atoz:
    alphabet[alpha] = -1
```

### 2. test case 개수 안 주고 무한으로 나올 때 끝내는 법
```python
while True:
    sen = sys.stdin.readline()
    if sen == "":
        break
```
### 3. 문자열 for문 안돌고 빠르게 출력하는 법 (대신 메모리 낭비 있음)
```python
print("\n".join(map(str, li)))
```