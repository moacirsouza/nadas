console.log("[-- INÍCIO --]");
console.log("\n");

var numero
somatorio = 0

for (var contador=1; contador<=10; contador++){
    numero = Number(window.prompt ("Digite o valor: "))
    somatorio = somatorio + numero
}
console.log("O Somatorio dos Dez numeros digitados é: " + somatorio); 


console.log("\n");
console.log("[-- FIM --]");