import Foundation

func solution(_ numbers:[Int], _ target:Int) -> Int {
    var ans = 0
    
    func findNum(_ sum: Int, _ index: Int) {
        if index == numbers.count - 1 {
            if (sum + numbers[index]) == target || (sum - numbers[index]) == target {
                ans += 1
            }
        } else {
            findNum(sum + numbers[index], index + 1)
            findNum(sum - numbers[index], index + 1)
        }
    }
    
    findNum(0, 0)
    
    return ans
}