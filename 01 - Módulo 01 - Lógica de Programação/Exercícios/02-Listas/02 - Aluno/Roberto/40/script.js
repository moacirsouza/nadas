console.log("[-- INÍCIO --]");
console.log("\n");

var nomeproduto, qtdeprod, precoproduto, desconto, total, totalapagar

nomeproduto = window.prompt("Qual o produto? " );
console.log("O produto é: " + nomeproduto);
qtdeprod = Number(window.prompt("Qual a quantidade do produto? "));
console.log("A quantidade do produto é: " + qtdeprod);
precoproduto = Number(window.prompt("Qual o preço do produto? "));
console.log("O preço do produto é: " + precoproduto);
total = qtdeprod * precoproduto
console.log("O total foi: " + total);

if (qtdeprod <= 5){
    desconto = 0.02
    totalapagar = (total*0.98);
    console.log("O desconto foi de " + desconto + " e o total a pagar será de: " + totalapagar);
}
if ((qtdeprod > 5) && (qtdeprod <= 10)){
    desconto = 0.03
    totalapagar = (total*0.97);
    console.log("O desconto foi de " + desconto + " e o total a pagar será: de " + totalapagar);
}
if (qtdeprod > 10){
    desconto = 0.05
    totalapagar = (total*0.95);
    console.log("O desconto foi de " + desconto + " e o total a pagar será de " + totalapagar);
}

console.log("\n");
console.log("[-- FIM --]");