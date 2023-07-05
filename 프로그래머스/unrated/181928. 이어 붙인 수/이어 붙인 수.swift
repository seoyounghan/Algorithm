import Foundation

func solution(_ num_list:[Int]) -> Int {
    var odd: Int = 0
    var even: Int = 0
    
    for num in num_list {
        if num%2 == 0 {
            even = even*10 + num
        } else {
            odd = odd*10 + num
        }
    }
    
    return (even + odd)
}