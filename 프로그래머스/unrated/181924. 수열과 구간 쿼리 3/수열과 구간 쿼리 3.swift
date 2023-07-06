import Foundation

func solution(_ arr:[Int], _ queries:[[Int]]) -> [Int] {
    var ans = arr
    for query in queries {
        let num1 = query[0] 
        let num2 = query[1]
        
        let tmp = ans[num1]
        ans[num1] = ans[num2]
        ans[num2] = tmp
    }
    return ans
}