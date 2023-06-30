import Foundation

let s1 = readLine()!
var result: String = ""

for i in s1 {
    var a = String(i)
    var uppers1 = a.uppercased()
    var lowers1 = a.lowercased()
    if a == uppers1 {
        result += lowers1
    } else {
        result += uppers1
    }
}
print(result)
