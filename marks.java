import java.util.Scanner;
class Marks_3{
	public static void main (String args[]){
		int z=100;
		Scanner scan=new Scanner(System.in);
		System.out.println("Please enter the number of subjects ");
		int j = scan.nextInt();
		
		int marks[];
		marks = new int[j];
		
		int i=0;
		int total=0;
		
		while(i<j){
			System.out.println("Please enter the marks of subject "+ (i+1));
			marks[i] = scan.nextInt();
			total=total+marks[i];
			i++;
		}
		
		double average=total/j;
		
		char rank='x';
		
		if (average>100||average<0) {
			System.out.println("Invalid inputs");
		}
		else if (average>75){ //checking average
			rank='A';
		}
		else if (average>65){
			rank='B';
		}
		else if (average>55){
			rank='C';
		}
		else if (average>45){
			rank='S';
		}
		else {
			rank='F';
		}
		
		do{
			if (average>100||average<0) {
				break;
			}
			else{
				System.out.println("Your total marks is "+total);
				System.out.println("Your average is "+average);
				System.out.println("Your rank is "+rank);//print rank as char
			}
		}
		while(z<10);
	}
}