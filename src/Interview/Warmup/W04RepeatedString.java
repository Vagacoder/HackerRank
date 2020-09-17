package Interview.Warmup;

/*
 * Warmup Repeated String
 * 
 *  
 */
public class W04RepeatedString {
    
    public static long repeatedString(String s, long n) {
        int sN = s.length();
        long result = 0;
        
        long fullStringN = n/sN;
        long partialStringN = n%sN;

        long aNinS = 0;
        long aNinPartialS = 0;

        for(int i = 0;i < sN; i++){
            char c = s.charAt(i);
            if(c == 'a'){
                aNinS++;
                if( i < partialStringN){
                    aNinPartialS++;
                }
            }
        }

        result += fullStringN * aNinS;
        result += aNinPartialS;

        return result;

    }

    public static void main(String[] args){
        String s1 = "aba";
        long n1 = 10L;
        long r1 = repeatedString(s1, n1);
        System.out.printf("Expected: 7, result: %d\n", r1);

        String s2 = "a";
        long n2 = 1000000000000L;
        long r2 = repeatedString(s2, n2);
        System.out.printf("Expected: 1000000000000, result: %d\n", r2);
    }
}
