console.log("[-- INÍCIO --]");
console.log("\n");

var inicio,fim,total

inicio = Number(window.prompt("Informe o horário de início do jogo: "));
console.log("O horário de início foi: " + inicio);
fim = Number(window.prompt("Informe o horário de fim do jogo: "));
console.log("O horário de término foi: " + fim);
if (fim<inicio){
total = (24-inicio) + fim
console.log ("O total de horas jogadas foi: " + total);
}
else if (fim>inicio){
total = fim - inicio
console.log("O total de horas jogadas foi: " + total);
}
else{
(fim=inicio)
total = 24
console.log ("Ele jogou por: " + total);
}

console.log("\n");
console.log("[-- FIM --]");