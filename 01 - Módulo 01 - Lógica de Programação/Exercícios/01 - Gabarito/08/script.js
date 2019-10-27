console.log("[-- INÍCIO --]");
console.log("\n");

/*
Nota do Instrutor: Todas as variáveis abaixo poderiam ter sido definidas
em apenas uma linha. A separação foi proposital, apenas para melhorar
a legiblidade do código.
*/
var eleitores, votosBrancos, votosNulos, votosValidos, totalDeVotos, abstinencias;
var percentualDeVotosBrancos, percentualDeVotosNulos;
var percentualDeVotosValidos, percentualDeAbstinencias;

eleitores    = Number(window.prompt("Informe o total de Eleitores do Município:"));
votosValidos = Number(window.prompt("Informe o total de votos Válidos:"));
votosBrancos = Number(window.prompt("Informe o total de votos Brancos:"));
votosNulos   = Number(window.prompt("Informe o total de votos Nulos:"));

totalDeVotos = votosBrancos + votosNulos + votosValidos;
abstinencias = eleitores - totalDeVotos;

percentualDeVotosBrancos = votosBrancos*100/eleitores;
percentualDeVotosNulos = votosNulos*100/eleitores;
percentualDeVotosValidos = votosValidos*100/eleitores;
percentualDeAbstinencias = abstinencias*100/eleitores;

console.log("+-----------------------------------------+");
console.log("|            [Totalizadores]              |");
console.log("+-----------------------------------------+");
console.log("| Eleitores    | " + eleitores);
console.log("| Votos        | " + totalDeVotos);
console.log("\n");

console.log("+-----------------------------------------+");
console.log("|      [Estatísticas das Eleições]        |");
console.log("+-----------------------------------------+");
console.log("|    Votos     |  Quantidade/Porcentagem  |");
console.log("+--------------+--------------------------+");
console.log("| Válidos      | " + votosValidos + "/" + percentualDeVotosValidos + "%");
console.log("| Brancos      | " + votosBrancos + "/" + percentualDeVotosBrancos + "%");
console.log("| Nulos        | " + votosNulos + "/" + percentualDeVotosNulos + "%");
console.log("| Abstinências | " + abstinencias + "/" + percentualDeAbstinencias + "%");

console.log("\n")
console.log("[-- FIM--]");