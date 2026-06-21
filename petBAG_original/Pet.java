package projectOne;

// Pet.java

/********************
 * IT-145 4-3 Project One
 * Pet.java
 * 
 * Nicholas Shaner
 * SNHU
 * IT-145-X3343 Found in App Development 23EW3
 * Dr. Vivian Lyon
 * February 4, 2024
 * 
 * ******************/

public class Pet {
	/*
	 * The following are instance field variables, 
	 * specific to the Pet class
	 */
	private String petType;
	private String petName;
	private int petAge;
	private int dogSpaces;
	private int catSpaces;
	private int daysStay;
	private double amountDue;
	
	/*
	 * These are the constructors for the Pet class
	 */
	public Pet(String petType, String petName, int petAge, int daysStay, double amountDue) {
		this.petType = petType;
		this.petName = petName;
		this.petAge = petAge;
		this.daysStay = daysStay;
		this.amountDue = 0.0;
	}
	
	/*
	 * These are the mutators of the Pet class
	 */
	public void setPetType(String petType) {
		this.petType = petType;
	}
	public void setPetName(String petName) {
		this.petName = petName;
	}
	public void setPetAge(int petAge) {
		this.petAge = petAge;
	}
	public void setDogSpaces(int dogSpaces) {
		this.dogSpaces = dogSpaces;
	}
	public void setCatSpaces(int catSpaces) {
		this.catSpaces = catSpaces;
	}
	public void setDaysStay(int daysStay) {
		this.daysStay = daysStay;
	}
	public void setAmountDue (double amountDue) {
		this.amountDue = amountDue;
	}
	
	/*
	 * These are the accessors for the Pet class
	 */
	public String getPetType() {
		return petType;
	}
	public String getPetName() {
		return petName;
	}
	public int getPetAge() {
		return petAge;
	}
	public int getDogSpaces() {
		return dogSpaces;
	}
	public int getCatSpaces() {
		return catSpaces;
	}
	public int getDaysStay() {
		return daysStay;
	}
	public double getAmountDue() {
		return amountDue;
	}
	
}