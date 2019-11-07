console.log("[-- INÍCIO --]");
console.log("\n");

var vendedor, proventosMensais, comissaoPorVeiculo, percentualSobreValorTotalDeVendas, totalDeVeiculosVendidos, salarioFinal;

vendedor = window.prompt("Informe o nome do vendedor:");
percentualSobreValorTotalDeVendas = 0.05;
proventosMensais = Number(window.prompt("Informe o salário de " + vendedor + ":"));
totalDeVeiculosVendidos = Number(window.prompt("Informe a quantidade de carros vendidos por " + vendedor + ":"));
comissaoPorVeiculo = Number(window.prompt("Informe, em Reais, o valor da comissão fixa por carro:"))
valorTotalDasVendas = Number(window.prompt("Informe o valor total de vendas, em Reais, do vendedor " + vendedor + ":"));

salarioFinal = proventosMensais + comissaoPorVeiculo*totalDeVeiculosVendidos + percentualSobreValorTotalDeVendas*valorTotalDasVendas;
console.log("O salário final do vendedor " + vendedor + "é: " + salarioFinal);

console.log("\n");
console.log("[-- FIM --]");