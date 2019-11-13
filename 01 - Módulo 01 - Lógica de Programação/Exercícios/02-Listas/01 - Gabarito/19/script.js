console.log("[-- INÍCIO --]");
console.log("\n");

var primeiroValor, segundoValor, maior;

primeiroValor = Number(window.prompt("Informe o primeiro valor:"));
segundoValor = Number(window.prompt("Informe o segundo valor:"));

maior = primeiroValor;

if(segundoValor>primeiroValor){
    maior = segundoValor;
}


console.log("O maior valor entre " + primeiroValor + " e " + segundoValor + " é: " + maior);

console.log("\n");
console.log("[-- FIM --]");