package Hundir_la_flota;
public class Partida {
    private int intentosRestantes; // Solo restará 1 intento si el usuario falla
    private int puntos;
    private int disparos;
    public Tablero tablero;

    public Partida(int dimensionTablero){
        this.setPuntos(0);
        this.setDisparos(0);
        this.setIntentosRestantes((int) (dimensionTablero * 1.7));
        tablero = new Tablero(dimensionTablero);
    }

    public String atacar(int x, int y){
        // Devuelve la respuesta del ataque
        int respuesta = this.tablero.recibeAtaque(x, y);
        if(respuesta == 3){ // Si ya se había intentado
            return "Ya has realizado un intento en esta posición"; // Detiene la función aquí
        }

        this.disparos++;
        if(respuesta == 0){ // Si es agua
            this.intentosRestantes -= 1;
            return "¡Agua!";

        } else if (respuesta == 2){ // Si el usuario gana
            this.puntos++;
            return "¡Has ganado la partida!";

        } else { // Si acierta a un barco
            this.puntos++;
            return "¡Tocado! Has golpeado un barco";
        }
    }

    public String mostrarEstadisticas(){
        return "Intentos restantes: " + this.intentosRestantes + "\nDisparos: " + this.disparos + "\nPuntos: " + this.puntos;
    }

    public void mostrarTablero(){
        this.tablero.imprimirTablero();
    }

    // Getters y Setters traducidos
    public int getPuntos(){
        return this.puntos;
    }
    public int getDisparos(){
        return this.disparos;
    }
    public int getIntentosRestantes(){
        return this.intentosRestantes;
    }
    public void setPuntos(int nuevosPuntos){
        this.puntos = nuevosPuntos;
    }
    public void setDisparos(int nuevosDisparos){
        this.disparos = nuevosDisparos;
    }
    public void setIntentosRestantes(int nuevosIntentos){
        this.intentosRestantes = nuevosIntentos;
    }
}
