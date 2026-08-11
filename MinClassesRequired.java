import java.util.*;

public class MinClassesRequired {

    public static int minClassesRequired(int n, int m, int[] a, int[] b) {
        Map<Integer, List<Integer>> adj = new HashMap<>();
        for (int i = 1; i <= n; i++) {
            adj.put(i, new ArrayList<>());
        }

        for (int i = 0; i < m; i++) {
            int u = a[i];
            int v = b[i];
            adj.get(u).add(v);
            adj.get(v).add(u);
        }
        Set<Integer> visited = new HashSet<>();
        int classes = 0;
        for (int person = 1; person <= n; person++) {
            if (visited.contains(person)) {
                continue;
            }
            classes++;
            Queue<Integer> queue = new ArrayDeque<>(); 
            queue.offer(person);
            visited.add(person);

            while (!queue.isEmpty()) {
                int current = queue.poll();
                
                for (int neighbor : adj.get(current)) {
                    if (!visited.contains(neighbor)) {
                        visited.add(neighbor);
                        queue.offer(neighbor);
                    }
                }
            }
        }

        return classes;
    }

    public static void main(String[] args) {
        int n = 7;
        int m = 4;
        int[] a = {1, 2, 3, 4};
        int[] b = {2, 3, 4, 5};

        System.out.println(minClassesRequired(n, m, a, b));
    }
}   