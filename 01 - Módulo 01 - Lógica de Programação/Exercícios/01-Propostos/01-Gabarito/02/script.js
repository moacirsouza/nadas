console.log("[-- INÍCIO --]");
console.log("\n");

// Não há necessidade de criar uma variável global para receber o resultado.
// Ela foi definida com "var" apenas por conveniência/costume, mas um "let"
// poderia ter sido usado sem problemas.
var resultado;

// Lembre-se: Aqui é apenas a DEFINIÇÃO da função, não a chamada.
function maiorDeTres(){
    // Aqui temos um exemplo de variáveis locais (i.e., foram definidas com "let").
    // Neste caso, "numero" e "maiorNumero" não podem ser acessadas fora da 
    // função "maiorDeTres".
    let numero, maiorNumero;

    window.alert("Este programa calcula o maior valor entre três números. Pressione 'Enter' para prosseguir.");

    for(let i = 0; i<3; i++){
        numero = Number(window.prompt("Digite o valor " + (i+1) + " :"));

        // Esse "if" é necessário, porque "maiorNumero" não foi inicializado com nenhum
        // valor. Se essa verificação não for realizada, o restante das comparações
        // não funcionará.
        if(i == 0){
            maiorNumero = numero;
            // A cláusula "continue" foi utilizada para evitar que o próximo "if" seja
            // executado desnecessariamente. Afinal, se durante essa iteração os valores 
            // de "maiorNumero" e "numero" são iguais, não tem motivo para executar o próximo
            // teste. A cláusula "continue" foi usada para "pular" diretamente para a próxima
            // iteração do laço, quando o segundo número será recebido do usuário. 
            continue;
        }
        
        if(numero > maiorNumero){
            maiorNumero = numero;
        }
    }

    return maiorNumero;
}

// AQUI é onde a função é efetivamente chamada ou invocada. Perceba que, como se trata
// de uma FUNÇÃO e não um PROCEDIMENTO, é necessário armazenar o valor do retorno (realizado
// pela cláusula "return") em uma variável para depois manipulá-lo.
resultado = maiorDeTres();

console.log("O maior valor é: " + resultado);

console.log("\n");
console.log("[-- FIM --]");