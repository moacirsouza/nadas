console.log("[-- INÍCIO --]");
console.log("\n");

var anoatual, numerodoempregado, anodenascimento, anodeingresso

anoatual = 2020

numerodoempregado = Number(window.prompt("Digite o Número do Empregado: "));
console.log("Número do empregado: " + numerodoempregado);
anodenascimento = Number(window.prompt("Qual o ano de nascimento do empregado? "));
console.log("Ano de Nascimento do Empregado: " + anodenascimento);
anodeingresso = Number(window.prompt("Qual o ano de ingresso do Empregado? "));
console.log("Ano de Ingresso: " + anodeingresso);

idadedoempregado = anoatual - anodenascimento
console.log("Idade do Empregado: " + idadedoempregado);
tempodetrabalho = anoatual - anodeingresso
console.log("Tempo de Trabalho: " + tempodetrabalho)

if ((idadedoempregado >= 65) || (tempodetrabalho >=30) || (idadedoempregado >=60 && tempodetrabalho >=25)){
    console.log("A idade do empregado é: " + idadedoempregado + " O Tempo de Trabalho é: " + tempodetrabalho + " Requerer Aposentadoria");
}
else {
    console.log("A idade do empregado é: " + idadedoempregado + " O Tempo de Trabalho é: " + tempodetrabalho + " Não Requerer Aposentadoria");
}





console.log("\n");
console.log("[-- FIM --]");