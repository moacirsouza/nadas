console.log("[-- INÍCIO --]");
console.log("\n");

var nomeDoAluno, nota, somaDasNotasDoBimestre, media;

nomeDoAluno = window.prompt("Informe o nome do aluno:");

function verificaNota(qualNota){
    do{
        nota = Number(window.prompt("Informe a nota " + qualNota + " do aluno " + nomeDoAluno + ":"));
    
        if( (nota < 0) || (nota > 10) ){
            window.alert("Você informou a nota " + nota + " para o aluno " + nomeDoAluno + ".\nEste valor deve estar entre 0 e 10.\nInforme um novo valor.");
        }
    }while( (nota < 0) || (nota > 10) )

    return nota;
}

// Iniciando a soma das notas com bimestre do aluno com 0
somaDasNotasDoBimestre = 0;

for(let i=0; i<2; i++){
    // A fórmula para se calcular a soma de um valor em um laço é, normalmente, a descrita
    // a seguir:
    // somaDasNotasDoBimestre = somaDasNotasDoBimestre + verificaNota(i+1);
    // O "atalho" programacional mais comum é, no entanto, o uso do operador +=, que significa
    // exatamente a mesma coisa, mas que suprime a repetição do nome da variável que vai 
    // receber o valor final.
    somaDasNotasDoBimestre += verificaNota(i+1);
}

console.log("A média do aluno " + nomeDoAluno + " é: " + (somaDasNotasDoBimestre/2));

console.log("\n");
console.log("[-- FIM --]");