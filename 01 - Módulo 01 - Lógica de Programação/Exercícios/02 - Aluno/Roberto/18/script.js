console.log("[-- INÍCIO --]");
console.log("\n");

var anoatual, anodenascimento, idadedevoto

anoatual = Number(window.prompt("Qual o ano atual: "));
anodenascimento = Number(window.prompt("Qual o ano de nascimento: "));
idadedevoto = anoatual-anodenascimento
if (idadedevoto>=18){
console.log("Você poderá votar ");
}
else{
console.log("Você não poderá votar ");
}

console.log("\n");
console.log("[-- FIM --]");