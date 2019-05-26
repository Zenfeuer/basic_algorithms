import java.util.ArrayList;
import java.util.Random;

public abstract class PokemonBase implements IPokemon
{
	// Attributes/Properties
	protected String name;
	protected String alternateName;
	protected String type;
	private int health;
	protected boolean fainted;
	protected ArrayList<String> attacks;

	public String getName()
	{
		return alternateName.isEmpty() ? name : alternateName;
	}

	public void setHealth(int health)
	{
		this.health = health;
	}

	public void reduceHealth(int damage)
	{
		health -= damage;

		if (health <= 0)
		{
			health = 0;
			fainted = true;
			faint();
		}

		System.out.println(getName() + " health: " + health);
	}

	// Methods
	public void attack(String attackName, int damage)
	{
		if (!attacks.isEmpty())
		{
			if (attacks.contains(attackName))
			{
				System.out.println(getName() + " has used " + attackName + ". [Estimated dmg: " + damage + "]");
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

	public void sleep(int sleepingTime) throws InterruptedException
	{
		System.out.println(getName() + " is sleeping!");

		Thread.sleep(sleepingTime);

		System.out.println(getName() + " has woke up!");
	}

	public void confused(int confusedTime) throws InterruptedException
	{
		System.out.println(getName() + " is confused!");

		Thread.sleep(confusedTime);

		System.out.println(getName() + " has recovered up!");
	}

	public void faint()
	{
		System.out.println(getName() + " has fainted!");
	}

	public void escape()
	{
		System.out.println(getName() + " has ran away!");
	}

	public void getCaught()
	{
		Random randomizer = new Random(System.nanoTime());

		if (randomizer.nextFloat() > 0.6)
		{
			System.out.println(getName() + " has been caught!");
		}
		else
		{
			System.out.println(getName() + " has NOT been caught!");
		}
	}

	public abstract void getAttacked(int damage, String enemyType);
}