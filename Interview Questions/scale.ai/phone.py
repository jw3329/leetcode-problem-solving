from datetime import datetime

# Helpers
def parse_date(date_string):
    return datetime.strptime(date_string, "%Y-%m-%dT%H:%M:%SZ") 

"""
Part 1
Return the party windows for each neighborhood

Returns:
    dict: A dictionary where:
        - keys are neighborhood names (str)
        - values are dictionaries containing:
            'start_hour': int (0-23)
            'end_hour': int (0-23)
"""
def create_party_windows(party_submission_data, geographic_data):
    # TODO: implement
    
    # party_submission_data having party id
    # geographic_data has party id with neighbor
    
    # party_id -> submission
    # neighborhood -> submissions
    # iterate to grab min and max
    # store it to res
    
    submissions = party_submission_data['submissions']
    submissionData = submissions['submissionData']
    # generate party_id -> object
    submission_id_map = dict()
    for submission in submissionData:
        submission_id_map[submission["party_id"]] = submission
    
    # generate neigh -> submissions
    geo_data = geographic_data['geo_data']
    neighbor_map = dict()
    neighbor_town_map = dict()
    for data in geo_data:
        if data["neighborhood"] not in neighbor_map:
            neighbor_map[data["neighborhood"]] = []
        neighbor_map[data["neighborhood"]].append(
            submission_id_map[data["party_id"]]
        )
        neighbor_town_map[data["neighborhood"]] = data["town"]
    
    res = {}
    # iterate neighbor_map, and find min and max
    for neighbor in neighbor_map:
        data = neighbor_map[neighbor]
        # grab start and end
        min_start = min(map(lambda x: x["start_time"], data))
        max_end = max(map(lambda x: x["end_time"], data))
        start_hour = parse_date(min_start).hour
        end_hour = parse_date(max_end).hour
        res[neighbor] = dict(
            start_hour=start_hour,
            end_hour=end_hour,
            town=neighbor_town_map[neighbor]
        )
    
    return res
    
"""
Part 2
Return the dead zone times for the given party windows

Returns:
    dict: A dictionary where:
        - keys are town names (str)
        - values are total dead zone time for the town (int)
"""
# neighborhood_a and neighborhood_b is part of town_a
# neighborhood_a has (5, 14)
# neighborhood_b has (18, 23)
# "town_a": 4
# (3, 9) (4, 8) (12, 16) -> 3
#  (4,8) (3,9) (12,16)
# (3, 8) (1, 9) (8, 12)
def compute_dead_zone_times(party_windows):
    # TODO: implement
    
    # identify different neighborhoods with same town
    # town -> neighborhoods
    # input is the map
    # calculate dead zone time
    # the way to calculate dead zone time is
    # sort by start time for each
    # next element start time - prev end time
    # all add up, then return
    
    # from input, try to make
    # town -> neighbors
    town_neighbor_map = dict()
    for neighbor in party_windows:
        data = party_windows[neighbor]
        if data["town"] not in town_neighbor_map:
            town_neighbor_map[data["town"]] = []
        town_neighbor_map[data["town"]].append(data)
    
    res = dict()
    for town in town_neighbor_map:
        neighbors = town_neighbor_map[town]
        sorted_neighbors = sorted(neighbors, key=lambda x: x["end_hour"])
        # after sorted, we need to calculate dead zone
        dead_zone = 0
        for i in range(1, len(sorted_neighbors)):
            dead_zone += max(sorted_neighbors[i]["start_hour"] - sorted_neighbors[i-1]["end_hour"], 0)
        res[town] = dead_zone
    
    # print('party_windows', party_windows)
    # print('town_neighbor_map', town_neighbor_map)
    # print('res', res)
    return res

# -- Data -- 
PARTY_SUBMISSION_DATA = {
    "metadata": {
      "_v": "2.0",
      "count": 10,
      "_id": "partySubmissions"
    },
    "submissions": {
      "submissionData": [
        {
          "start_time": "2024-11-04T06:00:00Z",
          "end_time": "2024-11-04T11:00:00Z",
          "party_id": "0j1k2l"
        },
        {
          "start_time": "2024-11-04T14:00:00Z",
          "end_time": "2024-11-04T17:00:00Z",
          "party_id": "3m4n5o"
        },
        {
          "start_time": "2024-11-04T16:00:00Z", 
          "end_time": "2024-11-04T20:00:00Z",
          "party_id": "9s0t1u"
        },
        {
          "start_time": "2024-11-04T08:00:00Z",
          "end_time": "2024-11-04T10:00:00Z",
          "party_id": "1j2k3l"
        },
        {
          "start_time": "2024-11-04T08:00:00Z",
          "end_time": "2024-11-04T10:00:00Z",
          "party_id": "1i2j3k"
        },
        {
          "start_time": "2024-11-04T16:00:00Z",
          "end_time": "2024-11-04T20:00:00Z",
          "party_id": "7o8p9q"
        },
        {
            "start_time": "2024-11-04T14:00:00Z",
            "end_time": "2024-11-04T17:00:00Z",
            "party_id": "5d6e7f"
        },
        {
            "start_time": "2024-11-04T07:00:00Z",
            "end_time": "2024-11-04T11:00:00Z",
            "party_id": "2a3b4c"
        },
        {
            "start_time": "2024-11-04T16:00:00Z",
            "end_time": "2024-11-04T20:00:00Z",
            "party_id": "8g9h0i"
        },
        {
            "start_time": "2024-11-04T18:00:00Z",
            "end_time": "2024-11-04T22:00:00Z",
            "party_id": "4m5n6o"
        },
      ]
    }
  }

