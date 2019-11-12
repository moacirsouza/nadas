console.log("[-- INÍCIO --]");
console.log("\n");

var discente, primeiraNota, segundaNoda, terceiraNota, mediaFinal;
var pesoDaPrimeiraNota, pesoDaSegundaNota, pesoDaTerceiraNota;

pesoDaPrimeiraNota = 2;
pesoDaSegundaNota = 3;
pesoDaTerceiraNota = 5;

discente = window.prompt("Informe o nome do(a) discente:");

primeiraNota = Number(window.prompt("Informe a primeira nota de " + discente + ":"));
segundaNoda = Number(window.prompt("Informe a segunda nota de " + discente + ":"));
terceiraNota = Number(window.prompt("Informe a terceira nota de " + discente + ":"));

mediaFinal = ((primeiraNota*pesoDaPrimeiraNota) + (segundaNoda*pesoDaSegundaNota) + (terceiraNota*pesoDaTerceiraNota))/10

console.log("A média final de " + discente + " foi " + mediaFinal);

console.log("\n");
console.log("[-- FIM --]");