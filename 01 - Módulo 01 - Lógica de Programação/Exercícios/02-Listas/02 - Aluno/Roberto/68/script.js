console.log("[-- INÍCIO --]");
console.log("\n");

 numerototalmercadorias = 0
 valordecadamercadoria = 0
 valortotalemestoque = 0
 mediavalormercadoria = 0
 soma = 0


numerototalmercadorias = Number(window.prompt("Qual o número total de mercadorias? "));

for (var i=1; i<=numerototalmercadorias; i++) {
    valordecadamercadoria = Number(window.prompt("Qual o valor de cada mercadoria? "));
    soma = soma + valordecadamercadoria
}
valortotalemestoque =  soma
mediavalormercadoria = soma/numerototalmercadorias

console.log("O valor total em estoque é: " + valortotalemestoque)
console.log("A média do valor da mercadoria é de: " + mediavalormercadoria)
        


console.log("\n");
console.log("[-- FIM --]");