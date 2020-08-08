import java.util.ArrayList;

public class special_number{

    public static void main(String[] args) {
        
        ArrayList<Integer> result = specialNumbers(1, 22);
        for(int i = 0; i < result.size(); i++){
            System.out.println(result.get(i));
        }
    }

    public static ArrayList<Integer> specialNumbers(int left, int right){
        ArrayList<Integer> arr = new ArrayList<>();
        // code here
        for(int i = left; i <= right; i++){
            //check special number
            Boolean isSpecial = true;
            int num = i;
            while(num > 0){
                int digit = num % 10;
                if(digit == 0 || i % digit != 0){
                    isSpecial = false;
                    break;
                }
                num /= 10;
            }
            if(isSpecial){
                arr.add(i);
            }
        }
        return arr;
    }
    
}