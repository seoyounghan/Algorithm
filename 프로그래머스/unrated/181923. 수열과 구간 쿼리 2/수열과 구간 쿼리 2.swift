import Foundation

func solution(_ arr:[Int], _ queries:[[Int]]) -> [Int] {
    var ans: [Int] = []
    for query in queries {
        let s = query[0]
        let e = query[1]
        let k = query[2]
        var tmp: Int = 1000001
        for num in s...e {
            if arr[num] > k {
                tmp = min(arr[num], tmp)
            }
        }
        if tmp == 1000001 {
            tmp = -1
        }
        
        ans.append(tmp)
    }
    return ans
}