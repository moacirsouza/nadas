console.log("[-- INÍCIO --]");
console.log("\n");

var resultado;

function maiorDeTres(){
    // As variáveis "numero" e "maiorNumero" são locais (i.e., foram definidas com "let")
    // e não podem ser acessadas fora da função "maiorDeTres"
    let numero, maiorNumero;

    window.alert("Este programa calcula o maior valor entre três números. Pressione 'Enter' para prosseguir.");

    for(let i = 0; i<3; i++){
        numero = Number(window.prompt("Digite o valor " + (i+1) + " :"));

        // Esse "if" é necessário, porque "maiorNumero" não foi inicializado com nenhum
        // valor. Se essa verificação não for realizada, o restante das comparações
        // não funcionará.
        if(i == 0){
            maiorNumero = numero;
            // A cláusula "continue" é necessária para evitar que o próximo "if" seja
            // executado desnecessariamente. Afinal, se "maiorNumero" e "numero" são
            // iguais, não tem motivo de verificar se um é maior que o outro.
            continue;
        }
        
        if(  numero > maiorNumero ){
            maiorNumero = numero;
        }
    }

    return maiorNumero;
}

// Foi preciso usar uma variável externa para receber o resultado da função,
// caso contrário, seria possível usar a variável "maiorNumero" do próprio retorno.
resultado = maiorDeTres();
console.log("O maior valor é: " + resultado);

console.log("\n");
console.log("[-- FIM --]");