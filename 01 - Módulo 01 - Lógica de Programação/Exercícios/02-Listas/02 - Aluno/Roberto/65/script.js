console.log("[-- INÍCIO --]");
console.log("\n");

var valor1, valor2
soma = 0

valor1 = Number(window.prompt("Digite o Primeiro Valor "))
valor2 = Number(window.prompt("Digite o Segundo Valor: "))
for (var i=valor1; i<=valor2; i++){
 soma = soma + i
 }

console.log("A soma dos valores entre os dois inteiros lidos é: " + soma);



console.log("\n");
console.log("[-- FIM --]");