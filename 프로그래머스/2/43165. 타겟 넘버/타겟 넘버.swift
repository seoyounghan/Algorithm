import Foundation

func solution(_ numbers:[Int], _ target:Int) -> Int {
    var ans = 0
    var numbersCount = numbers.count
    
    func dfs(index: Int, num: Int) {
        if index == numbersCount - 1 {
            if (num + numbers[index] == target) || (num - numbers[index] == target) {
                ans += 1
            }
        } else {
            dfs(index: index + 1, num: num + numbers[index])
            dfs(index: index + 1, num: num - numbers[index])
        }
        
    }
    
    dfs(index: 0, num: 0)
    
    
    return ans
}