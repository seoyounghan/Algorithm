import Foundation

func solution(_ my_string:String) -> String {
    var ans = ""
    var letters: [String] = []
    
    for i in my_string {
        var tmp = String(i)
        if !letters.contains(tmp) {
            ans += tmp
            letters.append(tmp)
        }
    }
    
    return ans
}