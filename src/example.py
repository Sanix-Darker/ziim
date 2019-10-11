import Zeus as Zeus
zeus = Zeus.Zeus(search_level = 1)

try:
    # Your code here
    test = "test"+12 # This will throws an error
except Exception as es:
    print(es)
    # Then call zeus here
    zeus.go(es)
    # That's all !
