console.log("[-- INÍCIO --]");
console.log("\n");

var n1,n2,media,aluno
aluno = window.prompt("Nome do Aluno: ");
n1 = Number(window.prompt("A nota da primeira avaliação foi: " ));
n2 = Number(window.prompt("A nota da segunda avaliação foi: "));
media = (n1+n2)/2
if (media>=6){
console.log("O aluno " + aluno + " está APROVADO COM MÉDIA: " + media);
}
else{
console.log("O aluno " + aluno + " está com MEDIA " + media + " e portanto REPROVADO ");
}

console.log("\n");
console.log("[-- FIM --]");