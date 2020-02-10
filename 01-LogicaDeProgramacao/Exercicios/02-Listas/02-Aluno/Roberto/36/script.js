console.log("[-- INÍCIO --]");
console.log("\n");

var idadeH1, idadeH2, idadeM1, idadeM2, idadehv, idadehn, idademv, idademn, somaidadehvmn, produtoidadehnmv

idadeH1 = Number(window.prompt("Qual a idade do Primeiro Homem? "));
console.log("A idade do Primeiro Homem é: " + idadeH1);
idadeH2 = Number(window.prompt("Qual a idade do Segundo Homem?" ));
console.log("A idade do Segundo Homem é: " + idadeH2);
idadeM1 = Number(window.prompt("Qual a idade da Primeira Mulher? "));
console.log("A idade da Primeira Mulher é: " + idadeM1);
idadeM2 = Number(window.prompt("Qual a idade da Segunda Mulher? "));
console.log("A idade da Segunda Mulher é: " + idadeM2);
if (idadeH1 > idadeH2){
    idadehv = idadeH1
    idadehn = idadeH2
}
else if (idadeH1 < idadeH2){
    idadehv = idadeH2
    idadehn = idadeH1
}
if (idadeM1 > idadeM2){
    idademv = idadeM1
    idademn = idadeM2
}
else if (idadeM1 < idadeM2){
    idademv = idadeM2
    idademn = idadeM1
}
somaidadehvmn = idadehv + idademn
produtoidadehnmv = idadehn * idademv

console.log("A soma das idades do Homem mais velho e a Mulher mais nova é: " + somaidadehvmn);
console.log("O produto das idades do Homem mais novo e a Mulher mais velha é: " + produtoidadehnmv);

console.log("[-- FIM --]");