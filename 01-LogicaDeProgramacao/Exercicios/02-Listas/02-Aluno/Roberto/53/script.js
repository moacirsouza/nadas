console.log("[-- INÍCIO --]");
console.log("\n");

var N

N = Number(window.prompt("Informe o Número: "));
console.log("O valor de N é: " + N);

if (N > 0){
for (var i=1; i<=N; i++){
    console.log(i)
}  
}
else {
    console.log("O valor precisa ser maior que zero");
} 

console.log("\n");
console.log("[-- FIM --]");