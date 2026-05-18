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
            num = sc.nextInt(); //lee el numero introducido por el usuario
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

        System.out.println("---Ejercicio5---");
        //Programa que lee numeros por teclado hasta el -1, después muestra los numeros de la lista con indice par y los multiplica por 100
        ArrayList<Integer> numeros = new ArrayList<Integer>();
        int num2 = 0;
        System.out.println("Introduce numeros (-1 = salir): ");
        while(true){
            num2 = sc.nextInt();
            if(num2==-1){
                break;
            }
            numeros.add(num2);
        }
        String salida = "Numeros con indice par (x100): ";
        for(int i = 0; i<numeros.size();i++){
            if(i%2==0){ //si al dividirlo entre 2 da de resto 0
                salida += String.valueOf(numeros.get(i) * 100) + " ";
            }
        }
        System.out.println(salida);

        System.out.println("---Ejercicio 6---");
        /*
        Codifica a aplicación que inserte nunha lista un conxunto de números enteiros entre 1 e 10. A partires desta lista crear:
        -Un conxunto cos elementos da lista sen repetir.
        -Un conxunto cos elementos repetidos.
        -Un conxunto cos elementos que só aparecen unha vez (únicos).

         */
        int[] ej6 = {-1,0,5,-1,6,9,6}; //array original
        ArrayList<Integer> noRepetidos = new ArrayList<Integer>();
        ArrayList<Integer> repetidos = new ArrayList<Integer>();
        ArrayList<Integer> unicos = new ArrayList<Integer>();

        //no repetidos y repetidos
        for(int i: ej6){
            if(!noRepetidos.contains(i)){ //si no contiene el numero
                noRepetidos.add(i);
            }else{ //si ya lo contiene
                repetidos.add(i);
            }
        }
        //unicos
        int contador = 0;
        for(int i: ej6){
            for(int j = 0; j<ej6.length;j++){
                if(ej6[j] == i){
                    contador++;
                }
            }
            if(contador == 1){//si sólo se encontró uno
                unicos.add(i);
            }
            contador = 0;
        }

        System.out.println("lista original: ");
        mostrarArray(ej6);
        System.out.println("No repetidos: " + noRepetidos.toString());
        System.out.println("Repetidos: " + repetidos.toString());
        System.out.println("Únicos: " + unicos.toString());


        System.out.println("---Ejercicio 7 y 8---");
        /*
        Implementar un mét0do estático que faga a unión de dous conxuntos de elementos xenéricos.
        A unión é un novo conxunto con tódolos elemento que pertenza, o menos, a un dos dous conxuntos
        Facer o mesmo que o exercicio 7 coa intersección, formada polos elementos comúns os dous conxuntos
         */
        int[] a1 = {1,2,3,4,5};
        int[] a2 = {6,7,8,9,10};
        mostrarArray(ejercicio7(a1,a2));

        System.out.println("---Ejercicio 9---");

        // ArrayList para guardar las temperaturas del día
        ArrayList<Double> temperaturas = new ArrayList<>();

        int opcion = 0;

        while (opcion != 4) {
            System.out.println("1. Nuevo registro");
            System.out.println("2. Listar registros");
            System.out.println("3. Mostrar estatísticas");
            System.out.println("4. Salir");
            System.out.print("Elige una opción: ");
            opcion = sc.nextInt();
            switch (opcion) {
                case 1:
                    // Nuevo registro
                    System.out.print("Introduce temperatura: ");
                    double novaTemp = sc.nextDouble();
                    temperaturas.add(novaTemp);
                    System.out.println("Temperatura registrada correctamente.");
                    break;

                    case 2:
                        // Listar registros
                        if (temperaturas.isEmpty()) { //si no hay datos
                            System.out.println("No hay datos");
                        } else {
                            System.out.println("\nLista de Temperaturas Rexistradas:");
                            for (int i = 0; i < temperaturas.size(); i++) {
                                System.out.println("Lectura " + (i + 1) + ": " + temperaturas.get(i) + " ºC");
                            }
                        }
                        break;
                    case 3:
                        // Mostrar estadísticas
                        if (temperaturas.isEmpty()) {//si no hay datos
                            System.out.println("No hay datos.");
                        } else {
                            double minimo = temperaturas.get(0);
                            double maximo = temperaturas.get(0);
                            double suma = 0;
                            for (double temp : temperaturas) {
                                if (temp < minimo) {
                                    minimo = temp;
                                }
                                if (temp > maximo) {
                                    maximo = temp;
                                }
                                suma += temp;
                            }

                            double promedio = suma / temperaturas.size();
                            System.out.println("\n--- Estatísticas del Día ---");
                            System.out.println("Temperatura Máxima: " + maximo + " ºC");
                            System.out.println("Temperatura Mínima: " + minimo + " ºC");
                            // Mostramos el promedio con dos decimales
                            System.out.printf("Temperatura Promedio: %.2f ºC\n", promedio);
                        }
                        break;
                    case 4:
                        // Salir
                        System.out.println("Saliendo...");
                        break;
                    default:
                        System.out.println("Opción no válida(1-4)");
                    }
                }

        System.out.println("---Ejercicio 10---");
        String[] codigos = new String[100];
        int[] cantidades = new int[100];
        int totalProductos = 0;

        opcion = 0;

        do {
            System.out.println("\n1. Alta\n2. Baja\n4. Ver\n5. Salir");
            opcion = sc.nextInt();
            sc.nextLine();

            switch (opcion) {
                case 1:
                    System.out.print("Codigo (0000): ");
                    String nuevoCodigo = sc.nextLine();

                    if (nuevoCodigo.length() != 4) {
                        System.out.println("Error formato");
                        break;
                    }

                    int indiceAlta = -1;
                    for (int i = 0; i < totalProductos; i++) {
                        if (codigos[i].equals(nuevoCodigo)) {
                            indiceAlta = i;
                            break;
                        }
                    }

                    if (indiceAlta == -1) {
                        if (totalProductos < codigos.length) {
                            codigos[totalProductos] = nuevoCodigo;
                            System.out.print("Cantidad: ");
                            cantidades[totalProductos] = sc.nextInt();
                            totalProductos++;
                            System.out.println("OK");
                        } else {
                            System.out.println("Lleno");
                        }
                    } else {
                        System.out.println("Ya existe");
                    }
                    break;

                case 2:
                    System.out.print("Codigo (0000): ");
                    String borrarCodigo = sc.nextLine();
                    int indiceBaja = -1;

                    for (int i = 0; i < totalProductos; i++) {
                        if (codigos[i].equals(borrarCodigo)) {
                            indiceBaja = i;
                            break;
                        }
                    }

                    if (indiceBaja != -1) {
                        for (int i = indiceBaja; i < totalProductos - 1; i++) {
                            codigos[i] = codigos[i + 1];
                            cantidades[i] = cantidades[i + 1];
                        }
                        totalProductos--;
                        System.out.println("OK");
                    } else {
                        System.out.println("No existe");
                    }
                    break;

                case 4:
                    if (totalProductos == 0) {
                        System.out.println("Vacio");
                    } else {
                        for (int i = 0; i < totalProductos; i++) {
                            System.out.println(codigos[i] + ": " + cantidades[i]);
                        }
                    }
                    break;

                case 5:
                    System.out.println("Fin");
                    break;

                default:
                    System.out.println("Error");
            }
        } while (opcion != 5);




        sc.close(); //cerrar el escaner al terminar el programa
    }




    private static int[] ejercicio7(int[] a1, int[] a2){
        int[] a3 = Arrays.copyOf(a1,a1.length+a2.length);
        int contadorA2 = 0;
        for(int i = a1.length; i<a3.length;i++){
            a3[i] = a2[contadorA2];
            contadorA2++;

        }
        return a3;
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
