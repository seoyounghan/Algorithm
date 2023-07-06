import Foundation

func solution(_ numLog:[Int]) -> String {
    var ans: String = ""
    var prev: Int = 0
    for num in numLog {
        let tmp: Int = prev - num
        if tmp == -1 {
            ans += "w"
        } else if tmp == 1 {
            ans += "s"
        } else if tmp == -10 {
            ans += "d"
        } else if tmp == 10 {
            ans += "a"
        }
        prev = num
    }
    return ans
}