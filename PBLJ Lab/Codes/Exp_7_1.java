package com.campany;

import java.io.File;
import java.io.FileInputStream;
import java.io.ObjectInputStream;
import java.io.Serializable;
import java.util.ArrayList;
import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		int id;
		String name;
		float salary;
		long contact_no;
		String email_id;

		Scanner sc = new Scanner(System.in);
		ArrayList<Employee> arr = new ArrayList<Employee>();

		try {
			File f = new File("C:\\Users\\Hp\\Documents\\CU\\3rd Year\\Semester 5\\PBLJ Lab\\text.txt");
			if (f.exists()) {
				FileInputStream fis = new FileInputStream(f);
				ObjectInputStream ois = new ObjectInputStream(fis);
				arr = (ArrayList<Employee>) ois.readObject();
			}
		} catch (Exception exp) {
			System.out.println(exp);
		}

		boolean flag = true;
		while (flag) {
			System.out.println("\n1. Enter the details.");
			System.out.println("2. Display details.");
			System.out.println("3. Exit.");
			System.out.print("Enter choice: ");
			int choice = sc.nextInt();
			switch (choice) {
			case 1:
				System.out.println("\nEnter the following details to ADD list:-");
				System.out.print("Enter ID: ");
				id = sc.nextInt();
				System.out.print("Enter Name: ");
				name = sc.next();
				System.out.print("Enter Salary: ");
				salary = sc.nextFloat();
				System.out.print("Enter Contact No: ");
				contact_no = sc.nextLong();
				System.out.print("Enter Email-ID: ");
				email_id = sc.next();

				Employee e1 = new Employee(id, name, salary, contact_no, email_id);
				arr.add(e1);

				break;
			case 2:
				for (Employee e : arr) {
					System.out.println(e);
				}
				break;
			case 3:
				System.out.println("Exit Sucessfully!");
				flag = false;
				break;
			default:
				System.out.println("Invalid Choice, Exit Sucessfully!");
				flag = false;
				break;
			}
		}
	}
}

class Employee implements Serializable {
	int id;
	String name;
	float salary;
	long contact_no;
	String email_id;

	public Employee(int id, String name, float salary, long contact_no, String email_id) {
		this.id = id;
		this.name = name;
		this.salary = salary;
		this.contact_no = contact_no;
		this.email_id = email_id;
	}

	public String toString() {
		return ("\nEmployee Details:-\n" + "ID: " + this.id + " Name: " + this.name + " Salary: " + this.salary
				+ " Contact No: " + this.contact_no + " Email-id: " + this.email_id);
	}
}