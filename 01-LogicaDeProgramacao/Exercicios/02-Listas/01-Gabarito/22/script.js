console.log("[-- INÍCIO --]");
console.log("\n");

var jornadaSemanal, jornadaMensal, quantidadeDeSemanasNoMes, jornadaDoMesAtual;
var horaExtra, salarioPorHora, salarioFinal;

quantidadeDeSemanasNoMes = 4;
jornadaSemanal = 40;
jornadaMensal = jornadaSemanal*quantidadeDeSemanasNoMes;

jornadaDoMesAtual = Number(window.prompt("Informe a jornada do mês atual:"));
salarioPorHora = Number(window.prompt("Informe o valor do salário por hora:"));

horaExtra = salarioPorHora*1.5;
salarioFinal = salarioPorHora*jornadaMensal;

if(jornadaDoMesAtual > jornadaMensal){
    salarioFinal += (jornadaDoMesAtual - jornadaMensal)*horaExtra;
}

console.log("Salário regular: " + salarioPorHora*jornadaMensal);
console.log("Horas extras neste mês: " + (jornadaDoMesAtual-jornadaMensal));
console.log("Salário final, acrescido das horas extras: " + salarioFinal);

console.log("\n");
console.log("[-- FIM --]");