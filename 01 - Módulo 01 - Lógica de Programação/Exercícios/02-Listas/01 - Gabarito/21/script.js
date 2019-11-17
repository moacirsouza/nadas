console.log("[-- INÍCIO --]");
console.log("\n");

var horaInicio, horaFim, duracaoDoJogo, duracaoDoDia;

duracaoDoDia = 24;

horaInicio = Number(window.prompt("Informe a que horas o jogo de Xadrez começou:"));
horaFim = Number(window.prompt("Informe a que horas o jogo de Xadrez terminou:"));

if(horaInicio < horaFim){
    duracaoDoDia = 0;
}

duracaoDoJogo = horaFim - horaInicio + duracaoDoDia;

console.log("O jogo teve " + duracaoDoJogo + " hora(s) de duração.");

console.log("\n");
console.log("[-- FIM --]");