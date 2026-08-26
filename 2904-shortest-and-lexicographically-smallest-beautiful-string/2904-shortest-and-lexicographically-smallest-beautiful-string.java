class Solution {
    public String shortestBeautifulSubstring(String s, int k) {
       String ans ="";
       int n = s.length();
       int min = Integer.MAX_VALUE;

       for(int i = 0; i < n; i++){
        String temp ="";
        int len = 0;
        
        int c = 0;

        for(int j = i; j < n; j++){
            char ch = s.charAt(j);
            temp += ch;

            if(ch == '1')
            c++;
            
            len = j - i +1;
            
            if(c==k){
                
            if(min > len){
                min = len;
                ans = temp;
            }
            else if( len == min && temp.compareTo(ans)<0)
                ans = temp;

                break;
            }

         }
       } 


       return ans;
    }
}