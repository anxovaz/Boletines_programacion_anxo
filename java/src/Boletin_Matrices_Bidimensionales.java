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


        System.out.println("Ejercicio 2");
        /*
        Deseña un mapa para un videoxogo que represente habitacións conectadas.
        Para iso crea unha táboa de 3x3 onde cada casiña represente unha habitación.
        Enche a táboa con cadeas que describan os habitáculos, como "Entrada", "Tesouro", "Trampa", etc.
        Permite o usuario elixir unha habitación introducindo a súa fila e columna para descubrir que contén.
        Engade unha condición de vitoria si o usuario encontra o "Tesouro"
         */
        String[][] mapa = {
                {"Entrada", "Pasillo oscuro", "Trampa de flechas"},
                {"Biblioteca", "Sala vacía", "Monstruo durmiendo"},
                {"Foso con agua", "Trampa de pinchos", "Tesouro"}
        };

        // Array de booleanos para llevar el registro de qué habitaciones ya se han descubierto
        boolean[][] descubierto = new boolean[3][3];

        boolean victoria = false;

        System.out.println("¡Bienvenido al explorador de mazmorras!");
        System.out.println("El mapa es de 3x3. Introduce filas y columnas del 0 al 2 para moverte.");
        System.out.println("Tu objetivo es encontrar el 'Tesouro'. ¡Ten cuidado con las trampas!\n");

        // 2. Bucle principal del juego
        while (!victoria) {
            System.out.print("Introduce la fila (0-2): ");
            int fila = sc.nextInt();

            System.out.print("Introduce la columna (0-2): ");
            int columna = sc.nextInt();

            // Validamos que los números estén dentro del rango del array (0, 1 o 2)
            if (fila < 0 || fila > 2 || columna < 0 || columna > 2) {
                System.out.println("Coordenadas inválidas. Recuerda que el mapa es de 3x3 (índices del 0 al 2).\n");
                continue; // Vuelve al principio del bucle sin ejecutar el resto
            }

            // Obtenemos el contenido de la habitación seleccionada
            String habitacion = mapa[fila][columna];
            descubierto[fila][columna] = true;

            if (habitacion.equals("Tesoro")) {
                victoria = true;
                System.out.println("Has encontrado el tesoro");
            } else if (habitacion.startsWith("Trampa") || habitacion.equals("Monstruo durmiendo")) {
                System.out.println("Esta habitacion parece peligrosa...");
            } else {
                System.out.println("Parece seguo");
            }

        }

        System.out.println("Ejercicio 3");
        /*
        Dado un menú dun restaurante, con varios primeiros pratos, segundos e sobremesas:
        Crear a función que permita mostrar o menú os comentáis.
        Deseñar a función que Permita o usuario facer un pedido  devoltanto o resultado nun array con primeiro, segundo e sobremesa.

         */
        String[][] menu = {
                {"Ensalada César", "Crema de calabaza"},
                {"Filete", "Salmón"},
                {"Flan", "Tarta"}
        };


        String[] categorias = {"primeros platos", "segundos platos", "postres"};
        String[] fases = {"primer plato", "segundo plato", "postre"};

        //mostrar el menú
        System.out.println("menú del día:");
        for (int i = 0; i < menu.length; i++) {
            System.out.println("\n" + categorias[i]);
            for (int j = 0; j < menu[i].length; j++) {
                // Mostramos j + 1 para que el cliente vea 1, 2, 3... en vez de empezar desde 0
                System.out.println((j + 1) + ". " + menu[i][j]);
            }
        }
        System.out.println("---");



        //crear pedido del usuario
        String[] pedido = new String[3];


        for (int i = 0; i < menu.length; i++) {
            int eleccion = -1;

            // Bucle para obligar al usuario a introducir un número válido dentro del menú
            while (eleccion < 0 || eleccion >= menu[i].length) {
                System.out.print("Elija el número de su " + fases[i] + ": ");
                eleccion = sc.nextInt() - 1; // Restamos 1 para adaptarlo al índice del array (0, 1, 2...)

                if (eleccion < 0 || eleccion >= menu[i].length) {
                    System.out.println("Opción no válida. Por favor, seleccione un número de la lista.");
                }
            }

            // Almacenamos el plato seleccionado directamente en el array del pedido
            pedido[i] = menu[i][eleccion];
        }


        System.out.println("Pedido:");
        System.out.println("Primero: " + pedido[0]);
        System.out.println("Segundo: " + pedido[1]);
        System.out.println("Postre:  " + pedido[2]);


        System.out.println("ejercicio 4");
        /*
        Crea o programa que siga as regras do xogo fundir a frota. As instrucións son:
        Usa unha táboa de tamaño 4x4 para representar o taboleiro.
        Enche o taboleiro colocando algúns barcos (B) en posicións aleatorias e o resto de casiñas con auga (~).
           Mostra o taboleiro o usuario (podes mostrar só agua para ocultar os barcos).
        Pregunta o usuario as coordenadas para "disparar" introducindo a fila e a columna.
        Actualiza o taboleiro mostrando X si o disparo impacta nun barco ou O si falla.
        Finaliza o xogo cando tódolos barcos sexan destruídos.

         */
        System.out.println("Ejecuta el main que hay en el paquete Hundir_la_flota");

    sc.close(); //cerrar entrada teclado
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
