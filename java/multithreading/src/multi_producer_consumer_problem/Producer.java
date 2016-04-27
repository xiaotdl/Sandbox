package multi_producer_consumer_problem;

import java.util.Random;
import java.util.concurrent.BlockingQueue;

/**
 * Created by xili on 4/27/16.
 */
public class Producer extends Thread{

    private BlockingQueue<Integer> bq;
    private Random random;

    public Producer(BlockingQueue<Integer> bq, String threadName){
        this.bq = bq;
        setName(threadName);
        random = new Random();
    }

    @Override
    public void run() {
        while(true){
            try {
                Thread.sleep(500);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
            int data = random.nextInt(100);
            try {
                //Inserts the specified element into this queue
                //waits if necessary for space to become available.
                bq.put(data);
                System.out.println("Data "+ data +" produced by "+this.getName() + ", " + bq);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }
}
