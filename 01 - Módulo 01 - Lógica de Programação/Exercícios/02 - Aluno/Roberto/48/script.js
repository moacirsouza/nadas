console.log("[-- INÍCIO --]");
console.log("\n");

var nomeDoAluno, nota, media;

nomeDoAluno = window.prompt("Informe o nome do aluno:");

function verificaNota(qualNota){
    do{
        nota = Number(window.prompt("Informe a nota "+ qualNota + " do aluno " + nomeDoAluno + ":"));
    
        if( (nota < 0) || (nota > 10) ){
            window.alert("Você informou a nota " + nota + " para o aluno " + nomeDoAluno + ".\nEste valor deve estar entre 0 e 10.\nInforme um novo valor.");
        }
    }while( (nota < 0) || (nota > 10) )

    console.log(nota);
}

for(let i=0; i<2; i++){
    console.log("O valor de i, nesta iteração é: " + i);
    verificaNota(i+1);
}

/*media = (primeiraNota+nota)/2;

console.log("As notas do aluno " + nomeDoAluno + " foram: " + primeiraNota + " e " + nota);
console.log("A média do aluno " + nomeDoAluno + " foi: " + media);
*/

console.log("\n");
console.log("[-- FIM --]");