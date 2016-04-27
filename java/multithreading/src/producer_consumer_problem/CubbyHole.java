package producer_consumer_problem;

import java.util.Queue;
import java.util.LinkedList;

/**
 * Created by xili on 4/27/16.
 */
class CubbyHole {
    private Queue<Integer> contents = new LinkedList<Integer>();
    private boolean available = false;

    public synchronized int get() {
        while (available == false) {
            try {
                wait();
            }
            catch (InterruptedException e) {
            }
        }
        available = false;
        notifyAll();
        System.out.println(contents);
        return contents.remove();
    }

    public synchronized void put(int value) {
        while (available == true) {
            try {
                wait();
            }
            catch (InterruptedException e) {
            }
        }
        contents.add(value);
        available = true;
        System.out.println(contents);
        notifyAll();
    }

    public synchronized void showContents() {
//        System.out.println(contents);
    }
}
