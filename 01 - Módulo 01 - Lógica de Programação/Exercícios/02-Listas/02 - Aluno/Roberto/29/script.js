console.log("[-- INÍCIO --]");
console.log("\n");

var n1,n2,n3

n1 = Number(window.prompt("Digite o primeiro número: " ));
console.log("O primeiro número é: " + n1);
n2 = Number(window.prompt("Digite o segundo número: " ));
console.log("O segundo número é: " + n2);
n3 = Number(window.prompt("Digite o terceiro número: " ));
console.log("O terceiro número é: " + n3);
if ((n1>n3)&&(n2>n1)){
console.log("A soma dos dois maiores é: " + (n1+n2));
}
else if ((n1>n2)&&(n3>n1)){
console.log("A soma dos dois maiores é: " + (n1+n3));   
}
else {
console.log("A soma dos dois maiores é: " + (n2+n3));
}

console.log("\n");
console.log("[-- FIM --]");