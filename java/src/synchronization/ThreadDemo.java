package synchronization;

/**
 * Created by xili on 4/25/16.
 */
class ThreadDemo extends Thread {
    private Thread t;
    private String threadName;
    PrintCount pc;

    ThreadDemo( String name,  PrintCount pc){
        this.threadName = name;
        this.pc = pc;
    }
    public void run() {
        synchronized(this.pc) {
            this.pc.run();
        }
        System.out.println("Thread " +  threadName + " exiting.");
    }

    public void start ()
    {
        System.out.println("Starting " +  threadName );
        if (t == null)
        {
            t = new Thread (this, threadName);
            t.start ();
        }
    }

    public static void main(String args[]) {

        PrintCount PD = new PrintCount();

        ThreadDemo T1 = new ThreadDemo( "Thread - 1 ", PD );
        ThreadDemo T2 = new ThreadDemo( "Thread - 2 ", PD );

        T1.start();
        T2.start();

        // wait for threads to end
        try {
            T1.join();
            T2.join();
        } catch( Exception e) {
            System.out.println("Interrupted");
        }
    }

}

