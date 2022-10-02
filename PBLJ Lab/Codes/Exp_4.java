package exp.four;

import java.util.HashMap;
import java.util.Hashtable;

public class Main {

	public static void main(String[] args) {
		HashMap<String, Integer> map1 = new HashMap<>();
		map1.put("Yash", 1001);
		map1.put("Rahul", 1002);
		// The value is updated if same key is used again
		map1.put("Rahul", 1002);
		map1.put("Raj", 1004);
		map1.put("Ravi", 1009);
		map1.put("Ramu", 1010);

		HashMap<Integer, String> map2 = new HashMap<>();
		map2.put(0, "A");
		map2.put(1, "B");
		map2.put(2, "C");
		map2.put(3, "D");

		// Searching key using contains Key
		if (map1.containsKey("Rahul")) {
			System.out.println("'Rahul' as Key is present in the map");
		} else {
			System.out.println("'Rahul' as Key is not present in the map");
		}

		// For getting value of the key
		System.out.println("\nValues for key Rahul: " + map1.get("Rahul"));
		// Printing the map
		System.out.println("\nmap1: " + map2);
		System.out.println("map2: " + map2);

		System.out.println("\nmap1 == map2 : " + map1.equals(map2));

		System.out.println("\nSize of map1: " + map1.size());
		map1.clear();
		System.out.println("After clearing map1, isEmpty: " + map1.isEmpty());

		// Hashtable
		Hashtable<Integer, String> hash = new Hashtable<Integer, String>();
		hash.put(1, "ABBA");
		hash.put(2, "BBBB");
		System.out.println("\nHashtable:-");
		hash.forEach((key, value) -> System.out.println("Rank: " + key + " | Name: " + value));

		System.out.println("\nSize of hashtable: " + hash.size());
		System.out.println("Whether the hashtable is empty: " + hash.isEmpty());

		// Null as key Value
		try {
			hash.put(null, "ACAC");
		} catch (Exception e) {
			System.out.println();
			System.out.println(e);
		} finally {
			System.out.println("hash: " + hash);
		}
	}
}