console.log("[-- INÍCIO --]");
console.log("\n");

var valor, qualificacaoDoNumero;

qualificacaoDoNumero = "positivo";

valor = Number(window.prompt("Informe um valor numérico:"));

if( valor < 0){
    qualificacaoDoNumero = "negativo";
}

console.log("O valor informado (" + valor + ") é " + qualificacaoDoNumero + ".");

console.log("\n");
console.log("[-- FIM --]");