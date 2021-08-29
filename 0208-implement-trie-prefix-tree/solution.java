class Trie {
    Trie[]  arr;
    boolean wordEnd;
    
    /*  Initialize your data structure here  */
    public Trie() {
        arr = new Trie[26];
    }
    
    
    /*  Inserts a word into the trie  */
    public void insert(String word) {
        insert( word, 0 );
    }
    
    private void insert(String word, int i) {
        if( i == word.length() ) {
            wordEnd = true;
            return;
        }
        
        int index = word.charAt(i) - 'a';
        if( arr[index] == null ) arr[index] = new Trie();
        
        arr[index].insert(word, i + 1);
    }
    
    
    /*  Returns if the word is in the trie  */
    public boolean search(String word) {
        return search( word, 0 );
    }
    
    private boolean search(String word, int i) {
        if( i == word.length() ) return wordEnd;
        
        int index = word.charAt(i) - 'a';
        
        if( arr[index] == null ) return false;
        else return arr[index].search( word, i + 1 );
    }
    
    
    /*  Returns if there is any word in the trie that starts with the given prefix  */
    public boolean startsWith(String prefix) {
        return startsWith( prefix, 0 );
    }
    
    public boolean startsWith(String prefix, int i) {
        if( i == prefix.length() ) return true;
        
        int index = prefix.charAt(i) - 'a';
        
        if( arr[index] == null ) return false;
        else return arr[index].startsWith( prefix, i + 1 );
    }
}