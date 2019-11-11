console.log("[-- INÍCIO --]");
console.log("\n");

var A,B,C,D,E,F,G,H,I,J

A = 6*(3+2);
console.log("A letra a) A <- 6*(3+2): " + A)
console.log("\tNão é possível mudar remover os parênteses sem mudar o valor da expressão. ");
console.log("\tProva:");
A = 6*3+2
console.log("\tA <- 6*3+2: " + A);
console.log("\n");

B = 2+(6*(3+2));
console.log("A letra b) B <- 2+(6*(3+2)): " + B);
console.log("\tÉ possível remover os parênteses mais externos sem mudar o valor da expressão. ");
console.log("\tProva:");
B = 2+6*(3+2);
console.log("\tB <- 2+6*(3+2): " + B);
console.log("\n");

C = 2+(3*6)/(2+4)
console.log("A letra c) C <- 2+(3*6)/(2+4): " + C);
console.log("\tÉ possível remover o primeiro parênteses sem mudar o valor da expressão. ");
console.log("\tProva");
C = 2+3*6/(2+4);
console.log("\tC <- 2+3*6/(2+4): " + C);
console.log("\n");
       

D = 2*(8/(3+1))
console.log("A letra d) D <- 2*(8/(3+1)): " + D);
console.log("\tÉ possível removar os parênteses mais externos sem mudar o valor da expressão."); 
console.log("\tProva:");
D = 2*8/(3+1);
console.log("\t D <- 2*8/(3+1): " + D);
console.log("\n");

E = 3+(16-2)/(2*(9-2))
console.log(" letra e) E <-3+(16-2)/(2*(9-2)): " + E);
console.log("\t Não é possível remover os parênteses sem mudar o valor da expressão. ");
console.log("\tProva:");
E = 3+16-2/(2*(9-2))
console.log("\t E <- 3+16-2/(2*(9-2)): " + E);
E = 3+(16-2)/2*(9-2)
console.log("\t E <- 3+(16-2)/2*(9-2): " + E);
console.log("\n");


F = (6/3)+(8/2)
console.log("letra f) F <- (6/3)+(8/2): " + F);
console.log("\tÉ possível alterar quaisquer pares de parênteses sem remover o valor da expressão. ");
console.log("\tProva:");
F = 6/3+8/2
console.log("\t F <- 6/3+8/2: " + F);
console.log("\n");

G = ((3+(8/2))*4)+(3*2)
console.log("letra g) G <- ((3+(8/2))*4)+(3*2): " + G);
console.log("\tÉ possível remover o primeiro, o terceiro e o último par de parênteses sem alterar o resultado.");
console.log("\tProva:");
G = (3+(8/2))*4+(3*2);
console.log("\t G <-(3+(8/2)*4)+(3*2): " + G);
G = ((3+8/2)*4)+(3*2);
console.log("\t G <- ((3+8/2)*4)+(3*2): " + G);
G = ((3+(8/2))*4)+3*2
console.log("\t G <- ((3+(8/2))*4)+3*2: " + G);
console.log("\n");


H = (6*(3*3)+6)-10
console.log("letra h) H <- (6*(3*3)+6)-10: " + H);
console.log("\tÉ possível alterar todos os parênteses sem alterar o resultado.");
console.log("\tProva: ");
H = 6*3*3+6-10;
console.log("\t H <- 6*3*3+6-10: " + H)
console.log("\n");

I = (((10*8)+3)*9)
console.log("letra i) I <- (((10*8)+3)*9) " + I);
console.log("\t É possível remover o primeiro e o terceiro parênteses sem alterar o resultado. ");
console.log("\tProva");
I = ((10*8)+3)*9;
console.log("\t I <- ((10*8)+3)*9: " + I);
I = ((10*8+3)*9);
console.log("\t I <- ((10*8+3)*9): "+ I);
console.log("\n");

J = ((-12)*(-4))+(3*(-4))
console.log("letra j) J <- ((-12)*(-4))+(3*(-4)): " + J);
console.log("É possível remover quaisquer parênteses sem alterar o resultado. ");
console.log("\tProva - Exemplos");
J = (-12)*(-4)+(3*(-4));
console.log("\t J <- (-12)*(-4)+(3*(-4)): " + J);
J = (-12*(-4))+(3*(-4));
console.log("\t J <- (-12*(-4))+(3*(-4)): " + J);
J = ((-12)*(-4))+3*(-4)
console.log("\t J <- ((-12)*(-4))+3*(-4): " + J);
console.log("\n");


console.log("[-- FIM --]");