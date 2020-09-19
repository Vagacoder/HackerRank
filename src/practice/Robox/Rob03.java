package practice.Robox;

import java.util.*;

public class Rob03 {


    public static int largestSubgrid(List<List<Integer>> grid, int maxSum) {
        int n = grid.size();

        HashMap<Integer, Integer> maxSums = new HashMap<>();

        for(int size = 1; size < n; size++){
            int step = n - size + 1;
            int maxSizeSum = 0;
            for(int i = 0; i < step; i++){
                for(int j =0; j < step; j++){
                    int curSum = sum(grid, i, j, size);
                    if(curSum > maxSizeSum){
                        maxSizeSum = curSum;
                    }
                }
            }
            maxSums.put(size, maxSizeSum);
        }

        int curMaxSum = -1;
        int curSize = -1;
        for(Integer key: maxSums.keySet()){
            int curSum = maxSums.get(key);
            if(curSum <= maxSum && curSum > curMaxSum){
                curMaxSum = curSum;
                curSize = key;
            }
        }

        return curSize;
    }

    private static int sum(List<List<Integer>> grid, int rS, int cS, int size){
        int n = grid.size();
        int sum = 0;

        for(int r = rS; r < rS+size; r++){
            for( int c= cS; c < cS+size; c++){
                sum += grid.get(r).get(c);
            }
        }
        return sum;
    }


    public static void main(String[] args){
        // List<List<Integer>> grid1 = {{1, 1, 1}, {1, 1, 1}, {1, 1, 1}};


    }
    
}
