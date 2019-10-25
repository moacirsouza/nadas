console.log("[-- INÍCIO --]");
console.log("\n");

var mensagem, nome, anos, meses, dias, umAno, umMes, idadeEmDias;

umAno = 365;
umMes = 30;

nome = window.prompt("Olá! Vou calcular sua idade em dias. Mas primeiro, preciso saber qual é o seu nome:");
window.alert("A seguir eu preciso saber há quantos anos, meses e dias você está vivo:");
anos = Number(window.prompt("Anos: "));
meses = Number(window.prompt("Meses: "));
dias = Number(window.prompt("Dias: "));

idadeEmDias = anos*umAno + meses*umMes + dias;

console.log("Oi, " + nome + "!\n\nVocê já viveu " + idadeEmDias + " dias! Incrível!");

console.log("\n");
console.log("[-- FIM --]");