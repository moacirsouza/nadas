console.log("[-- INÍCIO --]");
console.log("\n");

var numerodemacascompradas, custototaldacompra

numerodemacascompradas = Number(window.prompt("Qual o número de Maças compradas: ? "));
if (numerodemacascompradas<12){
custototaldacompra = 1.30*numerodemacascompradas
console.log("O Custo Total da Compra é: " + custototaldacompra)    
}
else{
custototaldacompra = 1.00*numerodemacascompradas
console.log("O Custo Total da Compra é: " + custototaldacompra)
}
console.log("\n");
console.log("[-- FIM --]");