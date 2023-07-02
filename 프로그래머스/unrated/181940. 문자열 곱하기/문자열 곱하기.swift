import Foundation

func solution(_ my_string:String, _ k:Int) -> String {
    var ans: String = ""
    
    for _ in 1...k {
      ans += my_string  
    }
    return ans
}