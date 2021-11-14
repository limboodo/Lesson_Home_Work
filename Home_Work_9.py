a = {}
for text in input().split():
    if text in a:
        a[text] = a.get(text) + 1
        print(a.get(text))
    else:
        a[text] = 1
        print(a.get(text))
