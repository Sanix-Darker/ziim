import Zeus as Zeus

z = Zeus.Zeus()

try:
    print("Example")
    test = 1200/0
except Exception as es:
    print(es)
    z.go(es)