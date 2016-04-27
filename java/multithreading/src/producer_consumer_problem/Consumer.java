package producer_consumer_problem;

/**
 * Created by xili on 4/27/16.
 */
class Consumer extends Thread {
    private CubbyHole cubbyhole;
    private int number;
    private int product_number;
    public Consumer(CubbyHole c, int number, int product_number) {
        cubbyhole = c;
        this.number = number;
        this.product_number = product_number;
    }
    public void run() {
        int value = 0;
        for (int i = 0; i < this.product_number; i++) {
            value = cubbyhole.get();
            System.out.println("Consumer #"
                    + this.number
                    + " got: " + value);
        }
    }
}
