console.log("[-- INÍCIO --]");
console.log("\n");

var precoA, precoG, numlitrosvendidos, tipodecombustivel, valoraserpago

precoA = 2.90
precoG = 3.30
tipodecombustivel = window.prompt("Qual o tipo de combustível? ");
console.log("O tipo de Combustível é: " + tipodecombustivel)
numlitrosvendidos = Number(window.prompt("Qual o número de litros vendidos? "));
console.log("O Número de litros vendidos foi: " + numlitrosvendidos);
if (tipodecombustivel == "A"){
    if(numlitrosvendidos > 20){
    valoraserpago = (precoA*numlitrosvendidos)*0.95
    console.log("O valor a ser pago é: " + valoraserpago)
    }
    else {
        valoraserpago = (precoA * numlitrosvendidos)*0.97
        console.log("O valor a ser pago é:" + valoraserpago)
    }
}
else if (tipodecombustivel == "G"){
    if(numlitrosvendidos > 20){
    valoraserpago = (precoG*numlitrosvendidos)*0.94
    console.log("O valor a ser pago é: " + valoraserpago)
    }
    else {
    valoraserpago = (precoG*numlitrosvendidos)*0.96
    console.log("O valor a ser pago é: " + valoraserpago)
}
}

console.log("\n");
console.log("[-- FIM --]");