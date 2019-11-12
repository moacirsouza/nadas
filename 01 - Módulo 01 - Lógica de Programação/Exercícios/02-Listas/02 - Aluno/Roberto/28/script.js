console.log("[-- INÍCIO --]");
console.log("\n");

var valor1, valor2, valor3

valor1 = Number(window.prompt("Digite o valor 1: "));
console.log("O valor 1 é: " + valor1);
valor2 = Number(window.prompt("Digite o valor 2: "));
console.log("O valor 2 é: " + valor2);
valor3 = Number(window.prompt("Digite o valor 3: "));
console.log("O valor 3 é: " + valor3);
if ((valor1>valor2)&&(valor2>valor3)){
console.log("O maior deles é: " + valor1);
}
else if ((valor2>valor1)&&(valor2>valor3)){
console.log("O maior valor é " + valor2);
}
else {
console.log ("O maior valor é: " + valor3);
}
 


console.log("\n");
console.log("[-- FIM --]");