GEOGRAPHIC_DATA = {
    "geo_data": [
      {
        "neighborhood": "Pearl District",
        "town": "Greenville",
        "state": "NC",
        "city": "Normic",
        "party_id": "3m4n5o"
      },
      {
        "neighborhood": "West Village",
        "town": "Manhattan",
        "state": "NY",
        "city": "New York City",
        "party_id": "1j2k3l"
      },
      {
        "neighborhood": "Pearl District",
        "town": "Greenville",
        "state": "NC",
        "city": "Normic",
        "party_id": "9s0t1u"
      },
      {
        "neighborhood": "Ballard",
        "town": "Greenville",
        "state": "NC",
        "city": "Normic",
        "party_id": "1i2j3k"
      },
      {
        "neighborhood": "Williamsburg",
        "town": "Brooklyn",
        "state": "NY",
        "city": "New York City",
        "party_id": "2a3b4c"
      },
      {
        "neighborhood": "Pearl District",
        "town": "Greenville",
        "state": "NC",
        "city": "Normic",
        "party_id": "7o8p9q"
      },
      {
        "neighborhood": "Williamsburg",
        "town": "Brooklyn",
        "state": "NY",
        "city": "New York City",
        "party_id": "5d6e7f"
      },
      {
        "neighborhood": "Ballard",
        "town": "Greenville",
        "state": "NC",
        "city": "Normic",
        "party_id": "0j1k2l"
      },
      {
        "neighborhood": "Astoria",
        "town": "Queens",
        "state": "NY",
        "city": "New York City",
        "party_id": "8g9h0i"
      },
      {
        "neighborhood": "East Village",
        "town": "Manhattan",
        "state": "NY",
        "city": "New York City",
        "party_id": "4m5n6o"
      },
    ]
  }
  
# -- Tests -- 
if __name__ == '__main__':
    # Part 1
    computed_party_windows = create_party_windows(PARTY_SUBMISSION_DATA, GEOGRAPHIC_DATA)
    expected_party_windows = {
        'Astoria': {'start_hour': 16, 'end_hour': 20},
        'Ballard': {'start_hour': 6, 'end_hour': 11},
        'East Village': {'start_hour': 18, 'end_hour': 22},
        'Pearl District': {'start_hour': 14, 'end_hour': 20},
        'West Village': {'start_hour': 8, 'end_hour': 10},
        'Williamsburg': {'start_hour': 7, 'end_hour': 17}
    }
    assert len(computed_party_windows) == len(expected_party_windows), "Computed party windows should have the same length as expected party windows"
    for neighborhood in expected_party_windows:
        computed_window = computed_party_windows[neighborhood]
        expected_window = expected_party_windows[neighborhood]
        assert computed_window['start_hour'] == expected_window['start_hour'], "Start hour aligns for neighborhood " + neighborhood
        assert computed_window['end_hour'] == expected_window['end_hour'], "End hour aligns for neighborhood " + neighborhood

    print("Passed all Part 1 test cases!")
    
    # Part 2
    deadzone_time_per_town = compute_dead_zone_times(computed_party_windows)
    expected_deadzone_time_per_town = {
        "Greenville": 3,
        "Brooklyn": 0,
        "Manhattan": 8,
        "Queens": 0
    }
    passed_all_part_2_test_cases = True
    part_2_test_cases = [
        [deadzone_time_per_town["Greenville"], 3],
        [deadzone_time_per_town["Brooklyn"], 0],
        [deadzone_time_per_town["Manhattan"], 8],
        [deadzone_time_per_town["Queens"], 0],
    ]
    for test_case_index, test_case in enumerate(part_2_test_cases):
        computed_answer, expected_answer = test_case
        if(computed_answer != expected_answer):
            passed_all_part_2_test_cases = False
            print(f"Failed part_2 test case {test_case_index}")
            print(f"computed_answer: {computed_answer}")
            print(f"expected_answer: {expected_answer}")
    if (passed_all_part_2_test_cases):
        print("Passed all Part 2 test cases!")
