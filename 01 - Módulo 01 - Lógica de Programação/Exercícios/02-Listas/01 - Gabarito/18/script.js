console.log("[-- INÍCIO --]");
console.log("\n");

var nome, anoAtual, anoDeNascimento, idadeMinimaParaSerVotante, permissaoParaVotar;

anoAtual = 2019;
idadeMinimaParaSerVotante = 18;
permissaoParaVotar = "";

nome = window.prompt("Informe o nome do(a) cidadão(ã):");
anoDeNascimento = Number(window.prompt("Informe o ano de nascimento de " + nome + ":"));

if((anoAtual-anoDeNascimento)<idadeMinimaParaSerVotante){
    permissaoParaVotar = "NÃO ";
}

permissaoParaVotar += "PODERÁ";

console.log("O(A) cidadão(ã) " + nome + " " + permissaoParaVotar + " votar este ano.");

console.log("\n");
console.log("[-- FIM --]");