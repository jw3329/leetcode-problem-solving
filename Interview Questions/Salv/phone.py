class KeyValueStore:
    def __init__(self):
        """
        Constructor.
        """
        # curr -> dict, snapshots -> dict
        # curr -> current stores
        # snapshots -> (snapshot_id -> dict)
        # init value of curr_snapshot_id, being incremented
        # once call snapshot, save curr_snapshot_id to snapshots with curr dict
        # dict -> key, -> values of versions
        # versions is sorted
        # if we can store version, with actual value, then
        # when we trying to find actual value, we can binary search, and grab
        # [(1, "abc"), (5, "def")]
        
        self.next_snapshot_id = 0
        self.curr = dict()
        self.snapshots = dict()
        self.wrotes = set()
        
        
        

    def set(self, k, v):
        """
        Associate key with given value.
        """
        if k not in self.snapshots:
            self.snapshots[k] = [(self.next_snapshot_id, v)]
        else:
            last_value = self.snapshots[k][-1]
            if last_value != v:
                self.snapshots[k].append((self.next_snapshot_id, v))
        

    def snapshot(self):
        """
        Snapshot the current state & return an auto incrementing integer snapshot id
        of the snapshot just created.

        Snapshot id starts with 0.
        """
        # from curr,
        # go through key value
        # check in snapshots, if key is in snapshots,
        # if not, create one, if it is, then check last value
        # if last value is same, no need to append, if not, then append
        res = self.next_snapshot_id
        self.next_snapshot_id += 1
        return res
        
        

    def get(self, k):
        """
        Get latest value associated with given key.
        """
        return self.snapshots[k][-1][1] if k in self.snapshots else None

    def get_from_snapshot(self, snapshot_id, k):
        """
        Get value associated with given key at given snapshot id.
        """    
        # get value from k
        # binary search snapshot_id
        # we should make sure we only store init version in snapshots
        # if we don't find target, we should get most recent version
        # grab value
        if k not in self.snapshots:
            return None
        values = self.snapshots[k]
        if len(values) == 0:
            return None
        if snapshot_id >= self.next_snapshot_id:
            return None
        # print(snapshot_id, k, self.snapshots)
        left = 0
        right = len(values) - 1
        while left < right:
            mid = (left + right) // 2
            if values[mid][0] < snapshot_id:
                left = mid + 1
            else:
                right = mid
        # print('returning value', values[left])
        if snapshot_id < values[left][0]:
            return None
        return values[left][1]
        

if __name__ == "__main__":
    store = KeyValueStore()
    snapshotId = store.snapshot()
    assert snapshotId == 0

    store = KeyValueStore()
    store.set("k1", "v1")
    assert store.get("k1") == "v1"
    # assert store.get_from_snapshot(first_snapshot, "k1") is None
    first_snapshot = store.snapshot() # -> 0
    assert store.get("k1") == "v1"
    store.set("k1", "v2")
    assert store.get("k1") == "v2"
    assert store.get("k2") is None
    assert store.get_from_snapshot(first_snapshot, "k1") == "v1"
    assert store.get_from_snapshot(first_snapshot, "k2") is None

    # curr -> dict, snapshots -> dict
    # curr -> current stores
    # snapshots -> (snapshot_id -> dict)
    # init value of curr_snapshot_id, being incremented
    # once call snapshot, save curr_snapshot_id to snapshots with curr dict
    # dict -> key, -> values of versions
    # versions is sorted
    # if we can store version, with actual value, then
    # when we trying to find actual value, we can binary search, and grab
    # [(1, "abc"), (5, "def")]

    store = KeyValueStore()
    first_snapshot = store.snapshot()
    store.set("k1", "v1")
    assert store.get("k1") == "v1"
    assert store.get_from_snapshot(first_snapshot, "k1") is None


    store = KeyValueStore()
    store.set("k1", "v1")
    store.set("k1", "v1.1")
    store.set("k1", "v1.2")
    first_snapshot = store.snapshot()
    assert store.get_from_snapshot(first_snapshot, "k1") == "v1.2"
    assert store.snapshot() == first_snapshot + 1


    store = KeyValueStore()
    store.set("k1", "v1")
    store.snapshot() # -> 0
    store.snapshot() # -> 1
    store.snapshot() # -> 2
    assert store.get("k1") == "v1"
    assert store.get_from_snapshot(0, "k1") == "v1"
    assert store.get_from_snapshot(1, "k1") == "v1"
    assert store.get_from_snapshot(2, "k1") == "v1"
    store.set("k1", "v2")
    store.set("k1", "v3")
    store.set("k1", "v4")
    store.set("k2", "v2")
    store.snapshot() # -> 3
    store.snapshot() # -> 4
    assert store.get("k1") == "v4"
    assert store.get("k2") == "v2"
    assert store.get_from_snapshot(2, "k1") == "v1"
    assert store.get_from_snapshot(3, "k1") == "v4"   
    assert store.get_from_snapshot(4, "k1") == "v4"   
    assert store.get_from_snapshot(3, "k2") == "v2"   
    assert store.get_from_snapshot(4, "k2") == "v2"   
    assert store.get_from_snapshot(2, "k2") == None 



    store = KeyValueStore()
    store.set("k1", "v1")
    first_snapshot = store.snapshot()
    store.set("k1", "v2")
    store.snapshot()
    assert store.get_from_snapshot(first_snapshot, "key") is None

