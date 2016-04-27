package producer_consumer_problem;

import java.util.ArrayList;

/**
 * Created by xili on 4/27/16.
 */
public class Main {
    public static final int PRODUCT_NUM = 1000;
    public static final int CONSUMER_NUM = 4;

    public static void main(String[] args) {
        // init instances
        CubbyHole c = new CubbyHole();
        Producer p0 = new Producer(c, 0, PRODUCT_NUM);
        ArrayList<Consumer> consumers = new ArrayList<Consumer>();
        for (int i = 0; i < CONSUMER_NUM; i++) {
            consumers.add(new Consumer(c, i, PRODUCT_NUM/CONSUMER_NUM));
        }

        // run
        p0.start();
        for (int i = 0; i < CONSUMER_NUM; i++) {
            consumers.get(i).start();
        }
    }
}
