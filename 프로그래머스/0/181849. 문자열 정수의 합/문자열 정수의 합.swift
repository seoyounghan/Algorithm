import Foundation

func solution(_ num_str:String) -> Int {
    var ans: Int = 0
    
    for i in num_str {
        ans += Int(String(i))!
    }
    
    return ans
}
