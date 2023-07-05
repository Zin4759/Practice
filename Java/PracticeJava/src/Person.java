public class Person {
    String name;
    Phone phone;
    Phone homePhones, officePhone;
    Person(String name) {
        this.name = name;
        this.phone = new Phone(this.name);
        this.homePhones = new Phone(this.name);
        this.officePhone = new Phone(this.name);
    }

    public void printPhoneId() {
        System.out.println(this.phone.id);
    }

    public void printUser(Phone phone) {
        phone.printUser();
    }
    public void printId(Phone phone) {
        phone.printId();
    }
}
