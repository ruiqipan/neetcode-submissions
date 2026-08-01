class Solution {
    public boolean hasDuplicate(int[] nums) {
        HashSet <Integer> hs = new HashSet();
        boolean tf = true;
        for(int n : nums){
            tf = hs.add(n);
            if(tf == false){
                return true;
            }
        }
        return false;
    }
}