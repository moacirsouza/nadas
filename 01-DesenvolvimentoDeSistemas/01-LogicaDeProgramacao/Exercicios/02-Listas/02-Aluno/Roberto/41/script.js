console.log("[-- INÍCIO --]");
console.log("\n");

var nota1, nota2, nota3, mediadosexercicios

nota1 = Number(window.prompt("Valor da Primeira Nota: "));
console.log("O valor da Primeira Nota foi: " + nota1);
nota2 = Number(window.prompt("Valor da Segunda Nota: "));
console.log("O valor da Segunda Nota foi: " + nota2);
nota3 = Number(window.prompt("Valor da Terceira Nota: "));
console.log("O valor da Terceira Nota foi: " + nota3);
mediadosexercicios = Number(window.prompt("Média dos Exercícios: "))
console.log("A média dos exercícios foi: " + mediadosexercicios);
mediadeaproveitamento = (nota1 + nota2*2 + nota3*3 + mediadosexercicios)/7
if (mediadeaproveitamento >= 9){
    console.log("O conceito foi: A ");
}
if ((mediadeaproveitamento >=7.5) && (mediadeaproveitamento < 9)){
    console.log("O conceito foi: B ");
}
if ((mediadeaproveitamento >=6) && (mediadeaproveitamento < 7.5)){
    console.log("O conceito foi: C ");
}
if (mediadeaproveitamento < 6){
    console.log("O conceito foi: D ")
}

console.log("\n");
console.log("[-- FIM --]");