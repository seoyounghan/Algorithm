import Foundation

func solution(_ a:Int, _ b:Int) -> Int {
    var bcount = 0.0
    var ans: Double
    var bc = b
    let ab2 = Double(2 * a * b)
    
    while bc != 0 {
        bc = bc / 10
        bcount += 1.0
    }
      
    
    let aplus = Double(a) * pow(10.0, bcount) + Double(b)
    
    if aplus > ab2 {
        ans = aplus
    } else {
        ans = ab2
    }
    
    return Int(ans)
}