import Foundation

func solution(_ ineq:String, _ eq:String, _ n:Int, _ m:Int) -> Int {
    var ans = 0
    if ineq == "<" {
        if eq == "=" {
            if n <= m {
                ans = 1
            }
        } else {
            if n < m {
                ans = 1
            }
        }      
    } else {
        if eq == "=" {
            if n >= m {
                ans = 1
            }
        } else {
            if n > m {
                ans = 1
            }
        }      
    }
    
    
    return ans
}