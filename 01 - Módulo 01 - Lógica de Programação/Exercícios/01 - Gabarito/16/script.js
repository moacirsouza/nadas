console.log("[-- INÍCIO --]");
console.log("\n");

var custoDaMaca, macasCompradas, valorFinal;

custoDaMaca = 1.3;

macasCompradas = Number(window.prompt("Comprou quantas maçãs?"));

if(macasCompradas >= 12){
    custoDaMaca = 1;
}

valorFinal = custoDaMaca*macasCompradas;

console.log("O custo total da compra (" + macasCompradas + " maçãs), foi R$ " + valorFinal + ".");

console.log("\n");
console.log("[-- FIM --]");