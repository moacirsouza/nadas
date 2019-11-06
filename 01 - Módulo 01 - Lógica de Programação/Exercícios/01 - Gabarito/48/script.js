console.log("[-- INÍCIO --]");
console.log("\n");

var nomeDoAluno, primeiraNota, segundaNota, media;

nomeDoAluno = window.prompt("Informe o nome do aluno:");

do{
    primeiraNota = Number(window.prompt("Informe a primeira nota do aluno " + nomeDoAluno + ":"));

    if( (primeiraNota < 0) || (primeiraNota > 10) ){
        window.alert("Você informou a nota " + primeiraNota + " para o aluno " + nomeDoAluno + ".\nEste valor deve estar entre 0 e 10.\nInforme um novo valor.");
    }
}while( (primeiraNota < 0) || (primeiraNota > 10) )

do{
    segundaNota = Number(window.prompt("Informe a segunda nota do aluno " + nomeDoAluno + ":"));

    if( (segundaNota < 0) || (segundaNota > 10) ){
        window.alert("Você informou a nota " + segundaNota + " para o aluno " + nomeDoAluno + ".\nEste valor deve estar entre 0 e 10.\nInforme um novo valor.");
    }
}while( (segundaNota < 0) || (segundaNota > 10) )

media = (primeiraNota+segundaNota)/2;
console.log("As notas do aluno " + nomeDoAluno + " foram: " + primeiraNota + " e " + segundaNota);
console.log("A média do aluno " + nomeDoAluno + " foi: " + media);

console.log("\n");
console.log("[-- FIM --]");