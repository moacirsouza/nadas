console.log("[-- INÍCIO --]");
console.log("\n");

var primeiroValor, segundoValor, resultadoDaDivisao;

primeiroValor = Number(window.prompt("Digite o primeiro valor:"));

do{
    segundoValor = Number(window.prompt("Digite o segundo valor (NÃO PODE SER ZERO):"));
}while(segundoValor == 0);

resultadoDaDivisao = primeiroValor/segundoValor;

console.log("O valor da divisão entre " + primeiroValor + " e " + segundoValor + " é: " + resultadoDaDivisao);

console.log("\n");
console.log("[-- FIM --]");