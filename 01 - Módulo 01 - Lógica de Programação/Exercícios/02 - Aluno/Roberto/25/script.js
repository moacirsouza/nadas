console.log("[-- INÍCIO --]");
console.log("\n");

var numerodaconta, saldo, debito, credito, saldoatual

numerodaconta = Number(window.prompt("Número da Conta: "));
console.log("O número da conta é: " + numerodaconta);
saldo = Number(window.prompt("O saldo em conta é: "));
console.log("O saldo da conta é: " + saldo);
debito = Number(window.prompt("O valor do débito é: "));
console.log("O valor do débito é: " + debito);
credito = Number(window.prompt("O valor do crédito é: " + credito));
console.log("O valor do crédito é: " + credito);
saldoatual = saldo - debito + credito
console.log("O valor do saldo atual é: " + saldoatual);
if (saldoatual>=0){
console.log("O saldo é POSITIVO");
}
else{
console.log("O saldo é NEGATIVO");    
}

console.log("\n");
console.log("[-- FIM --]");