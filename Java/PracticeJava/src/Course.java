public class Course {
    String id, name;
    Integer numOfStudents = 0;

    Course(String id, String name) {
        this.id = id;
        this.name = name;
    }

    public void addStudent() {
        this.numOfStudents = this.numOfStudents + 1;
    }

    public void minusStudent() {
        if (this.numOfStudents > 0)
            this.numOfStudents = this.numOfStudents - 1;
        else {
            System.out.println("error occurred. initialize numOfStudents by zero.");
            this.numOfStudents = 0;
        }
    }

    public void knowNumOfStudents () {
        System.out.println(this.numOfStudents);
    }
}
