console.log("[-- INÍCIO --]");
console.log("\n");

var numero
somatorio = 0

for (var contador=1; contador<=10; contador++){
numero = Number(window.prompt("Digite o Número: "));
if (numero<=40){
    somatorio = somatorio + numero
}
}
console.log("O somatorio dos valores abaixo de 40 foi: " + somatorio);



console.log("\n");
console.log("[-- FIM --]");