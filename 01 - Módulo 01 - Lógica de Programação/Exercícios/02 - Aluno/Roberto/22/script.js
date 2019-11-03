console.log("[-- INÍCIO --]");
console.log("\n");

var nhorastrab,vlrhorareg,salnormal,saltotal,vlrhoraext

nhorastrab = Number(window.prompt("Número de horas trabalhadas por mês: "))
console.log("O número de horas trabalhadas no mês foi: " + nhorastrab);
vlrhorareg = Number(window.prompt("O salário por hora é: "));
console.log("O salário por hora é: " + vlrhorareg);
if (nhorastrab>160){
vlrhoraext = vlrhorareg + (vlrhorareg*50/100)
saltotal = 160*vlrhorareg + vlrhoraext
console.log("O salário por hora é: " + vlrhorareg)
console.log("O salário total do funcionário é: " + saltotal)
}
else{
salnormal = nhorastrab*vlrhorareg
console.log("O salário normal do funcionário foi de: " + salnormal)
}
 
console.log("\n");
console.log("[-- FIM --]");