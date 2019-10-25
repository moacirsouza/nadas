console.log("[-- INÍCIO --]");
console.log("\n");

var anos, meses, dias, umAno, umMes, idadeEmDias;

umAno = 365;
umMes = 30;

anos = Number(window.prompt("Digite a sua idade em anos: "));
meses = Number(window.prompt("Digite a sua idade em meses: "));
dias = Number(window.prompt("Digite a sua idade em dias: "));

idadeEmDias = anos*365 + meses*umMes + dias;

console.log("A sua idade em dias é: " + idadeEmDias);

console.log("\n");
console.log("[-- FIM --]");