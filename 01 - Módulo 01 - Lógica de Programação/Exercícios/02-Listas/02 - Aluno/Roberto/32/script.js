console.log("[-- INÍCIO --]");
console.log("\n");

var time1,time2,golstime1,golstime2

time1 = window.prompt("Nome do Primeiro Time: ");
console.log("O nome do primeiro time é: " + time1);
time2 = window.prompt("Nome do Segundo Time: ");
console.log("O nome do segundo time é: " + time2);
golstime1 = Number(window.prompt("O número de gols do primeiro time foi: "));
console.log("O número de gols do primeiro time foi: " + golstime1);
golstime2 = Number(window.prompt("O número de gols do segundo time foi: "));
console.log("O número de gols do segundo time foi: " + golstime2);
if (golstime1>golstime2){
    console.log("O vencedor é: " + time1);    
    }
    else if (golstime2>golstime1){
    console.log("O vencedor é: " + time2);  
    }
    else {
console.log("O resultado foi EMPATE");
    }

console.log("\n");
console.log("[-- FIM --]");