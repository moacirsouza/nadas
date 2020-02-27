console.log("[-- INÍCIO --]");
console.log("\n");

var numerodealunos, notadoaluno
somatoriodasnotas = 0

numerodealunos = Number(window.prompt("Qual o número de alunos? "))

for (var contador=1; contador<=numerodealunos; contador++){
    notadoaluno = Number(window.prompt("Nota do aluno: "));
    somatoriodasnotas = somatoriodasnotas + notadoaluno
}
media = somatoriodasnotas/numerodealunos

console.log("A média das notas dos " + numerodealunos + " alunos foi: " + media);

console.log("\n");
console.log("[-- FIM --]");