console.log("[-- INÍCIO --]");
console.log("\n");

var eleitores,votosbranco,nulos,validos,percentvb,percentvn,percentvv
eleitores = Number(window.prompt("Qual o número total de eleitores? "));
votosbranco = Number(window.prompt("Qual o total de votosbranco "));
nulos = Number(window.prompt("Qual o número de votos nulos? "));
validos = Number(window.prompt("Qual o número de votos válidos? "));
percentvb = votosbranco/eleitores
console.log("O total de votos em branco foi: " + percentvb);
percentvn = nulos/eleitores;
console.log("O total de votos nulos foi: " + percentvn);
p
ercentvv = validos/eleitores;
console.log("O total de votos válidos foi: " + percentvv);

console.log("\n");
console.log("[-- FIM --]");