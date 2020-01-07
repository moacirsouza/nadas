console.log("[-- INÍCIO --]");
console.log("\n");

var a, b, c

a = Number(window.prompt("Qual o valor do lado A? "))
console.log("O valor do lado A é: " + a);
b = Number(window.prompt("Qual o valor do lado B? "))
console.log("O valor do lado B é: " + b);
c = Number(window.prompt("Qual o valor do lado C? "))
console.log("O valor do lado C é: " + c);
if ((a<b+c) && (b<a+c) && (c<a+b)){
    if ((a==b) && (b==c)){
        console.log("O triângulo é Equilátero")
    }
    else if ((a==b) || (b==c) || (a==c)){
        console.log("O triângulo é Isósceles")
    }
    else {
        console.log("Triângulo Escaleno");
    }  
}
else {
    console.log("Não é possível formar um Triângulo")
}




console.log("\n");
console.log("[-- FIM --]");