import java.util.ArrayList;
import java.util.Random;

public abstract class PokemonBase implements IPokemon
{
	// Attributes/Properties
	protected String name;
	protected String alternateName;
	protected String type;
	protected int health;
	protected ArrayList<String> attacks;

	public void getName()
	{
		return alternateName.isEmpty() ? name : alternateName;
	}

	// Methods
	public void attack(String attackName)
	{
		if (!attacks.isEmpty())
		{
			if (attacks.contains(attackName))
			{
				System.out.println(getName() + " has used " + attackName);
			}
			else
			{
				System.out.println("Attack " + attackName + " cannot be performed.");
			}
		}
	}

	public void sound(String pokemonSound)
	{
		System.out.println(pokemonSound);
	}

	public void sleep(int sleepingTime)
	{
		System.out.println(getName() " is sleeping!");

		Thread.sleep(sleepingTime);

		System.out.println(getName() " has woke up!");
	}

	public void confused(int confusedTime)
	{
		System.out.println(getName() " is confused!");

		Thread.sleep(sleepingTime);

		System.out.println(getName() " has recovered up!");
	}

	public void faint()
	{
		System.out.println(getName() " has fainted!");
	}

	public void escape()
	{
		System.out.println(getName() " has ran away!");
	}

	public void getCaught()
	{
		Random randomizer = new Random(System.nanoTime());

		if (randomizer.nextFloat() > 0.6)
		{
			System.out.println(getName() " has been caught!");
		}
	}
}