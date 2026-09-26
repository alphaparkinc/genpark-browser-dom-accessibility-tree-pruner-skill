import sys
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

from client import BrowserDomAccessibilityTreePrunerClient

def main():
    client = BrowserDomAccessibilityTreePrunerClient()
    res = client.prune_accessibility_tree()
    print("=== Browser DOM Accessibility Tree Pruner Output ===")
    print(f"Page: {res['page_url']} | Token Reduction: {res['estimated_token_reduction']}")
    print(f"Nodes: {res['raw_dom_node_count']} raw -> {res['retained_essential_nodes_count']} essential actionable nodes")
    print("\nPruned Action Tree:")
    for node in res['pruned_interactive_tree']:
        action_flag = "[CLICKABLE]" if node['actionable'] else "[LANDMARK]"
        print(f"  * {action_flag:12s} <{node['role']}> '{node['name']}' -> {node['selector']}")

if __name__ == '__main__':
    main()
