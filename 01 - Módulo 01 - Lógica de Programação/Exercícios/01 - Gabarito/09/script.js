console.log("[-- INÍCIO --]");
console.log("\n");

var salario, reajuste;

salario = Number(window.prompt("Informe o salário do funcionário: "));
reajuste = Number(window.prompt("Informe o valor do reajuste: "));

console.log("Valor do salário original: " + salario);
salario = salario + (salario*reajuste/100);
console.log("Valor do salário após o reajuste: " + salario);

console.log("\n");
console.log("[-- FIM --]");