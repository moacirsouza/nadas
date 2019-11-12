console.log("[-- INÍCIO --]");
console.log("\n");

var salario,reajuste,novosalario

salario = Number(window.prompt("Salário mensal do funcionário "));
reajuste = Number(window.prompt("Percentual de Reajuste "))
novosalario = salario + (salario*reajuste)/100;
console.log("O valor do novo salário é: " + novosalario);
console.log("\n");
console.log("[-- FIM --]");