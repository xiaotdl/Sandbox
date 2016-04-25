package basic;

/**
 * Created by xili on 4/25/16.
 */
// Create a thread to implement Runnable
public class DisplayMessage implements Runnable
{
    private String message;
    public DisplayMessage(String message)
    {
        this.message = message;
    }
    public void run()
    {
        while(true)
        {
            System.out.println(message);
            // Let the thread sleep for a while.
            try {
                Thread.sleep(1);
            } catch (InterruptedException e) {
                System.out.println("Thread " +  "basic.DisplayMessage" + message + " interrupted.");
            }
        }
    }
}
