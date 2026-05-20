package Hundir_la_flota;

import java.util.Scanner;

public class Main {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in); // Usamos 'sc' como en los ejercicios anteriores
        System.out.println("Introduce la dimensión del Tablero: ");
        int dimensionTablero = sc.nextInt();
        Partida partida1 = new Partida(dimensionTablero);

        while(true){
            if (partida1.getIntentosRestantes() == 0) {
                System.out.println("Has perdido. Te has quedado sin intentos.");
                break;
            }

            partida1.mostrarTablero();
            System.out.println("¿Qué deseas hacer:\n1. Mostrar estadísticas\n2. Realizar un disparo\n3. Salir");
            int entradaUsuario = sc.nextInt();

            if(entradaUsuario == 1){
                System.out.println(partida1.mostrarEstadisticas());
                // Accedemos a 'tablero' y al mét0do 'barcosRestantes()' traducidos
                System.out.println("Barcos restantes en el mar: " + partida1.tablero.barcosRestantes());

            } else if(entradaUsuario == 2){
                System.out.println("Introduce la coordenada X:");
                int x = sc.nextInt();
                System.out.println("Introduce la coordenada Y:");
                int y = sc.nextInt();

                // Llamamos al método 'atacar' con los nuevos mensajes en español
                String respuesta = partida1.atacar(x, y);
                System.out.println(respuesta);

                // Modificado para que coincida con la condición de victoria en español
                if(respuesta.equals("¡Has ganado la partida!")){
                    System.out.println("Tus estadísticas finales: \n" + partida1.mostrarEstadisticas());
                    break;
                }

            } else {
                System.out.println("Saliendo del juego...");
                break;
            }

            System.out.println("-------------------------------------------");
        }

        sc.close();
    }
}