console.log("[-- INÍCIO --]");
console.log("\n");

var precomorango, precomaca, pesomorango, pesomaca, totalmorango, totalmaca, valorfinal

precomorango = 2.5
precomaca = 1.8

pesomorango = Number(window.prompt("Quantos Kilos de Morango: "));
console.log("Quantos Kilos de Morango? " + pesomorango);
pesomaca = Number(window.prompt("Quantos Kilos de Maça?  " + pesomaca));
console.log("Quantos Kilos de Maça? " + pesomaca);

if (pesomorango > 5) {
    totalmorango = (precomorango - 0.3) * pesomorango
}
else {
    totalmorango = precomorango * pesomorango
}
if (pesomaca > 5) {
    totalmaca = (precomaca - 0.3) * pesomaca    
}
else {
    totalmaca = precomaca * pesomaca
}
if ((totalmorango + totalmaca) > 25 || (pesomorango + pesomaca) > 8 ) {
    valorfinal = (totalmorango + totalmaca) * 0.9
    }
else {
    valorfinal = totalmorango + totalmaca
    }
console.log ("O valor final da compra foi: " + valorfinal);

console.log("\n");
console.log("[-- FIM --]");