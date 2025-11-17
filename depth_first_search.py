import csv
import ast  # safe eval for dictionary


def dfs_iterative(graph, start):
    visited = set()
    stack = [start]
    order = []

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            order.append(node)
            for neighbor in reversed(graph[node]):
                if neighbor not in visited:
                    stack.append(neighbor)
    return order


def dfs_recursive(graph, node, visited=None, order=None):
    if visited is None:
        visited = set()
    if order is None:
        order = []

    if node not in visited:
        visited.add(node)
        order.append(node)
        for neighbor in graph[node]:
            dfs_recursive(graph, neighbor, visited, order)

    return order


def run_tests_from_csv(filename):
    total = 0
    passed = 0

    with open(filename, "r") as file:
        reader = csv.DictReader(file)
        for i, row in enumerate(reader, 1):
            graph = ast.literal_eval(row["graph"])
            start = row["start"]

            expected_iter = ast.literal_eval(row["expected_iterative"])
            expected_recur = ast.literal_eval(row["expected_recursive"])

            result_iter = dfs_iterative(graph, start)
            result_recur = dfs_recursive(graph, start)

            iter_pass = (result_iter == expected_recur)
            recur_pass = (result_recur == expected_recur)

            total += 1  # 2 checks per test case (iter + recur)
            passed += (iter_pass + recur_pass)//2

            print(f"\nTest Case {i}: Start = {start}")
            print("Graph:", graph)

            #print("Expected Iterative:", expected_iter)
            print("Actual Iterative  :", result_iter, "✅" if iter_pass else "❌")

            print("Actual Recursive  :", result_recur, "✅" if recur_pass else "❌")
            print("Expected Result:", expected_recur)

    print(f"\nSummary: {passed}/{total} checks passed ✅")


if __name__ == "__main__":
    run_tests_from_csv("dfs_test_case.csv")
