import Foundation

func solution(_ a:Int, _ d:Int, _ included:[Bool]) -> Int {
    var ans: Int = 0
    var sum: Int = 0
    for i in included {
        if sum == 0 {
            sum += a
        } else {
            sum += d
        }
        if i == true {
            ans += sum
        }
    }
    return ans
}