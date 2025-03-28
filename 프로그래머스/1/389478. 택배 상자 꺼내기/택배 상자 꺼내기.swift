import Foundation

func solution(_ n: Int, _ w: Int, _ num: Int) -> Int {
    let rowCount = (n - 1) / w + 1
    var warehouse = [[Int]](repeating: [Int](repeating: 0, count: w), count: rowCount)
    var currentBoxNumber = 1
    
    for i in 0..<rowCount {
        let remain = n - (currentBoxNumber - 1)
        let boxesInThisRow = min(remain, w)
        if i % 2 == 0 {
            for c in 0..<boxesInThisRow {
                warehouse[i][c] = currentBoxNumber + c
            }
        } else {
            for c in 0..<boxesInThisRow {
                warehouse[i][w - 1 - c] = currentBoxNumber + c
            }
        }
        currentBoxNumber += boxesInThisRow
    }
    
    var rowOfNum = -1, colOfNum = -1
    outer: for i in 0..<rowCount {
        for j in 0..<w {
            if warehouse[i][j] == num {
                rowOfNum = i
                colOfNum = j
                break outer
            }
        }
    }
    
    var countAbove = 0
    for i in (rowOfNum+1)..<rowCount {
        if warehouse[i][colOfNum] != 0 {
            countAbove += 1
        }
    }
    
    return countAbove + 1
}
