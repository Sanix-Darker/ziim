<img src="./images/logo.png" width="100" align="center" />

# Ziim

Never open a Browser-tab again, copy/Paste your error/Exception to find available solutions online randomly!\
Ziim will handle everything for you, directly in the CLI after catching an error!\
**AMAZING RIGHT ?**

## DEMO

<img src="./images/demo.gif" />

## How it's works

Theese are steps :

- Ziim get your error and ask you, where you want to find solution
- You just need to enter number corresponding the forum you want to fetch answers
- That's all, Ziim will provide you the available questions matching your error, give you the answers, votes,...

YOU GET IT ?\

No need to:

- `copy the Exception`,
- `Minimize your terminal`,
- `Open the browser`,
- `Paste it on google or any searchEngine`,
- `Open multiple tabs per result`,
- `fetching where the solution of your problem could be`...

## Handled Forums

For Now, Ziim can find on:

- *[Done]* StackOverflow
- *[Done]* StackExchange
- *[Done]* Codeproject
- *[Done]* CodeRanch
- *[Done]* SitePoint
- *[Done]* Quora
- *[Done]* Reddit
- *[Not yet]* Hackr
- *[Not yet]* Webdeveloper

You will have the available list in `./src/list_json.py`

## Requirements

- Python (3.x is recommended)
- requests
- lxml


## How to use it

Let's see some examples on how to use it :

### In your code

Make sure you have installed all requirements in ./python/requirements.txt, by running :
```shell
pip install -r requirements.txt
```

In the code :

```python
# You import first Ziim Class and instantiate it
import Ziim as Ziim
ziim = Ziim.Ziim() # search_level is not required and as default it's 0

try:
    # Your code here
    test = 12/0 # This will throws an error
except Exception as es:
    # Then call ziim here
    ziim.go(es)
    # That's all !
```

Run in the cli :
```shell
cd ./test
python example.py
```

## As a CLI

Just hit this sample command : 
```shell
python ./cli/ziimcli.py node ./example.js
# or add an alias:
alias ziimcli = "python absolute/path/to/cli/ziimcli.py"

# Then hit:
ziimcli node ./example.js
```

The command `node ./example.js` will be executed and the error will be taken to ziim, with this method you can start any kind of process in CLI and use ziimcli to fetch solutions.

## ZiimCLI DEMO

<img src="./images/ziimcli.gif" />

## Author

- [Sanix-darker](https://github.com/sanix-darker)