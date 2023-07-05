import Foundation

func solution(_ num_list:[Int]) -> Int {
    var sum = 0
    var sup = 1
    for num in num_list {
        sum += num
        sup = sup*num
    }
    
    if sup < sum*sum {
        return 1
    } else {
        return 0
    }
}