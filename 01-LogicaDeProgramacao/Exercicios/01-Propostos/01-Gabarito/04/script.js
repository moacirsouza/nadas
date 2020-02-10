console.log("[-- INÍCIO --]");
console.log("\n");

var usuario, listaDeCompras, contador, finalizador;

// OBRIGATÓRIO: Inicia o "contador" da quantidade de itens
// da lista como zero. Ele vai ser utilizado como índice
// do Array, logo, será submetido a cálculos e manipulações
// aritméticas
contador = 0;

// OBRIGATÓRIO: Inicia o "finalizador" como uma String vazia,
// uma vez que ele vai ser o parâmetro que o
// laço de entrada vai verificar a cada iteração
finalizador = "";

// OBRIGATÓRIO: Inicia a lista como um Array vazio.
// Também é possível iniciá-lo com valores, mas se
// ele vai ser sobrescrito quando o usuário começar a
// informar a lista de compras, para quê gastar memória
// com isso? ¯\_(ツ)_/¯
listaDeCompras = [];

usuario = window.prompt("Crie sua Lista de Compras!\n\nPara começar, por favor, informe o seu nome:");

while( finalizador != "FECHAR"){
    // Este é um "truqe" divertido, para mostrar o número
    // da mensagem com, no mínimo, duas posições
    let mostrador = (contador+1).toString().padStart(2,"0");

    // Como a mensagem estava muito comprida, decidi colocá-la
    // em uma variável. É uma ação opcional, mas valiosa, pois
    // se ela precisar mudar, o código em si, a lógica, não muda.
    // Só quem muda é a mensagem ;).
    let mensagem = "(ATENÇÃO: Para finalizar, digite FECHAR, em letras maiúsculas e sem espaços)\n\nInforme o item: ";

    // Este é outro "truque" interessante.
    // A expressão a seguir é do tipo: "a = b = c".
    // Ela é avaliada da seguinte forma: "a = (b = c)".
    // Logo, o valor de "c" é passado para "b" que, por fim,
    // é passado para "a".
    finalizador = listaDeCompras[contador] = window.prompt(mensagem + mostrador);

    // Incrementa o contador a cada iteração
    contador++;
}

// O "pop()" é um método primitivo do JavaScript, presente
// em praticamente todas as linguagens de programação, cuja
// função é remover o último item do Array.
// A importâncoa dele neste programa é que a lista final
// não vai conter o valor do "finalizador".
listaDeCompras.pop();

console.log("PARABÉNS, sua lista de compras foi criada!\n\n");
console.log("+---------------------------------");
console.log("| Lista de compras de " + usuario);
console.log("+---------------------------------");

// Por fim, a lista é lida com um "for" (Afinal, agora sabemos
// a quantidade exata de itens contidos nela!), afim de mostrar
// o resultado na tela para o usuário
for(let i=0; i<listaDeCompras.length; i++){
    let mostrador = (i+1).toString().padStart(2,"0");
    console.log("Item " + mostrador + ": " + listaDeCompras[i]);
}

console.log("\n");
console.log("[-- FIM --]");
