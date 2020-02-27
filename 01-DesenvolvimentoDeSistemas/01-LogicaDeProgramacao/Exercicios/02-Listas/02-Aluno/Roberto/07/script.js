console.log("[-- INÍCIO --]");
console.log("\n");

var anos,meses,dias,idade
anos = Number(window.prompt("Quantos anos? "));
meses = Number(window.prompt("Quantos meses? ")); 
dias = Number(window.prompt("Quantos dias "));
idade = (anos*365)+(meses*30)+dias;
console.log("A sua idade é de " + idade);

console.log("\n");
console.log("[-- FIM --]");