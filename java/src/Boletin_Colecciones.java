import java.util.*;

public class Boletin_Colecciones {
    public static void main(String[] args){
        //Ejercicio 1
        System.out.println("---Ejercicio 1---");
        String[] array1 = {"Hola", "adios"};
        String[] array2 = {"Buenas", "chao"};

        mostrarArray(ejercicio1(array1, array2));

        System.out.println("---Ejercicios 2 y 3---");
        ArrayList<Integer> list = new ArrayList<>();
        int counter = 0;
        while (counter < 1000){
            Random r = new Random();
            int number = r.nextInt(1,11); // el 11 no lo recoge
            list.add(number);
            counter++;
        }
        System.out.println(list);

        //recorrer la lista
        for(int i = 0; i<list.size(); i++){
            if(list.get(i) == 5 | list.get(i) == 7){
                list.remove(list.get(i));
                //al eliminar un elemento la lista se hace mas pequeña pero i sigue siendo el mismo al eliminar
                //por lo cual si hay 2 cincos o sietes juntos solo se eliminará el primero
                /*

                Antes de eliminar:
                lista = 1, 4, 4, 2, 5, 5, 1, 8, 1
                        0  1  2  3  4  5  6  7  8      i = 4

                Despues de eliminar:
                lista = 1, 4, 4, 2, 5, 1, 8, 1
                        0  1  2  3  4  5  6  7       i = 4 Aumentará en 1 e valor en la siguente iteración del bucle, por lo cual saltaría al indece 5 (1) sin pasar por el anterior

                 */
                i--;
            }
        }

        //iterator
        ListIterator<Integer> listIterator = list.listIterator();
        while(listIterator.hasNext()){
            int i = listIterator.next();
            if(list.get(i) == 5 | list.get(i) == 7) {
                list.remove(list.get(i));
            }
        }

        System.out.println(list);



        System.out.println("---Ejercicio 4---");
        Scanner sc = new Scanner(System.in);
        //Programa que lee los numeros por teclado y mete los positivos en el arrayList 'positivos' y los negativos en el 'negativos'
        ArrayList<Integer> positivos = new ArrayList<Integer>();
        ArrayList<Integer> negativos = new ArrayList<Integer>();
        int num = 0;
        while(true) {
            System.out.println("introduce un número (0 = salir): ");
            num = sc.nextInt();
            if (num > 0) {
                positivos.add(num);
            } else if (num < 0) {
                negativos.add(num);
            } else { //si es 0
                break;
            }
        }
        System.out.println(positivos.toString());
        System.out.println(negativos.toString());

    }

    private static String[] ejercicio1(String[] a1, String[] a2){
        String[] a3 = Arrays.copyOf(a1, (a1.length + a2.length));
        int contadorA2 = 0;
        for(int i = a1.length; i<a3.length; i++){
            a3[i]=a2[contadorA2];
            contadorA2++;
        }
        return a3;

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
    private static void mostrarArray(String[] array){
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
