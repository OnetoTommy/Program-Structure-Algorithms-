import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.Deque;
import java.util.List;

public class DFS_AllPath {

  List<List<Integer>> a = new ArrayList<List<Integer>>();
  Deque<Integer> b = new ArrayDeque<Integer>();

  public static void main(String[] args) {
    int[][] graph = {
        { 1, 2 }, // Node 0 → [1,2]
        { 3 }, // Node 1 → [3]
        { 3 }, // Node 2 → [3]
        {} // Node 3 → []
    }; // Node 3 → []
    DFS_AllPath solver = new DFS_AllPath();
    List<List<Integer>> result = solver.allpath(graph);
    System.out.println(result);

  }

  public void dfs(int[][] graph, int x) {

    if (x == graph.length - 1) {
      a.add(new ArrayList<Integer>(b));
      return;
    }

    for (int y : graph[x]) {
      b.offerLast(y);
      dfs(graph, y);
      b.pollLast();
    }

  }

  public List<List<Integer>> allpath(int[][] graph) {
    b.offerLast(0);
    dfs(graph, 0);
    return a;
  }
}