console.log("[-- INÍCIO --]");
console.log("\n");

var primeiroValor, segundoValor, valoresEmOrdemCrescente;

primeiroValor = Number(window.prompt("Informe o primeiro valor:"));
segundoValor = Number(window.prompt("Informe o segundo valor:"));

valoresEmOrdemCrescente = primeiroValor + ", " + segundoValor;

if(segundoValor < primeiroValor){
    valoresEmOrdemCrescente = segundoValor + ", " + primeiroValor;
}

console.log("Escrevendo os valores " + primeiroValor + " e " + segundoValor + ", em ordem crescente: " + valoresEmOrdemCrescente);

console.log("\n");
console.log("[-- FIM --]");