console.log("[-- INÍCIO --]");
console.log("\n");

var numerodecarrosvendidos, valortotaldasvendas, salariofixo, valorrecebidoporcarrovendido, salariofinal
numerodecarrosvendidos = Number(window.prompt("Qual o número de carros vendidos? : "));
valortotaldasvendas = Number(window.prompt("Qual o valor do total das vendas? : "));
salariofixo = Number(window.prompt("Qual o salário fixo? : "));
valorrecebidoporcarrovendido = Number(window.prompt("Qual o valor recebido por veículo vendido: "));
salariofinal = salariofixo + (valorrecebidoporcarrovendido*numerodecarrosvendidos) + (5*valortotaldasvendas/100);
console.log ("O salário final do vendedor é: " + salariofinal);


console.log("\n");
console.log("[-- FIM --]");