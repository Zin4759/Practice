public class Phone {
    String user = "";
    String id = "A99999";

    Phone(String user) {
        this.user = user;
    }

    public void printId() {
        System.out.println(this.id);
    }
    public void printUser() {
        System.out.println(this.user);
    }
}
