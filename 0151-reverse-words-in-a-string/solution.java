class Solution {
    /**
     * @time  : O(n), n is the length of input string
     * @space : O(m), m is the number of words in the input string
     */
    
    public String reverseWords(String s) {
        int l = 0, r = s.length() - 1;
        while(l <= r && s.charAt(l) == ' ') ++l;
        while(l <= r && s.charAt(r) == ' ') --r;

        Deque<String> d = new ArrayDeque();
        StringBuilder word = new StringBuilder();
        
        while(l <= r) {
            char c = s.charAt(l);

            if((word.length() != 0) && (c == ' ')) {
                d.offerFirst(word.toString());
                word.setLength(0);
            } else if(c != ' ') {
                word.append(c);
            }
            ++l;
        }
        
        d.offerFirst(word.toString());
        return String.join(" ", d);
    }
}