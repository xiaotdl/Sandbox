package producer_consumer_problem;

/**
 * Created by xili on 4/27/16.
 */
class Producer extends Thread {
    private CubbyHole cubbyhole;
    private int number;
    private int product_number;

    public Producer(CubbyHole c, int number, int product_number) {
        this.cubbyhole = c;
        this.number = number;
        this.product_number = product_number;
    }

    public void run() {
        for (int i = 0; i < this.product_number; i++) {
            this.cubbyhole.put(i);
            System.out.println("Producer #" + this.number
                    + " put: " + i);
            this.cubbyhole.showContents();
            try {
                sleep((int)(Math.random() * 100));
            } catch (InterruptedException e) { }
        }
    }
}
