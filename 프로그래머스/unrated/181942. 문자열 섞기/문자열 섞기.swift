import Foundation

func solution(_ str1:String, _ str2:String) -> String {
    var ans: String = ""
    
    for i in 0..<str1.count {
        ans = ans + String(str1[str1.index(str1.startIndex, offsetBy: i)])
        ans = ans + String(str2[str2.index(str2.startIndex, offsetBy: i)])
    }
    
    return ans
}