func solution(_ k: Int, _ dungeons: [[Int]]) -> Int {
    var maxCount = 0

    func dfs(current: Int, count: Int, remaining: [[Int]]) {
        var progressed = false
        for (index, dungeon) in remaining.enumerated() {
            if current >= dungeon[0] {
                progressed = true
                var nextRemaining = remaining
                nextRemaining.remove(at: index)
                dfs(current: current - dungeon[1], count: count + 1, remaining: nextRemaining)
            }
        }
        if !progressed {
            maxCount = max(maxCount, count)
        }
    }
    
    dfs(current: k, count: 0, remaining: dungeons)
    return maxCount
}
