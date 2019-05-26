public interface IPokemon
{
	public void attack(String attackName);

	public void sound(String pokemonSound);

	public void sleep(int sleepingTime);

	public void confused(int confusedTime);

	public void faint();

	public void escape();

	public void getCaught();
}