package itc;

/**
 * Created by xili on 4/25/16.
 */
public class Demo {
    public static void main(String[] args) {
        Chat m = new Chat();
        T1 t1 = new T1(m);
        t1.start();
        T2 t2 = new T2(m);
        t2.start();
    }
}
