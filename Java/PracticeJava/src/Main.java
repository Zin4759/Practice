public class Main {
    public static void main(String[] args) {
        Person person1 = new Person("unknown");
        /*
        person1.phone.printId(); //good because this code is sample
        person1.printPhoneId(); //wrong code
        */

        person1.homePhones.printUser();
        person1.homePhones.printId();
        person1.officePhone.printUser();
        person1.officePhone.printId();

        Person person2 = new Person("harry");
        person2.homePhones.printUser();
        person2.homePhones.printId();
        person2.officePhone.printUser();
        person2.officePhone.printId();
    }
}