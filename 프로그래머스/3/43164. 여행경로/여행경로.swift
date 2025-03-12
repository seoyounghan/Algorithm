import Foundation

func solution(_ tickets:[[String]]) -> [String] {
    let ticketNum = tickets.count
    var ans: [String] = ["ICN"]
    var isVisited = Array(repeating: false, count: ticketNum)
    var sortedTickets = tickets.sorted {
        if $0[0] == $1[0] {
            return $0[1] < $1[1]
        }
        return $0[0] < $1[0]
    }
    var isAns = false
    
    func dfs(path: [String], count: Int) {
        if isAns { return }
        
        if count == ticketNum {
            ans = path
            isAns = true
            return
        }
        
        for i in 0..<ticketNum {
            if !isVisited[i] && sortedTickets[i][0] == path.last! {
                isVisited[i] = true
                dfs(path: path + [sortedTickets[i][1]], count: count + 1)
                isVisited[i] = false
            }
        }
    }
    
    dfs(path: ans, count: 0)
    
    return ans 
}