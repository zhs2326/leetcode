/*
This problem can be easily solved with BFS.
Just use a queue to implement BFS to simulate the rotting process.
The queue should be a queue of vectors and each vector stores the position of one rotten orange and the current minute.
Then we need to check that rottem orange's neighbors and if some of them are fresh oranges, they will be rotten one minute later.
So we need to increase the current minute by one and then push that orange's position and the new current minute into the queue.
Don't forget to change the corresponding value of that orange in the grid to be 2!
Or the program won't terminate!
Finally, we need to iterate over all the oranges in the grid again to check whether there are fresh oranges left.
If there are still fresh oranges, we should return -1. Otherwise, we should return the current minute.
*/

class Solution {
public:
    int orangesRotting(vector<vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();
        
        queue<vector<int>> q;
        
        for (int i = 0; i < m; i++){
            for(int j = 0; j < n; j++){
                if(grid[i][j] == 2){
                    vector<int> v = {i, j, 0};
                    q.emplace(v);
                }
            }
        }
        
        int directions[5] = {-1, 0, 1, 0, -1};
        int res = 0;
        
        while(!q.empty()){
            vector<int> v = q.front();
            q.pop();
            int x = v[0];
            int y = v[1];
            int d = v[2];
            res = d;
            for(int i = 0; i < 4; i++){
                int dx = directions[i];
                int dy = directions[i+1];
                if(x+dx >= 0 && x+dx < m && y+dy >= 0 && y+dy < n && grid[x+dx][y+dy] == 1){
                    v = {x+dx, y+dy, d+1};
                    q.push(v);
                    grid[x+dx][y+dy] = 2;
                }
            }
        }
        
        for(int i = 0; i < m; i++){
            for(int j = 0; j < n; j++){
                if(grid[i][j] == 1){
                    return -1;
                }
            }
        }
        
        return res;
    }
};
