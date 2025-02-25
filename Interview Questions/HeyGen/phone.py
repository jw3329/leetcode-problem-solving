from typing import Optional
'''
Notes
put(a, 1) (0,1)
put(a, 2) (0,2)
get(a) => 2 look for current (0) , and final value which is very end
snapshot() -> next_snapshot_id = 1
snapshot()
snapshot()
put(a) 
bisect left
get(a) => 2 -> get very end value
delete(a) -> change very end value to -inf
- check if next_snapshot_id exists, if exists, then remove, if not, then skip
{
  a -> [(0, 2)]
}
get(a) => raise Error -> if you find -inf for that value, then raise error
'''
import sys

class SnapshotMap:
    def __init__(self):
        # Initialize your class here
        # first snapshot should be 0
        # snapshots 
        # key -> values: [(snapshot_id, value)]
        self.next_snapshot_id = 0
        self.snapshots = dict()

    def get(self, k: str, snap_id: Optional[int] = None) -> int:
        print(k, snap_id, self.snapshots)
        # Implement the get method here
        # do bisect left
        # get k and snap_id
        if snap_id is not None and snap_id >= self.next_snapshot_id:
          raise Exception('snapshot id over')
        if snap_id is None:
          if self.snapshots[k][-1][1] == -sys.maxsize: raise Exception('')
          return self.snapshots[k][-1][1]
        values = self.snapshots[k]
        left = 0
        right = len(values) - 1
        while left <= right:
          mid = left + (right - left) // 2
          print('here', mid, snap_id)
          # check if snap_id is less then mid
          # if more, then left + 1
          # else, then right = mid
          # [0, 1, 3]
              # ^
          if snap_id == values[mid][0]:
            return values[snap_id][1]
          elif snap_id > values[mid][0]:
            left = mid
          else:
            right = mid - 1
        # return
        print(left, values[left][1])
        return values[left][1]

    def put(self, k: str, v: int) -> None:
        # Implement the put method here
        # check if current snapshot is in key
        # if in key, then change value
        # if not, then insert
        if k not in self.snapshots:
          self.snapshots[k] = [[self.next_snapshot_id, v]]
        else:
          # in value
          # check now the very end
          end_snapshot = self.snapshots[k][-1]
          # check same snapshot
          if end_snapshot[0] == self.next_snapshot_id:
            # update
            end_snapshot[1] = v
          else:
            # insert
            self.snapshots[k].append([self.next_snapshot_id, v])

    def delete(self, k: str) -> None:
        # Implement the delete method here
        if k not in self.snapshots:
          raise Exception('k not stored')
        self.snapshots[k][-1][1] = -sys.maxsize

    def take_snapshot(self) -> int:
        # Implement the take_snapshot method here
        res = self.next_snapshot_id
        self.next_snapshot_id += 1
        return res

print("===== Initialization =====")

# Create an instance of SnapshotMap
s = SnapshotMap()

# Add key-value pairs to the map
s.put("a", 1)
s.put("b", 2)

# Take a snapshot of the current state of the map
snap_id_0 = s.take_snapshot()

# Update the map
s.put("a", 5)
s.delete("b")
s.put("a", 10)

# Take another snapshot
snap_id_1 = s.take_snapshot()

# Update the map again
s.put("b", 20)

# Take a final snapshot
snap_id_2 = s.take_snapshot()

# Update the map one last time
s.put("a", 100)

print("===== Validation =====")

# Assert the current state of the map and the state at each snapshot
assert snap_id_0 == 0
assert snap_id_1 == 1
assert snap_id_2 == 2
assert s.get("a") == 100
assert s.get("a", snap_id_0) == 1
assert s.get("a", snap_id_1) == 10
assert s.get("a", snap_id_2) == 10

assert s.get("b") == 20
assert s.get("b", snap_id_0) == 2

# Check that a KeyError is raised for a key that does not exist in a snapshot
try:
    s.get("b", snap_id_1)
except KeyError:
    pass
else:
    raise Exception("KeyError was not raised")

assert s.get("b", snap_id_2) == 20

print("===== All Passed! =====")
