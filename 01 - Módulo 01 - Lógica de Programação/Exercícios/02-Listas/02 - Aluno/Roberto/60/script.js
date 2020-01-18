console.log("[-- INÍCIO --]");
console.log("\n");

var n
q = 0
i = 0

for (var contador=1; contador<=10; contador++){
    n = Number(window.prompt("Qual o valor do número? "))
if ((n>=10) && (n<=20)){
    q = q + 1
}
else {
    i = i + 1
} 
  
}    
console.log("A quantidade de valores entre 10 e 20 foi/foram " + q);
console.log("A quantidade de valores fora do intervalo entre 10 e 20 foi/foram " + i);


console.log("\n");
console.log("[-- FIM --]");