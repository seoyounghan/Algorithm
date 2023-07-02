import Foundation

func solution(_ a:Int, _ b:Int) -> Int {
    var acount = 0.0
    var bcount = 0.0
    var ans: Double
    var ac = a
    var bc = b
    
    while ac != 0 {
        ac = ac / 10      
        acount += 1.0
    }
    
    while bc != 0 {
        bc = bc / 10
        bcount += 1.0
    }
    
    
    
    let aplus = Double(a) * pow(10.0, bcount) + Double(b)
    let bplus = Double(b) * pow(10.0, acount) + Double(a)
    
    if aplus >= bplus {
        ans = aplus
    } else {
        ans = bplus
    }
    
    return Int(ans)
}