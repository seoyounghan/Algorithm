import Foundation

func solution(_ numbers:[Int]) -> [Int] {
    var ans: [Int] = []
    
    for (i, n) in numbers.enumerated() {
        let b = i + 1
        for t in numbers[b...] {
            ans.append(n + t)
        }
    }
    
    return Array(Set(ans)).sorted()
}