import Foundation

func solution(_ num_list:[Int]) -> [Int] {
    var num_list2 = num_list
    var last = num_list[num_list.count - 1] 
    var last2 = num_list[num_list.count - 2]
    
    if last > last2 {
        num_list2.append(last-last2)
    } else {
        num_list2.append(last*2)
    }
    return num_list2
}