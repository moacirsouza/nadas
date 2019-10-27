console.log("[-- INÍCIO --]");
console.log("\n");

var custoFinalParaOConsumidor, custoDeFabrica, porcentagemDoDistribuidor, impostos;

porcentagemDoDistribuidor = 0.28;
impostos = 0.45;

custoDeFabrica = Number(window.prompt("Informe o Custo de Fábrica do carro:"));
custoFinalParaOConsumidor = custoDeFabrica*(1+porcentagemDoDistribuidor+impostos);

console.log("O custo final do carro para o consumidor é: R$ " + custoFinalParaOConsumidor);

console.log("\n");
console.log("[-- FIM --]");