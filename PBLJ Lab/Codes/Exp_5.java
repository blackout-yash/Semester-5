package exp.five;

import java.util.Arrays;
import java.util.HashSet;
import java.util.Iterator;
import java.util.Set;

public class Main {

	public static void main(String[] args) {
		Set<Integer> s1 = new HashSet<Integer>();
		s1.add(4);
		s1.add(2);
		s1.add(1);
		s1.add(1);
		s1.add(5);

		Integer[] arr = { 7, 1, 2, 3, 1, 5 };
		Set<Integer> s2 = new HashSet<Integer>();
		s2.addAll(Arrays.asList(arr));

		System.out.println("s1: " + s1);
		System.out.println("s2: " + s2);

		System.out.println("\ns1 == s2: " + s1.equals(s2));

		Set<Integer> union = new HashSet<Integer>(s1);
		union.addAll(s2);
		System.out.println("\nUnion of s1 & s2: " + union);

		System.out.println("\nRemove 2 from set s1.");
		s1.remove(2);
		System.out.println("s1: " + s1);

		Iterator newData = s1.iterator();
		System.out.println("\nPrinting values using Iteratore!");
		System.out.print("s1: ");
		while (newData.hasNext()) {
			System.out.print(newData.next() + " ");
		}

		System.out.println("\n\nSize of s2: " + s2.size());
		System.out.println("Clearing elemets from s2!");
		s2.clear();
		System.out.println("Whether set2 is empty: " + s2.isEmpty());
	}

}
