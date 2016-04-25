package synchronization;

/**
 * Created by xili on 4/25/16.
 */
class PrintCount {
    public void run(){
        try {
            for(int i = 5; i > 0; i--) {
                System.out.println("Counter   ---   "  + i );
            }
        } catch (Exception e) {
            System.out.println("Thread  interrupted.");
        }
    }

}
