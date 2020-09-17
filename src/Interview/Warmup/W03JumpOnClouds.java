package Interview.Warmup;

/*
 * Warmup 03 Jumping on the Clouds
 * Emma is playing a new mobile game that starts with consecutively numbered clouds. 
 * Some of the clouds are thunderheads and others are cumulus. She can jump on any 
 * cumulus cloud having a number that is equal to the number of the current cloud 
 * plus 1 or 2. 
 * 
 * She must avoid the thunderheads. Determine the minimum number of jumps it will 
 * take Emma to jump from her starting postion to the last cloud. It is always 
 * possible to win the game.

 * For each game, Emma will get an array of clouds numbered 0 if they are safe or
 * 1 if they must be avoided. 
 * 
 * For example, c= [0, 1, 0, 0, 0, 1, 0] indexed from 0...6. The number on each 
 * cloud is its index in the list so she must avoid the clouds at indexes 1 and 
 * 5. She could follow the following two paths: 0 -> 2 -> 4 -> 6 or 0 -> 2 -> 3 
 * -> 4 -> 6. The first path takes 3 jumps while the second takes 4.

 * Function Description

Complete the jumpingOnClouds function in the editor below. It should return the minimum number of jumps required, as an integer.

jumpingOnClouds has the following parameter(s):

    c: an array of binary integers

 * Input Format

The first line contains an integer n, the total number of clouds. The second line 
contains n space-separated binary integers describing clouds c[i] where 0 <= i < n


 * Constraints
 2 <= n <=100
 c[i] belongs to {0,1}
 c[0] = c[n-1] = 0


 * Output Format

Print the minimum number of jumps needed to win the game.

 * Sample Input 0

7
0 0 1 0 0 1 0

 * Sample Output 0

4

 * Explanation 0:
Emma must avoid
and . She can win the game with a minimum of jumps:
 */


public class W03JumpOnClouds {
    
    public static int jumpingOnClouds(int[] c) {
        int jump = 0;
        int cur = 0;
        int n = c.length;
        while (cur < n){
            if((cur+2) < n-1 && c[cur+2] == 1 ){
                cur+=1;
            }else if(cur+2 > n-1){
                cur+=1;
            }else{
                cur+=2;
            }
            jump++;
        }
        return jump - 1;
    }

    public static void main(String[] args){
        int[] c1 = {0, 0, 1, 0, 0, 1, 0};
        int j1 = jumpingOnClouds(c1);
        System.out.printf("Expected: 4, result: %d\n", j1);

        int[] c2 = {0, 0, 0, 1, 0, 0};
        int j2 = jumpingOnClouds(c2);
        System.out.printf("Expected: 3, result: %d\n", j2);
    }
}