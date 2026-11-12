# CLA-2: Algorithm Battle — Which Data Structure Wins?

## Part A — Problem selection
**Application: Student Record Search.** A college stores Student ID, name and department. A unique ID is frequently used to retrieve a student's record. An unsorted list may inspect many records, so efficient search matters. BST stores IDs in ordered form; AVL is a balanced BST; hashing supports fast exact-key lookup.

## Part B — Implementation
- **BST:** smaller ID goes left, larger ID right. Search follows comparisons. Inorder is sorted; preorder and postorder are also implemented.
- **AVL:** BST insertion plus node heights and balance factor `height(left)-height(right)`. LL, RR, LR and RL rotations rebalance it.
- **Hashing:** hash index `ID % capacity`; collisions are resolved by checking successive slots (linear probing, wrap-around).

## Part C — Mini experiment
The program uses the same 40 unique IDs and insertion order for all structures. It tests successful search (ID 1038), unsuccessful search (9999), inserts ID 1120, then searches for it. Run `python src/main.py`; the program prints comparisons/probes, heights, collisions and traversals.

### Observations (fill from your own run)
| Metric | BST | AVL | Hashing |
|---|---:|---:|---:|
| Successful search comparisons/probes | ___ | ___ | ___ |
| Unsuccessful search comparisons/probes | ___ | ___ | ___ |
| Insertion comparisons/probes for 1120 | ___ | ___ | ___ |
| Initial height | ___ | ___ | N/A |
| Final height | ___ | ___ | N/A |
| Initial insertion collisions | N/A | N/A | ___ |
| Collision(s) for ID 1120 | N/A | N/A | ___ |
| Traversals | In/pre/post | Inorder | Not supported |

## Part D — Technical comparison
| Parameter | BST | AVL | Hashing + linear probing |
|---|---|---|---|
| Search | Average O(log n), worst O(n) | O(log n) worst | Average O(1), worst O(n) |
| Insertion | Average O(log n), worst O(n) | O(log n), balancing rotations | Average O(1), probes possible |
| Height | Insertion-order dependent | Balanced | N/A |
| Ordered traversal | Yes | Yes | No |
| Strength | Simple | Predictable search | Fast exact lookup |
| Weakness | Can skew | More complex | Collisions/load factor |

Interpret measured values carefully: fewer comparisons/probes means fewer inspected keys in this run. Height indicates tree path depth. Collision count depends on hash function and capacity. A single dataset is evidence for this experiment, not a universal proof.

## Part E — Final verdict
**Recommended winner for exact Student-ID lookup: Hashing with Linear Probing**, provided the table has suitable capacity and load factor. It generally gives average O(1) lookup. Use the actual output to justify: successful/unsuccessful probes ___/___; initial collisions ___; BST/AVL heights ___/___ . AVL is preferable if sorted traversal and guaranteed O(log n) search are important; plain BST is easiest but can become skewed.

## Viva quick answers
1. BST: left keys smaller, right keys larger.
2. BST can skew due to insertion order; worst height n.
3. AVL: self-balancing BST; balance factor −1, 0, +1.
4. Rotations: LL, RR, LR, RL.
5. Hashing maps a key to a table slot.
6. Collision: different keys map to same slot.
7. Linear probing checks subsequent slots until empty/matching key.
8. Load factor = records/table capacity.
9. Hashing does not naturally produce sorted traversal.
10. Hash for exact lookup; AVL for ordered operations and worst-case logarithmic search.

**Submission:** run the code, capture output, fill observations, push folder to GitHub, and submit repository URL plus report on Google Classroom. Do not present unrun values as experimental results.
