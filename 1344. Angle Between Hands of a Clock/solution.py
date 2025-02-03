class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        # calculate each hour and minute location
        # get location angle
        # get minimum
        # 360 / 12 -> 30
        # 30 / 60 -> 0.5
        # for each min, it's moving 0.5
        # we already having same for min
        # 360 / 60 -> 6
        min_angle = 6 * minutes
        hour_angle = 30 * hour + 0.5 * minutes
        # now calculate
        # 180 - 15
        # 180 - 105
        # do calculation of
        # abs diff of those two
        # 360 - abs diff
        abs_diff = abs(min_angle - hour_angle)
        return min(abs_diff, 360 - abs_diff)
        # return min(abs(min_angle - hour_angle))
