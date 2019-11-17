console.log("[-- INÍCIO --]");
console.log("\n");

var L1,L2,L3

L1 = Number(window.prompt("Digite o valor do L1: "));
L2 = Number(window.prompt("Digite o valor de L2: "));
L3 = Number(window.prompt("Digite o valor de L3: "));

if (L1<(L2+L3)&&L2<(L1+L3)&&L3<(L1+L2)){
console.log("É um triângulo");
}
else {
console.log("Não é um triângulo");
}  

console.log("\n");
console.log("[-- FIM --]");