import Foundation

func solution(_ arr:[Int], _ idx:Int) -> Int {
    
    for (i, a) in arr.enumerated() {
        if i >= idx && a == 1 {
            return i
        } 
    }
    
    
    return -1
}