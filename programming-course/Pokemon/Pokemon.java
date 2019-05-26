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
		System.out.println("-------------------------------------------------------");
		System.out.println();

		System.out.println("Match: " + this.getName() + " vs " + enemy.getName());
		System.out.println();

		Random randomizer = new Random(System.nanoTime());
		int rounds = randomizer.nextInt(10) + 10;
		int attackIndex;
		int damage;

		boolean isMyTurn = true;
		String winner = "";

		while (rounds > 0)
		{
			damage = randomizer.nextInt(150) + 1;

			if (isMyTurn)
			{
				System.out.println();
				System.out.println(">" + this.getName() + " turn:");
				System.out.println();

				attackIndex = randomizer.nextInt(this.attacks.size()-1);

				this.attack(this.attacks.get(attackIndex), damage);
				enemy.getAttacked(damage, this.type);

				if (enemy.fainted)
				{
					winner = this.getName();
					break;
				}
			}
			else
			{
				System.out.println();
				System.out.println(">" + enemy.getName() + " turn:");
				System.out.println();

				attackIndex = randomizer.nextInt(enemy.attacks.size()-1);

				enemy.attack(enemy.attacks.get(attackIndex), damage);
				this.getAttacked(damage, enemy.type);

				if (this.fainted)
				{
					winner = enemy.getName();
					break;
				}
			}

			isMyTurn = !isMyTurn;
			rounds--;
		}

		if (!winner.isEmpty())
		{
			System.out.println();
			System.out.println("THE WINNER IS: " +  winner);
		}
		else
		{
			System.out.println();
			System.out.println("TIE!");
		}

		System.out.println("Fight finished!");
		System.out.println();
		System.out.println("-------------------------------------------------------");
		System.out.println();
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
			trueDamage = 5 + randomizer.nextInt(damage*2);
			System.out.println(getName() + " has been attacked. It is effective. Loses " + trueDamage + " HP.");
		}
		else
		{
			trueDamage = damage/4;
			System.out.println(getName() + " has been attacked. Loses " + trueDamage + " HP.");
		}

		reduceHealth(trueDamage);
	}
}