console.log("[-- INÍCIO --]");
console.log("\n");

var v1, v2, divisao

v1 = Number(window.prompt("Digite o primeiro valor: "))

do{
    v2 = Number(window.prompt("Digite o segundo valor (NÃO PODE SER ZERO):"));
    }while(v2 == 0);

divisao = v1/v2
console.log("O valor da divisão foi: " + divisao)

console.log("\n");
console.log("[-- FIM --]");