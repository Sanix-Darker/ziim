# Zeus-python

## How to use it

Let's see some examples on how to use it :

- In Python:

Make sure you have installed all requirements in ./python/requirements.txt, by running :
```shell
pip install -r requirements.txt
```

```python
# You import first Zeus Class
import Zeus as Zeus
# You instantiate
zeus = Zeus.Zeus(search_level = 10) # search_level is not required and as default it's 0

try:
    # Your code here
    test = 12/0 # This will throws an error
except Exception as es:
    # Then call zeus here
    zeus.go(es)
    # That's all !
```

Run in the cli :
```shell
python example.py
```

## Author

- [Sanix-darker]("https://github.com/sanix-darker")