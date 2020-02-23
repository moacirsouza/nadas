console.log("[-- INÍCIO --]");
console.log("\n");

var qtdeatualemestoque, qtdemaximaemestoque, qtdeminimaemestoque, qtdemedia, qtdeatualemestoque

qtdeatualemestoque = (window.prompt("Qtde atual em estoque: "));
console.log("Qtde atual em estoque é: " + qtdeatualemestoque);
qtdemaximaemestoque = (window.prompt("Qtde máxima em estoque: "));
console.log("Qtde máxima em estoque é: " + qtdemaximaemestoque);
qtdeminimaemestoque = (window.prompt("Qtde mínima em estoque: "));
console.log("Qtde mínima em estoque: " + qtdeminimaemestoque);
qtdemedia = (qtdemaximaemestoque/2) + (qtdeminimaemestoque/2);
console.log("A quantidade média em estoque é: " + qtdemedia);
if (qtdeatualemestoque>=qtdemedia){
console.log("Não efetuar a compra");
}
else{
console.log("Efetuar a compra");
}

console.log("\n");
console.log("[-- FIM --]");