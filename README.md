
# Zeus

Never open a Browser-tab again, copy/Paste your error/Exception to find available solutions online randomly!\
Zeus will handle everything for you, directly in the CLI after catching an error!\
**AMAZING RIGHT ?**

## How it's works

Theese are steps :

- Zeus get your error and ask you, where you want to find solution
- You just need to enter number corresponding the forum you want to fetch answers
- That's all, Zeus will provide you the available questions matching your error, give you the answers, votes,...

YOU GET IT ?\

No need to:

- `copy the Exception`,
- `Minimize your terminal`,
- `Open the browser`,
- `Paste it on google or any searchEngine`,
- `Open multiple tabs per result`,
- `fetching where the solution of your problem could be`...

## Available versions of Zeus

For now Zeus can be use on :

- *[Stable]* Python
- *[On going]* Javascript

## Handled Forums

For Now, Zeus can find on:

- *[Done]* StackOverflow
- *[Done]* StackExchange
- *[Done]* Codeproject
- *[Done]* CodeRanch
- *[Done]* SitePoint
- *[Not yet]* Codeguru
- *[Not yet]* ProgrammersHeaven
- *[Not yet]* Quora
- *[Not yet]* Designertalk
- *[Not yet]* Hashnode
- *[Not yet]* Codecall
- *[Not yet]* Reddit
- *[Not yet]* Hackr
- *[Not yet]* Webdeveloper

You will have the available list in `./list.json`

## How to use it

Let's see some examples on how to use it :

### In Python:

Make sure you have installed all requirements in ./python/requirements.txt, by running :
```shell
cd ZeusPYTHON
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
cd ZeusPYTHON
python example.py
```

### In JS:

Make sure you have installed all requirements in ./python/requirements.txt, by running :
```shell
cd ZeusJS
yarn install
# or npm install
```

```javascript
import Zeus from './Zeus';
// We instantiate Zeus
let Zeus = new Zeus(1);

try{
    // Put your source code herer
    const test = "Exemple"+24 // Let's generate our error here
}catch(err){
    console.log(err)
    // Now call Zeus
    Zeus.go(err)
    // That's all
}
```

Run in the cli :
```shell
cd ZeusJS
node example.js
```

## DEMO

<img src="./images/demo.gif" />

## Author

- [Sanix-darker](https://github.com/sanix-darker)