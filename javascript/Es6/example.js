import Zeus from './Zeus';
// We instantiate Zeus
let Zeus = new Zeus(3);

try{
    // Put your source code herer
    const test = "Exemple"+24 // Let's generate our error here
}catch(err){
    console.log(err)
    // Now call Zeus
    Zeus.go(err)
    // That's all
}