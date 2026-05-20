import java.util.Arrays;
import java.util.Random;
import java.util.Scanner;

public class Boletin_Vectores {
    public static void main(String[] args) {
        //Ejercicio 1
        System.out.println("Ejercicio 1");
        Random r = new Random();
        int[] numeros = new int[6];
        String derecho = "derecho: ";
        for(int i = 0; i<numeros.length; i++){
            numeros[i] = r.nextInt(1,51);
            derecho += numeros[i] + " ";

        }

        String reves = "reves: ";
        for(int i = numeros.length-1; i>=0;i--){
            reves += numeros[i] + " ";
        }

        System.out.println(derecho);
        System.out.println(reves);
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

        System.out.println("Ejercicio 3");
        for(int i = 0; i<notas.length; i++){
            if (notas[i] == notaMasAlta) {
                System.out.println("El alumno con número " + i + 1 + " ha sacado un " + notaMasAlta);
                break;
            }
        }
        Scanner sc = new Scanner(System.in);
        System.out.println("Introduce númeo de aumno para buscar en la lista: ");
        int num = sc.nextInt();
        System.out.println(notas[num-1]);

        Arrays.sort(notas);
        System.out.println("Lista ordenada de notas: ");
        mostrarArray(notas);

        System.out.println("Ejercicio 4");
        //calcular letra DNI
        int dni = 12345678;
        int resto = dni % 23; // %->calcula el resto
        char[] letrasDNI = {'T', 'R', 'W', 'A', 'G', 'M', 'Y', 'F', 'P', 'D', 'X', 'B', 'N', 'J', 'Z', 'S', 'Q', 'V', 'H', 'L', 'C', 'K', 'E'};
        System.out.println("La letra adecuada es: " + letrasDNI[resto]); //uso el indice para sacar la letra

        System.out.println("Ejercicio 5");

        System.out.println("Buscando el numero 5 en este array: ");
        int[] ejercicio5a = {3,6,2,7,9,1};
        mostrarArray(ejercicio5a);
        System.out.println(ejercicio5(ejercicio5a, 5));

        System.out.println("---");

        System.out.println("Ejercicio 6");
        int[] ejercicio6 = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15};
        //Si estuviese descordenada usaria Arrays.sort()
        boolean encontrado = false;
        int numeroAbuscar = 2;
        for(int i = (ejercicio6.length / 2); i < ejercicio6.length; i++) { //empieza a partir de la mitad
            if (ejercicio6[i] == numeroAbuscar) {
                System.out.println("Encontrado en: " + (i+1));
                encontrado = true;
                break;
            }
        }
        if(encontrado == false){ //empieza desde el principio hasta el fin
            for(int i = 0; i < ejercicio6.length / 2 + 1; i++){
                if (ejercicio6[i] == numeroAbuscar) {
                    System.out.println("Encontrado en: " + (i+1));
                    encontrado = true;
                    break;
                }
            }
        }

        if(!encontrado){
            System.out.println("No encontrado");
        }

        System.out.println("Ejercicio 7");
        int[] ejercicio7 = {1,2,3};
        int[] ejercicio7c = ejercicio7(ejercicio7);
        mostrarArray(ejercicio7c);

        System.out.println("Ejercicio 8");
        int[] ejercicio8a = {1,2,3,4,5,6,7};
        mostrarArray(ejercicio8(ejercicio8a)); //2,4,6

        System.out.println("Ejercicio 9");
        int[] ejercicio9a = {1,-12,3,0,5,9,7,1,4};
        mostrarArray(ejercicio9(ejercicio9a));

        System.out.println("Ejercicio 10");
        int[] ejercicio10a = {1,-12,3,0,5,9,7,1,4};
        mostrarArray(ejercicio10(ejercicio10a,3));



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
    private static int ejercicio5(int[] array, int numero){
        //función que recibe un array y busca el numero indicado en el array
        //Si se encuentra devuelve el indice, si no -1

        for(int i = 0; i < array.length; i++){
            if (array[i] == numero){
                return i;
            }
        }
        return -1;
    }

    private static int[] ejercicio7(int[] arrayOriginal) {
        int[] copia = Arrays.copyOf(arrayOriginal, arrayOriginal.length);
        return copia;
    }
    private static int[] ejercicio8(int[] array) {
        int[] pares = new int[array.length];
        int contadorPares = 0;
        for(int i = 0; i < array.length; i++){
            if(array[i] % 2 == 0){ //si al dividir un numero entre 2 no da resto es par
                pares[contadorPares] = array[i];
                contadorPares++;
            }
        }
        //limpiar los ceros del array
        int [] paresArrayLimpio = Arrays.copyOf(pares,contadorPares);
        return paresArrayLimpio;
    }
    private static int[] ejercicio9(int[] arrayOriginal) {
        /*
        Función que devuelve un array sin repeticiones.
        Sería más facil y eficiente usar Arrays.sort para ordenarlo y simplemente comparar un elemento con el anterior para saber si hay repeticiones, pero para conservar y respetar el orden de los elementos no utilizo esta forma
        */
        boolean coincidencia = false;
        int[] arrayLimpio = new int[arrayOriginal.length];
        int contadorLimpio = 0;
        for(int i = 0; i < arrayOriginal.length; i++){
            for(int j = 0; j < arrayOriginal.length; j++){
                if(j!=i){ //para no tener en cuenta la misma posicion
                    if (arrayOriginal[i] == arrayOriginal[j]){
                        coincidencia = true;
                    }
                }
            }
            if (!coincidencia){ //si no hay coincidencia
                arrayLimpio[contadorLimpio] = arrayOriginal[i];
                contadorLimpio++;
            }else{
                coincidencia = false; //reinicia para la siguiente interacción
            }
        }


        int[] arraySinCerosFinales = Arrays.copyOf(arrayLimpio, contadorLimpio);
        return arraySinCerosFinales;
    }
    private static int[] ejercicio10(int[] array, int numero) {
        for(int i = 0; i < array.length; i++){
            if(array[i] == numero){
                array[i] = -99999; //lo marca para eliminar
            }
        }
        int[] array2 = new int[array.length];
        int contadorArray2 = 0;
        for(int i = 0; i < array.length; i++){
            if(!(array[i] == -99999)){
                array2[contadorArray2] = array[i];
                contadorArray2++;
            }
        }
        int[] array3 = Arrays.copyOf(array2, contadorArray2);
        return array3;
    }

}