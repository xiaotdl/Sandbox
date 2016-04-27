package multi_producer_consumer_problem;

import java.util.concurrent.BlockingQueue;

/**
 * Created by xili on 4/27/16.
 */
public class Consumer extends Thread{

    private BlockingQueue<Integer> bq;

    public Consumer(BlockingQueue<Integer> bq, String threadName){
        this.bq = bq;
        setName(threadName);
    }

    @Override
    public void run() {
        while(true){
            try {
                Thread.sleep(500);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
            try {
                //take() Retrieves and removes the head of this queue
                //waits if necessary until an element becomes available.
                int data = bq.take();
                System.out.println("Data "+ data +" consumed by "+this.getName() + ", " + bq);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }
}


