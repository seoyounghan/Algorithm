import Foundation

func solution(_ name:String) -> Int {
    let nameArray = Array(name)
    let n = nameArray.count
    var answer = 0

    for letter in nameArray {
        let ascii = Int(letter.asciiValue!)
        let moveUp = ascii - 65 
        let moveDown = 91 - ascii 
        answer += min(moveUp, moveDown)
    }
    

    var horizontalMove = n - 1   
    for i in 0..<n {
        var next = i + 1

        while next < n && nameArray[next] == "A" {
            next += 1
        }

        horizontalMove = min(horizontalMove, 2 * i + (n - next), i + 2 * (n - next))
    }
    
    answer += horizontalMove
    return answer
}