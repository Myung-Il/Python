def po(s):
    s = s**2
    return s

a = int(input())
print(eval(f"po({a})"))



tp = input()
exec(f"""

a = {tp}
a = a**2
print(a)

""")
