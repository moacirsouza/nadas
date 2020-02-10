console.log("[-- INÍCIO --]");
console.log("\n");

var salariofixo, valordasvendas, salariototal

salariofixo = Number(window.prompt("Qual o valor do salário fixo? "));
console.log("O valor do salário fixo é: " + salariofixo);
valordasvendas = Number(window.prompt("O valor das vendas foi: "));
console.log("O valor das vendas foi: " + valordasvendas);
if (valordasvendas<=1500){
salariototal = salariofixo + 0.03*salariofixo 
console.log("O Salário total foi: " + salariototal);
}
else{
salariototal = salariofixo + 0.03*salariofixo + 0.05*(valordasvendas-1500);
console.log("O Salário total foi: " + salariototal);
}
console.log("\n");
console.log("[-- FIM --]");