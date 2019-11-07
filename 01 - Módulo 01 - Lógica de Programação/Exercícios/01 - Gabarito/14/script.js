console.log("[-- INÍCIO --]");
console.log("\n");

var valor, mensagem;

mensagem = "É MAIOR QUE 10!";

valor = Number(window.prompt("Digite um valor numérico:"));

if( valor <=    10){
    mensagem = "NÃO " + mensagem;
}

console.log(mensagem);

console.log("\n");
console.log("[-- FIM --]");