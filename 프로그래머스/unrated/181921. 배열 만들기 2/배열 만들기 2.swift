import Foundation

func solution(_ l:Int, _ r:Int) -> [Int] {
    var ans: [Int] = []
    for i in l...r {
        let tmp = String(i)
        var tok = 0
        for j in tmp {
            if (j != "0") && (j != "5") {
                tok = 1
                break
            }
        }
        if tok == 0 {
            ans.append(i)
        }
    }
    if ans.isEmpty {
        return [-1]
    } else {
        return ans
    }
}