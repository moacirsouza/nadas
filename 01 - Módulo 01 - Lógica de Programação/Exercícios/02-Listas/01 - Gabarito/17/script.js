console.log("[-- INÍCIO --]");
console.log("\n");

var discente, notaDaAvaliacao01, notaDaAvaliacao02, media, resultadoFinal;

discente = window.prompt("Informe o nome do(a) aluno(a):");

notaDaAvaliacao01 = Number(window.prompt("Informe a primeira nota do(a) aluno(a) " + discente + ":"));
notaDaAvaliacao02 = Number(window.prompt("Informe a segunda nota do(a) aluno(a) " + discente + ":"));

media = (notaDaAvaliacao01+notaDaAvaliacao02)/2;

resultadoFinal = "APROVADO(A)";

if(media < 6){
    resultadoFinal = "REPROVADO(A)";
}

console.log("O(A) aluno(a) " + discente + " foi " + resultadoFinal + ", com média final " + media);


console.log("\n");
console.log("[-- FIM --]");