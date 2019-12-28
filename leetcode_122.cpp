/*
The intuition is that every time when you find you can make profits, you should make a transaction.
Likewise, when you find that the price will go down, you should sell the stock.
One thing you need to take care of is that in C++, size() will return an unsigned int, which is likely to result in an overflow.
So I recommend converting the length of the array to int first, namely writing something like: int n = prices.size();.
And in this way, overflows won't occur.
*/

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int res = 0;
        int n = prices.size();
        for(int i = 0; i < n-1; i++){
            if (prices[i+1]-prices[i] > 0){
                res += prices[i+1]-prices[i];
            }
        }
        return res;
        
    }
};
