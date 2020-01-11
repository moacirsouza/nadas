console.log("[-- INÍCIO --]");
console.log("\n");

var v1, v2, divisao

v1 = Number(window.prompt("Digite o primeiro valor: "))
console.log("Primeiro valor: " + v1);
v2 = Number(window.prompt("Digite o segundo valor: "))
console.log("Segundo valor: " + v2);
while (v2==0){  
    window.alert("VALOR INVALIDO");
    v2 = Number(window.prompt("Digite o segundo valor: "))
}
divisao = v1/v2
console.log("O valor da divisão de: " + v1 + " por " + v2 + " foi " + divisao)

console.log("\n");
console.log("[-- FIM --]");