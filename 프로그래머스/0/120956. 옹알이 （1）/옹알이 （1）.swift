import Foundation

func solution(_ babbling:[String]) -> Int {
    var ans = 0
    var isVisited = Array(repeating: false, count: 4)
    let li = ["aya", "ye", "woo", "ma"]
    
    for i in babbling {
        var tmp = 0
        for l in li {
            if i.contains(l) {
                tmp += l.count
            }
        }
        
        if tmp == i.count {
            ans += 1
        }
    }
    
    
    return ans
}