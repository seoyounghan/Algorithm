import Foundation

func solution(_ num:Int, _ n:Int) -> Int {
    var ans = 0
    if (num%n == 0) {
        ans = 1
    } else {
        ans = 0
    }
    
    return ans
}