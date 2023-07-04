import Foundation

func solution(_ number:Int, _ n:Int, _ m:Int) -> Int {
    var ans = 0
    if (number%n == 0) && (number%m == 0) {
        ans = 1
    }
    
    return ans
}