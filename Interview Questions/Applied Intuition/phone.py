def helper(lat, lon, length):
    robot = -37.3900, -122.0812
    # print("left, right, top, bottom", lat, lat + length, lon, lon + length)
    return lat <= robot[0] < lat + length and lon <= robot[1] < lon + length


def solve(lat, lon, length, limit):
    left_up_scanned = helper(lat - length, lon - length, length)
    right_up_scanned = helper(lat, lon - length, length)
    left_down_scanned = helper(lat - length, lon, length)
    right_down_scanned = helper(lat, lon, length)
    print(
        lat,
        lon,
        length,
        left_up_scanned,
        right_up_scanned,
        left_down_scanned,
        right_down_scanned,
    )
    condition = 0
    condition += left_up_scanned == True
    condition += right_up_scanned == True
    condition += left_down_scanned == True
    condition += right_down_scanned == True
    if length < limit:
        return lat, lon, length
    if left_up_scanned:
        return solve(lat - length / 2, lon - length / 2, length / 2, limit)
    if right_up_scanned:
        return solve(lat + length / 2, lon - length / 2, length / 2, limit)
    if left_down_scanned:
        return solve(lat - length / 2, lon + length / 2, length / 2, limit)
    if right_down_scanned:
        return solve(lat + length / 2, lon + length / 2, length / 2, limit)


print(solve(0, 0, 180, 0.000001))
