import java.util.*;

// Download jar from: https://github.com/google/gson
import com.google.gson.Gson;

public class TestOrderedSerialization {

    public static void main(String[] args) {
        Map<String, String> orderedMap = new LinkedHashMap<String, String>();

        orderedMap.put("4","white");
        orderedMap.put("2","blue");
        orderedMap.put("3","green");
        orderedMap.put("1","red");

        String gson = new Gson().toJson(orderedMap);
        System.out.println("gson: " + gson.toString());
        // >>>
        // gson: {"4":"white","2":"blue","3":"green","1":"red"}
    }

}
