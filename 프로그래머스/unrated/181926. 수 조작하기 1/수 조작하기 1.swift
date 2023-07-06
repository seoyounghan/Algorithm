import Foundation

func solution(_ n:Int, _ control:String) -> Int {
    var ans: Int = n
    for c in control {
        if c == "w" {
            ans += 1
        } else if c == "s" {
            ans -= 1
        } else if c == "d" {
            ans += 10
        } else if c == "a" {
            ans -= 10
        }
    }
    return ans
}