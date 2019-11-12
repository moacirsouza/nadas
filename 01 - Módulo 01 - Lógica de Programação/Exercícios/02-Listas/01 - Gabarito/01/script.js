console.log("[-- INÍCIO --]");
console.log("\n");

var A, B, temporario;

A = 10;
B = 20;

console.log("O valor original de A eh: " + A);
console.log("O valor original de B é: " + B);

temporario = A;
A = B;
B = temporario;

console.log("O valor de A, depois da troca é: " + A);
console.log("O valor de B, depois da troca é: " + B);

console.log("\n");
console.log("[-- FIM --]");