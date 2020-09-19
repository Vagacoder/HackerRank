package practice.Robox;

import java.util.*;

public class Rob02 {


    public static String compressWord(String word, int k) {

        int n = word.length();
        if(n <=1 || n < k){
            return word;
        }
        int i = 0;
        boolean found = false;
        Outer:
        for(; i <= n - k; i++){
            int count = 0;
            for(int j = i+1; j < i+k; j++){
                if(word.charAt(j) != word.charAt(i)){
                    if(found){
                        break Outer;
                    }else{
                        break;
                    }
                }else{
                    count++;
                    if(count >=k){
                        found = true;
                    }
                }
            }
        }
        if (found){
            String shortWord1 = word.substring(0, i);
            if(i+k < n){
                String shortWord2 = word.substring(i+k, n);
                shortWord1 += shortWord2;
            }
            return compressWord(shortWord1, k);
        }
        return word;
    }





    public static void main(String[] args){

        String word1 = "abbcccb";
        String re1 = compressWord(word1, 3);

        System.out.println(re1);

    }
    
}
