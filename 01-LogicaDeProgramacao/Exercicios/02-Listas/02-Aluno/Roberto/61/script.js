console.log("[-- INÍCIO --]");
console.log("\n");

var n
somatorio = 0

for (var contador=1; contador<=10; contador++){
n = Number(window.prompt("Qual o valor? "));
somatorio = somatorio + n
}
media = somatorio/10

console.log("A média aritmética dos Dez valores lidos foi: " + media);

console.log("\n");
console.log("[-- FIM --]");