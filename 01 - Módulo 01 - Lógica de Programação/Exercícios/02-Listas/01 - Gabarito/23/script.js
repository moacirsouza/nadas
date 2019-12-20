console.log("[-- INÍCIO --]");
console.log("\n");

var nome, sexo, altura, peso_ideal;

nome = window.prompt("Informe seu nome:");
sexo = window.prompt("Informe seu sexo (M/F):");
altura = Number(window.prompt("Informe sua altura\n(Use o ponto, ao invés da vírgula, como separador de decimais):"));

if(sexo == "M"){
    peso_ideal = (72.7 * altura) - 58;
}else{
    peso_ideal = (62.1 * altura) - 44.7;
}

console.log("O seu peso ideal é: " + peso_ideal);
console.log("O erro do programa original era não solicitar a altura do(a) usuário(a).");

console.log("\n");
console.log("[-- FIM --]");