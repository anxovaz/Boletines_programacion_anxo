import java.util.Scanner;

public class Boletin_Matrices_Bidimensionales {
    public static void main(String[] args){
        System.out.println("Ejercicio 1");
        /*
        Deseña o programa que permita organizar a túa axenda. Para iso o programa ten que posibilitar:
Crear unha táboa (bidimensional) onde as filas sexan días da semán e as columnas as horas do día.
Enche a táboa con cadeas que representen actividades, por exemplo: "Matemáticas", "Historia", "Deporte", “Compra”, “Piscina”.
Mostra o horario inicial o usuario.
Permite o usuario:
Cambiar unha actividade por outra.
Engadir unha actividade extra nunha posición valeira.
     e)Mostra o horario actualizado tras cada modificación.

         */
        String[][] agenda = new String[7][2];
        //Días de la semana
        agenda[0][0] = "Lunes";
        agenda[1][0] = "Martes";
        agenda[2][0] = "Miércoles";
        agenda[3][0] = "Jueves";
        agenda[4][0] = "Viernes";
        agenda[5][0] = "Sábado";
        agenda[6][0] = "Domingo";
        //Actividades
        agenda[0][1] = "Matemáticas";
        agenda[1][1] = "Plástica";
        agenda[2][1] = "E.Física";
        agenda[3][1] = "Biología";
        agenda[4][1] = "Historia";
        agenda[5][1] = "";
        agenda[6][1] = "";

        //Instancia scanner
        Scanner sc = new Scanner(System.in);

        //Menú
        boolean bucle1 = true;
        while(bucle1){
            mostrarArrayBidimensional(agenda);
            System.out.println("Selecciona una opción:\n1.Cambiar actividad\n2.Añadir actividad\n3.Salir");
            int opcion = sc.nextInt();
            switch (opcion){
                case 1:
                    System.out.println("introduce día:");
                    String dia = sc.next();
                    System.out.println("Introduce actividad:");
                    String actividad = sc.next();
                    int indice = getIndiceArrayBidimensional(dia,agenda);
                    if(indice == -1){
                        //si no se encuentra día
                        System.out.println("Error, día incorrecto");
                    }else {
                        agenda[indice][1] = actividad;
                    }
                    break; //cierra el switch case, no el while infinito
                case 2:
                    mostrarVaciosBidimennsional(agenda);
                    System.out.println("Introduce indice de uno de los días sin actividades:");
                    int indiceAanhadir = sc.nextInt();
                    System.out.println("Indica la actividad: ");
                    String actividadNueva = sc.next();
                    agenda[indiceAanhadir][1] = actividadNueva;
                    break;
                case 3:
                    System.out.println("Saliendo...");
                    bucle1 = false;



            }

        }
    }
    public static void mostrarArrayBidimensional(String[][] array){
        for(int i = 0; i<array.length; i++){
            System.out.println(array[i][0] + ": " + array[i][1]);

        }
    }
    public static int getIndiceArrayBidimensional(String valor, String[][] array){
        for(int i = 0; i<array.length;i++){
            if(array[i][0].compareTo(valor) == 0){ //si se encuentra
                return i;
            }
        }
        return -1;//si no se encuentra
    }
    public static void mostrarVaciosBidimennsional(String[][] array){
        //función que sólo muestra los días que tienen actividades vacías
        for(int i = 0; i<array.length; i++){
            if(array[i][1].compareTo("")==0){//si está vacio
                System.out.println(i + " -> " + array[i][0] + ": " + array[i][1]);
            }

        }
    }
}
