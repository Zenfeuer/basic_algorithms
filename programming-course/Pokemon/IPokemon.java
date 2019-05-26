public interface IPokemon
{
	public void attack(String attackName, int damage);

	public void sound(String pokemonSound);

	public void sleep(int sleepingTime) throws InterruptedException;

	public void confused(int confusedTime) throws InterruptedException;

	public void faint();

	public void escape();

	public void getCaught();
}