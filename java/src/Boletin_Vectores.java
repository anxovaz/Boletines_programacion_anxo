import java.util.Random;

public class Boletin_Vectores {
    public static void main(String[] args) {
        System.out.println("Ejercicio 1");
        int[] numeros = new int[6];
        for (int i = 0; i < numeros.length; i++) {
            int number = new Random().nextInt(1, 5);
            numeros[i] = number;

        }
        Boletin_Vectores.mostrarArray(numeros);

        System.out.println("Ejercicio 2");
        int[] notas = new int[30];
        //rellenar el array con notas aleatorias
        for(int i = 0; i < notas.length; i++){
            notas[i] = new Random().nextInt(0, 11); // el 11 no lo incluye
        }
        //calcular aprobados
        int aprobados = 0;
        for(int i = 0; i < notas.length; i++){
            if(notas[i] >= 5){
                aprobados++;
            }
        }
        System.out.println("Número de aprobados: " + aprobados);
        //Calcular nota más alta
        int notaMasAlta = 0;
        for(int i = 0; i < notas.length; i++){
            if(notas[i] > notaMasAlta){
                notaMasAlta = notas[i];
            }
        }
        System.out.println("Nota más alta: " + notaMasAlta);
        //calcular la media
        int suma = 0;
        int media = 0;
        for(int i = 0; i < notas.length; i++){
            suma += notas[i];
        }
        media = suma / notas.length;
        System.out.println("La media es: " + media);



    }
    private static void mostrarArray(int[] array){
        String salida = "";
        for(int i = 0; i<array.length; i++){
            salida = salida + array[i];
            if(i!=array.length-1){
                salida = salida + ", ";
            }
        }
        System.out.println(salida);
    }

}