console.log("[-- INÍCIO --]");
console.log("\n");

var agenteDeVendas, salarioFixo, totalDeVendas, baseParaCalculoDaComissao, tetoParaComissaoNivelUm, comissaoNivelUm, comissaoNivelDois, salarioFinal;

// Os três valores a seguir viraram variáveis ao invés de
// serem inseridos diretamente no código. Esta é uma solução
// mais elegante, pois, se algum dos números mudar no futuro,
// estes serão os únicos lugares que precisarão sofrer alteração,
// deixando o código mais limpo e fácil de manter
tetoParaComissaoNivelUm = 1500;
comissaoNivelUm = 0.03;
comissaoNivelDois = 0.05;

// Inicia o salário final com 0, afim de evitar um "else" extra
// durante o cálculo das comissões
salarioFinal = 0;

agenteDeVendas = window.prompt("Agente de Vendas:");
salarioFixo = Number(window.prompt("Informe o salário fixo de " + agenteDeVendas + ":"));
totalDeVendas = Number(window.prompt("Informe o valor total de vendas de " + agenteDeVendas + ":"));
baseParaCalculoDaComissao = totalDeVendas;

// Apenas se o total de vendas for maior que 1500 é que o
// salário final recebe um acréscimo de 5% em cima da
// diferença entre o total de vendas e o teto
if(totalDeVendas > tetoParaComissaoNivelUm){
    salarioFinal = (totalDeVendas-tetoParaComissaoNivelUm)*comissaoNivelDois;
    baseParaCalculoDaComissao = tetoParaComissaoNivelUm;
}

// Se a variável "salarioFinal" não houvesse sido inicializada
// com 0, todas as vezes que o total de vendas fosse menor ou igual
// ao teto, o uso do "+=" retornaria "NaN" (Not a Number), pois
// tentaria usar, no cálculo, o valor de "salarioFinal", que neste
// momento seria "undefined". Ao forçar aquela atribuição logo cedo
// no código, somos capazes de evitar o uso de um "else" extra.
salarioFinal += salarioFixo + (baseParaCalculoDaComissao*comissaoNivelUm);

console.log("O salário final de " + agenteDeVendas + " é: " + salarioFinal);

console.log("\n");
console.log("[-- FIM --]");