console.log("[-- INÍCIO --]");
console.log("\n");

var v1, v2, divisao

v1 = Number(window.prompt("Digite o primeiro valor: "))
console.log("Primeiro valor: " + v1);
v2 = Number(window.prompt("Digite o segundo valor: "))
console.log("Segundo valor: " + v2);
while (v2==0){  
    console.log("DIGITE UM VALOR DIFERENTE DE ZERO");
    v2 = Number(window.prompt("Digite o segundo valor: "))
}
divisao = v1/v2
console.log("O valor da divisão foi: " + divisao)

console.log("\n");
console.log("[-- FIM --]");