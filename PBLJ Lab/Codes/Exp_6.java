package exp.six;

import java.util.ArrayList;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		ArrayList<String> list = new ArrayList<String>();
		while (true) {
			System.out.println("1. Insert");
			System.out.println("2. Search");
			System.out.println("3. Delete");
			System.out.println("4. Display");
			System.out.println("5. Exit");
			Scanner sc = new Scanner(System.in);
			String str;
			System.out.print("Enter your choice: ");
			int choice = sc.nextInt();
			switch (choice) {
			case 1:
				System.out.print("Enter the item to be inserted: ");
				str = sc.next();
				list.add(str);
				System.out.println("Inserted successfully!");
				break;
			case 2:
				System.out.print("Enter the item to search: ");
				str = sc.next();
				if (list.contains(str))
					System.out.println("Item found in the list.");
				else
					System.out.println("Item not found in the list.");
				break;
			case 3:
				System.out.print("Enter the item to delete: ");
				str = sc.next();
				if (list.contains(str)) {
					list.remove(str);
					System.out.println("Deleted successfully");
				} else
					System.out.println("Item does not exist.");
				break;
			case 4:
				System.out.print("The Items in the list are: ");
				System.out.println(list);
				break;
			case 5:
				System.exit(0);
			}
		}
	}
}