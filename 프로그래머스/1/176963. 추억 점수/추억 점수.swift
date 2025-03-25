import Foundation

func solution(_ name:[String], _ yearning:[Int], _ photo:[[String]]) -> [Int] {
    var yearningDict: [String: Int] = [:]
    for (i, person) in name.enumerated() {
        yearningDict[person] = yearning[i]
    }

    var result: [Int] = []

    for people in photo {
        var score = 0
        for person in people {
            if let value = yearningDict[person] {
                score += value
            }
        }
        result.append(score)
    }

    return result
}
