import Foundation

func solution(_ my_string:String, _ overwrite_string:String, _ s:Int) -> String {
    let s1 = my_string.startIndex
    let s2 = my_string.index(my_string.startIndex, offsetBy: s)
    
    
    if (s + overwrite_string.count < my_string.count) {
        let s3 = my_string.index(my_string.startIndex, offsetBy: s + overwrite_string.count)
        let s4 = my_string.endIndex

        return (String(my_string[s1..<s2]) + overwrite_string + String(my_string[s3..<s4]))
    } else {
        return (String(my_string[s1..<s2]) + String(overwrite_string))
    }
}