import Foundation

func solution(_ n: Int, _ vertex: [[Int]]) -> Int {
    var graph = Array(repeating: [Int](), count: n+1)
    
    for edge in vertex {
        let a = edge[0]
        let b = edge[1]
        graph[a].append(b)
        graph[b].append(a)
    }
    
    var dist = Array(repeating: -1, count: n+1)
    dist[1] = 0 
    
    var queue = [1]
    var index = 0
    
    while index < queue.count {
        let current = queue[index]
        index += 1
        
        // 현재 노드와 인접한 노드들 확인
        for next in graph[current] {
            // 아직 방문하지 않은 노드라면 거리 갱신 후 큐에 추가
            if dist[next] == -1 {
                dist[next] = dist[current] + 1
                queue.append(next)
            }
        }
    }
    
    // dist 배열 중 최댓값(가장 멀리 떨어진 거리) 찾기
    let maxDist = dist.max() ?? 0
    
    // 최댓값과 같은 거리를 가진 노드의 개수 반환
    return dist.filter { $0 == maxDist }.count
}


