import java.util.ArrayList;
import java.util.Random;

public class Pokemon extends PokemonBase
{
	protected Pokemon nextEvolution;
	protected ArrayList<String> strongAgainst;
	protected ArrayList<String> weakAgainst;
	protected ArrayList<String> resistantTo;
	protected ArrayList<String> vulnerableTo;

	public Pokemon(String name, String altName, String type, int health,
		ArrayList<String> attacks, ArrayList<String> strongAgainst,
		ArrayList<String> weakAgainst, ArrayList<String> resistantTo,
		ArrayList<String> vulnerableTo)
	{
		this.name = name;
		this.alternateName = altName;
		this.type = type;
		this.attacks = attacks;
		this.strongAgainst = strongAgainst;
		this.weakAgainst = weakAgainst;
		this.resistantTo = resistantTo;
		this.vulnerableTo = vulnerableTo;
		this.fainted = false;

		this.setHealth(health);
	}

	public void fight(Pokemon enemy)
	{
		Random randomizer = new Random(System.nanoTime());
		int rounds = randomizer.nextInt(5) + 5;

		boolean isMyTurn = true;

		while (rounds > 0)
		{
			if (isMyTurn)
			{
				
			}

		}
	}

	public void getAttacked(int damage, String enemyType)
	{
		Random randomizer = new Random(System.nanoTime());
		int trueDamage;

		if (resistantTo.contains(enemyType))
		{
			trueDamage = randomizer.nextInt(5);
			System.out.println(getName() + " has been attacked. It is not effective. Loses " + trueDamage + " HP.");
		}
		else if (vulnerableTo.contains(enemyType))
		{
			trueDamage = 5 + randomizer.nextInt(damage);
			System.out.println(getName() + " has been attacked. It is effective. Loses " + trueDamage + " HP.");
		}
		else
		{
			trueDamage = damage/4;
			System.out.println(getName() + " has been attacked. Loses " + trueDamage + " HP.");
		}

		reduceHealth(damage);
	}
}