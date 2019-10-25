console.log("[-- INÍCIO --]");
console.log("\n");

var eleitores, votosBrancos, votosNulos, votosValidos, totalDeVotos;
var percentualDeVotosBrancos, percentualDeVotosNulos, percentualDeVotosValidos;

eleitores    = Number(window.prompt("Informe o total de Eleitores do Município:"));
votosBrancos = Number(window.prompt("Informe o total de votos Brancos:"));
votosNulos   = Number(window.prompt("Informe o total de votos Nulos:"));
votosValidos = Number(window.prompt("Informe o total de votos Válidos:"));

totalDeVotos = votosBrancos + votosNulos + votosValidos;

percentualDeVotosBrancos = eleitores*votosBrancos/100;
percentualDeVotosNulos = eleitores*votosNulos/100;

console.log("+------------------------------------+");
console.log("       [Resultado das Eleições]       ");
console.log("+------------------------------------+");
console.log("|  Votos  | Quantidade/Porcentagem |");
console.log("+---------+------------+-------------+");
console.log("| Válidos |  |");
console.log("| Brancos |            | Porcentagem |");
console.log("| Nulos   |            | Porcentagem |");
console.log("+---------+------------+-------------+");

console.log("\n");
console.log("[-- FIM --]");