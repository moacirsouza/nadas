console.log("[-- INÍCIO --]");
console.log("\n");

var nomedoaluno, nota1, nota2, media, resposta

nomedoaluno = window.prompt("Qual o nome do aluno? ")

do{
    
    do{
    nota1 = Number(window.prompt("Digite a primeira nota: "));
    if ((nota1 < 0) || (nota1 > 10)){
    window.alert("A nota está incorreta.\nEste valor deve estar entre 0 e 10 ")
}
}while ((nota1 < 0) || (nota1 > 10))

do{
    nota2 = Number(window.prompt("Digite a segunda nota "));
    if ((nota2 < 0) || (nota2 > 10)){
    window.alert("A nota está incorreta.\nEste valor deve estar entre 0 e 10 ")    
    } 
}while ((nota2 < 0) || (nota2 > 10))

media = (nota1+nota2)/2

window.alert("A média do aluno " + nomedoaluno + " foi " + media);

resposta = window.prompt("NOVO CÁLCULO (S/N)? ");

}while (resposta == "S");


console.log("\n");
console.log("[-- FIM --]");