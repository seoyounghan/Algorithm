import Foundation

func solution(_ begin:String, _ target:String, _ words:[String]) -> Int {
    var words = words
    if !words.contains(target) {
        return 0
    }
    var ans = words.count + 1
    
    func compareWord(word: String, count: Int, wordLists: [String]) {
        if count >= words.count {
            return
        }
        if target == word {
            ans = min(ans, count)
        } else {
            for i in wordLists {
                var tmp = 0
                for j in zip(i, word) {
                    if j.0 != j.1 {
                        tmp += 1
                    }
                }
                if tmp == 1 {
                    let newWordLists = wordLists.filter { $0 != i }
                    compareWord(word: i, count: count + 1, wordLists: newWordLists)
                }
            }
        }
    }
    
    compareWord(word: begin, count: 0, wordLists: words)
    
    if ans == words.count + 1 {
        ans = 0
    }
    
    return ans
}