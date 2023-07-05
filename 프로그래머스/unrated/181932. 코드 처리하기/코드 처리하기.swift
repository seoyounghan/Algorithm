import Foundation

func solution(_ code:String) -> String {
    var mode = 0
    var ret: String = ""
    var count = 0
    for i in code {
        if mode == 0 {
            if i == "1" {
                mode = 1
            } else {
                if count%2 == 0 {
                    ret += String(i)}
            }
        } else {
            if i == "1" {
                mode = 0
            } else {
                if count%2 != 0 {
                ret += String(i) } 
            }
        }
        count += 1
    }
    if ret.isEmpty {
        return "EMPTY"
    } else {
        return ret
    }
}