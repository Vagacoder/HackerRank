package practice.Robox;

import java.util.*;

public class Rob01 {
    
    public static int numPlayers(int k, List<Integer> scores) {
        // Write your code here
        int n = scores.size();

        Collections.sort(scores);

        int[] ranks = new int[n];
        ranks[n-1] = 1;

        int rank = 2;
        for(int i = n-2; i >=0; i--){
            if(scores.get(i) == scores.get(i+1)){
                ranks[n-1-i] = ranks[i+1];
                rank++;
            }else{
                ranks[n-1-i] = rank++;
            }
        }

        // for(int i = 0; i < n; i++){
        //     System.out.println(ranks[i]);
        // }

        int count = 0;
        for(int index = 0; index< n; index++){

            if(ranks[index]>k){
                return index;
            }else{
                count++;
            }
            if(count >k){
                return count;
            }
        }


        return n;
    }



    public static void main(String[] args){

        List<Integer> scores1 = new ArrayList<>();
        scores1.add(100);
        scores1.add(50);
        scores1.add(50);
        scores1.add(25);

        System.out.println(numPlayers(3, scores1));

    }
}
