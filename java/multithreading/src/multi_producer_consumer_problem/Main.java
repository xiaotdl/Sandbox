package multi_producer_consumer_problem;

import java.util.ArrayList;
import java.util.concurrent.ArrayBlockingQueue;

/**
 * Created by xili on 4/27/16.
 */
public class Main {

    public static final int PRODUCER_NUM = 5;
    public static final int CONSUMER_NUM = 2;

    public static void main(String[] args) {
        // init instances
        ArrayBlockingQueue<Integer> bq = new ArrayBlockingQueue<>(10);

        ArrayList<Producer> producers = new ArrayList<Producer>();
        for (int i = 0; i < PRODUCER_NUM; i++) {
            producers.add(new Producer(bq, "Producer " + Integer.toString(i)));
        }

        ArrayList<Consumer> consumers = new ArrayList<Consumer>();
        for (int i = 0; i < CONSUMER_NUM; i++) {
            consumers.add(new Consumer(bq, "Consumer " + Integer.toString(i)));
        }

        // run
        for (int i = 0; i < PRODUCER_NUM; i++) {
            producers.get(i).start();
        }
        for (int i = 0; i < CONSUMER_NUM; i++) {
            consumers.get(i).start();
        }
    }
}
