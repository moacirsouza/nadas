console.log("[-- INÍCIO --]");
console.log("\n");

var x, y, z, resposta

x = Number(window.prompt("Digite o valor de X: "));
console.log("O valor de X é: " + x);
y = Number(window.prompt("Digite o valor de Y: "));
console.log("O valor de Y é: " + y);
z = (x*y) + 5
console.log("O valor de Z é: " + z);
if (z <= 0){
   resposta = "A"
   console.log("Os valores são: " + z + " e " + resposta);
   } 
else if (z <= 100){
    resposta = "B"
    console.log("Os valores são: " + z +  " e " + resposta);
} 
else {
    resposta = "C"
    console.log("Os valores são: " + z +  " e " + resposta);
}


console.log("\n");
console.log("[-- FIM --]");