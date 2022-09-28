package exp.one;

public class Main {

	public static void main(String[] args) {

		int empno[] = { 1001, 1002, 1003, 1004, 1005, 1006, 1007 };

		String name[] = { "Ashish", "Sushma", "Rahul", "Chahat", "Ranjan", "Suman", "Tanmay" };

		String JoinDate[] = { "01/04/2009", "23/08/2012", "12/11/2008", "29/01/2013", "16/07/2005", "1/1/2000",
		                      "12/06/2006"
		                    };

		char d_code[] = { 'e', 'c', 'k', 'r', 'm', 'e', 'c' };

		String dept[] = { "R&D", "PM", "Acct", "front", "Desk", "Engg", "Manufacturing", "PM" };

		int basic[] = { 20000, 30000, 10000, 12000, 50000, 23000, 29000 };
		int hra[] = { 8000, 12000, 8000, 6000, 20000, 9000, 12000 };
		int it[] = { 3000, 9000, 1000, 2000, 20000, 4400, 10000 };
		String designation = null;
		int da = 0;
		int salary = 0;
		int index = -1;
		int emp = Integer.parseInt(args[0]);

		for (int i = 0; i < empno.length; i++) {
			if (empno[i] == emp) {
				index = i;
			}
		}

		if (index == -1) {
			System.out.println("There is no such employee with Emp Id: " + emp);
		} else {

			char code;
			code = d_code[index];

			switch (code) {
			case 'e':
				designation = "Engineer";
				da = 20000;
				break;
			case 'c':
				designation = "Consultant";
				da = 32000;
				break;
			case 'k':
				designation = "Clerk";
				da = 12000;
				break;
			case 'r':
				designation = "Receptonist";
				da = 15000;
				break;
			case 'm':
				designation = "Manager";
				da = 40000;
				break;
			default:
				designation = "Invalid";
				da = 0;
			}
			salary = basic[index] + hra[index] + da - it[index];
			System.out.println("Emp No" + "    " + "Emp Name" + "   " + "Department" + "     " + "Designation"
			                   + "      " + "Salary");

			System.out.println(empno[index] + "        " + name[index] + "      " + dept[index] + "          "
			                   + designation + "        " + salary);

		}
	}
}