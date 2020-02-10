console.log("[-- INÍCIO --]");
console.log("\n");

 valordecadamercadoria = 0
 valortotalemestoque = 0
 mediavalormercadoria = 0
 qtde = 0
 soma = 0
 var resposta


valordecadamercadoria = Number(window.prompt("Qual o valor de cada mercadoria? "));
resposta = window.prompt("MAIS MERCADORIAS (S/N)? ")
while (resposta == "S"){  
soma = soma + valordecadamercadoria
qtde = qtde + 1
valortotalemestoque =  soma
mediavalormercadoria = soma/qtde
resposta = window.prompt("MAIS MERCADORIAS (S/N)? ")
}
console.log("O valor total em estoque é: " + valortotalemestoque)
console.log("A média do valor da mercadoria é de: " + mediavalormercadoria)
        


console.log("\n");
console.log("[-- FIM --]");