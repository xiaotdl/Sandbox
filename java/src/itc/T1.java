package itc;

/**
 * Created by xili on 4/25/16.
 */
class T1 implements Runnable {
    private Thread t;
    Chat m;
    String[] s1 = { "Hi", "How are you ?", "I am also doing fine!" };

    public T1(Chat m1) {
        this.m = m1;
    }

    public void start ()
    {
        t = new Thread (this, "T1-Xiaotian");
        t.start ();
    }

    public void run() {
        for (int i = 0; i < s1.length; i++) {
            m.Question(t.getName() + ":\n\t" + s1[i]);
        }
    }
}

