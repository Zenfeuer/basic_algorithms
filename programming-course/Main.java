import java.util.ArrayList;
import java.util.Arrays;

class Main
{
	public static void main(String[] args)
	{	
		ArrayList<String> electricAttacks = new ArrayList<String>(
			Arrays.asList("Bolt Strike", "Charge", "Discharge", "Electrify", "Shock Wave", "Thunderbolt"));

		ArrayList<String> grassAttacks = new ArrayList<String>(
			Arrays.asList("Leaf Blade", "Magical Leaf", "Solar Beam", "Vine Whip", "Power Whip"));

		ArrayList<String> waterAttacks = new ArrayList<String>(
			Arrays.asList("Bubble", "Bubble Beam", "Hydro Cannon", "Surf", "Whirlpool"));

		ArrayList<String> fireAttacks = new ArrayList<String>(
			Arrays.asList("Burn Up", "Fire Blast", "Flame Charge", "Incinerate", "Flamethrower", "Heat Wave", "Overheat"));

		ArrayList<String> electricStrongAgainst = new ArrayList<String>(Arrays.asList("Flying", "Water"));
		ArrayList<String> electricWeakAgainst = new ArrayList<String>(Arrays.asList("Ground", "Grass", "Electric", "Dragon"));
		ArrayList<String> electricResistantTo = new ArrayList<String>(Arrays.asList("Flying", "Steel", "Electric"));
		ArrayList<String> electricVulnerableTo = new ArrayList<String>(Arrays.asList("Ground"));

		ArrayList<String> grassStrongAgainst = new ArrayList<String>(Arrays.asList("Ground", "Rock", "Water"));
		ArrayList<String> grassWeakAgainst = new ArrayList<String>(Arrays.asList("Flying", "Poison", "Bug", "Steel", "Fire", "Grass", "Dragon"));
		ArrayList<String> grassResistantTo = new ArrayList<String>(Arrays.asList("Ground", "Water", "Grass", "Electric"));
		ArrayList<String> grassVulnerableTo = new ArrayList<String>(Arrays.asList("Flying", "Poison", "Bug", "Fire", "Ice"));

		ArrayList<String> waterStrongAgainst = new ArrayList<String>(Arrays.asList("Ground", "Rock", "Fire"));
		ArrayList<String> waterWeakAgainst = new ArrayList<String>(Arrays.asList("Water", "Grass", "Dragon"));
		ArrayList<String> waterResistantTo = new ArrayList<String>(Arrays.asList("Steel", "Fire", "Water", "Ice"));
		ArrayList<String> waterVulnerableTo = new ArrayList<String>(Arrays.asList("Grass", "Electric"));

		ArrayList<String> fireStrongAgainst = new ArrayList<String>(Arrays.asList("Bug", "Steel", "Grass", "Ice"));
		ArrayList<String> fireWeakAgainst = new ArrayList<String>(Arrays.asList("Rock", "Fire", "Water", "Dragon"));
		ArrayList<String> fireResistantTo = new ArrayList<String>(Arrays.asList("Bug", "Steel", "Fire", "Grass", "Ice"));
		ArrayList<String> fireVulnerableTo = new ArrayList<String>(Arrays.asList("Ground", "Rock", "Water"));

		System.out.println("Hello World!");
	}
}
