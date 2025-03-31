import Foundation

func solution(_ brown:Int, _ yellow:Int) -> [Int] {
    for num in 1...yellow {
        if yellow % num == 0 {
            var num2 = yellow / num
            
            if num * 2 + num2 * 2 + 4 == brown {
                return [num2 + 2, num + 2]
            } 
        }
    }
    return [0, 0]
}