import Foundation

func solution(_ operations:[String]) -> [Int] {
    var q: [Int] = []
    
    for i in operations {
        var operation = i.components(separatedBy: " ")
        
        if operation[0] == "I" {
            q.append(Int(operation[1])!)
        } else if operation[0] == "D" {
            if q.count == 0 {
                continue
            }
            
            if operation[1] == "-1" {
                q.remove(at: q.firstIndex(of: q.min()!)!)
            } else {
                q.remove(at: q.firstIndex(of: q.max()!)!)
            }
        }
    }
    if q.count == 0 {
        return [0, 0]
    }
    
    return [q.max()!, q.min()!]
}