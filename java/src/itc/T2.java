package itc;

/**
 * Created by xili on 4/25/16.
 */
class T2 implements Runnable {
    private Thread t;
    Chat m;
    String[] s2 = { "Hi", "I am good, what about you?", "Great!" };

    public T2(Chat m2) {
        this.m = m2;
    }

    public void start ()
    {
        t = new Thread (this, "T2-Wendi");
        t.start ();
    }

    public void run() {
        for (int i = 0; i < s2.length; i++) {
            m.Answer(t.getName() + ":\n\t" + s2[i]);
        }
    }
}
