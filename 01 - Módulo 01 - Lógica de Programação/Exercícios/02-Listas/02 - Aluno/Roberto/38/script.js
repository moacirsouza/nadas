console.log("[-- INÍCIO --]");
console.log("\n");

var codusuario, senha

codusuario = Number(window.prompt("Qual o código do usuário?"));

if (codusuario != 1234){
    console.log("'Usuário Inválido!'");
}
else if (codusuario = 1234){
senha = Number(window.prompt("Qual a senha de acesso? "));
if (senha != 9999){
    console.log("senha incorreta");
}
else {
    console.log("'Acesso Permitido'");
}
}
console.log("\n");
console.log("[-- FIM --]");