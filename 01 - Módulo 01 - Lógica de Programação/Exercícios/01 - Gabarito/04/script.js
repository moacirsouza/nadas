console.log("[-- INÍCIO --]");
console.log("\n");

var A, B, C, D, E, F, G, H, I, J;

console.log("Letra a) A <- 6*(3+2)");
console.log("\tNão é possível remover os parênteses sem alterar o valor da expresão.\n\tProva:");
A = 6*(3+2);
console.log("\tA <- 6*(3+2): " + A);
A = 6*3+2;
console.log("\tA <- 6*3+2: " + A);
console.log("\n");

console.log("Letra b) B <- 2+(6*(3+2))");
console.log("\tÉ possível remover os parênteses mais externos sem alterar o resultado.\n\tProva:")
B = 2+(6*(3+2));
console.log("\tB <- 2+(6*(3+2)): " + B);
B = 2+6*(3+2);
console.log("\tB <- 2+6*(3+2): " + B);
console.log("\n");

console.log("C <- 2+(3*6)/(2+4)");
console.log("D <- 2*(8/(3+1))");
console.log("E <- 3+(16-2)/(2*(9-2))");
console.log("G <- ((3+(8/2))*4)+(3*2)");
console.log("F <- (6/3)+(8/2)");
console.log("H <- (6*(3*3)+6)-10");
console.log("I <- (((10*8)+3)*9)");
console.log("J <- ((-12)*(-4))+(3*(-4))");

console.log("\n");
console.log("[-- FIM --]");