console.log("[-- INÍCIO --]");
console.log("\n");

var nome, altura, sexo, pesoideal, M, F

nome = window.prompt("Qual o nome da pessoa? ");
console.log("O nome da pessoa é: " + nome);
sexo = window.prompt("Qual o sexo da pessoa? M ou F ");
console.log("O sexo da pessoa é: " + sexo);
altura = Number(window.prompt("Qual a altura da pessoa? "));
console.log("A altura da pessoa é: " + altura);
if (sexo = M){
pesoideal = (72.7*altura) - 58;
console.log("O peso ideal de " + nome + " é: " + pesoideal);
}
else{ 
pesoideal = (62.1*altura) - 44.7 
console.log("O peso ideal de " + nome + " é: " + pesoideal);     
}

console.log("\n");
console.log("[-- FIM --]");

