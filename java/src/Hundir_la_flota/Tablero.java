package Hundir_la_flota;
/*
0 = agua
1 = barco
-1 = barco visitado (tocado)
-2 = agua visitada (agua)
 */

import java.util.Random;

public class Tablero {
    public int[][] tablero;
    private Random rand = new Random();

    public Tablero(int dimension){
        this.tablero = new int[dimension][dimension];
        this.llenarTablero((int) (dimension * 0.9));
    }

    private void llenarTablero(int numeroBarcos){
        // Llenar el tablero con 0's (agua)
        for(int i = 0; i < this.tablero.length; i++){
            for(int j = 0; j < this.tablero[i].length; j++){
                this.tablero[i][j] = 0;
            }
        }

        int barcosColocados = 0;
        while(barcosColocados != numeroBarcos){
            int x = this.rand.nextInt(0, this.tablero.length);
            int y = this.rand.nextInt(0, this.tablero[0].length);

            if(this.tablero[x][y] == 0){ // Si es agua
                this.tablero[x][y] = 1;
                barcosColocados++;
            } // Si ya tiene un barco, vuelve a generar los números aleatorios
        }
    }

    public void imprimirTablero(){
        String linea = "|";

        String lineaBordeSuperiorEInferior = "+";
        for(int i = 0; i < this.tablero.length; i++){
            lineaBordeSuperiorEInferior = lineaBordeSuperiorEInferior + "---+";
        }

        System.out.println(lineaBordeSuperiorEInferior);
        for(int i = 0; i < this.tablero.length; i++){
            for(int j = 0; j < this.tablero[i].length; j++){
                if(this.tablero[i][j] == -1){ // Barco tocado
                    linea = linea + " X |";
                } else if(this.tablero[i][j] == -2) { // Agua disparada
                    linea = linea + " 0 |";
                } else {
                    linea = linea + " - |";
                }
            }
            System.out.println(linea);
            linea = "|";
        }
        System.out.println(lineaBordeSuperiorEInferior);
    }

    public int recibeAtaque(int x, int y) {
        /*
        Función que devuelve uno de estos enteros:
        0 si es agua
        1 si es un barco
        2 si es el último barco (victoria)
        3 si el usuario repite el ataque en la misma posición
        */
        if (this.tablero[x][y] == 0) { // Agua
            this.cambiarPosicion(x, y, -2);
            return 0;

        } else if(this.tablero[x][y] == 1) { // Barco
            this.cambiarPosicion(x, y, -1);
            if(this.barcosRestantes() == 0){
                return 2;
            } else {
                return 1;
            }

        } else { // Si el usuario vuelve a intentar en la misma posición
            return 3;
        }
    }

    public int barcosRestantes(){
        // Muestra los barcos que quedan en el tablero (solo los 1's, no los -1's)
        int barcos = 0;
        for(int i = 0; i < this.tablero.length; i++){
            for(int j = 0; j < this.tablero[i].length; j++){
                if(this.tablero[i][j] == 1){
                    barcos++;
                }
            }
        }
        return barcos;
    }

    private void cambiarPosicion(int x, int y, int nuevoValor){
        // Función que cambia el valor de una posición en el tablero por uno nuevo
        this.tablero[x][y] = nuevoValor;
    }
}
