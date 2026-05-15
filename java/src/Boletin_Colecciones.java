import java.util.ArrayList;

import java.util.Random;

public class Boletin_Colecciones {
    public static void main(String[] args){

        //Ejercicios 2 y 3
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




        System.out.println(list);

    }
}
