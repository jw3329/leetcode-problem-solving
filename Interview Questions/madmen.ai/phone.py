ads = [
    Ad(
        "ad-001",
        [
            Attribute("channel", "social"),
            Attribute("headline", "Buy Now!"),
            Attribute("region", "US"),
            Attribute("budget", 500),
        ]
    ),
    Ad(
        "ad-002",
        [
            Attribute("channel", "search"),
            Attribute("headline", "Sale Today"),
            Attribute("region", "EU"),
            Attribute("budget", 2000),
        ]
    ),
    Ad(
        "ad-003",
        [
            Attribute("channel", "social"),
            Attribute("region", "US"),
            Attribute("budget", 1000),
        ]
    )
]

aggregated = aggregate_attributes(ads)

[
    AggregatedAttribute(
        name="channel",
        values=["social", "search"]
    ),
    AggregatedAttribute(
        name="headline",
        values=["Buy Now!", "Sale Today"]
    ),
    AggregatedAttribute(
        name="region",
        values=["US", "EU"]
    ),
    AggregatedAttribute(
        name="budget",
        min_value=500,
        max_value=2000
    )
]

from typing import List, Optional, Union

class Attribute:
    def __init__(self, name: str, value: Union[str, int]):
        self.name = name
        self.value = value

class Ad:
    def __init__(self, id: str, attributes: List[Attribute]):
        self.id = id
        self.attributes = attributes

class AggregatedAttribute:
    def __init__(
        self, 
        name: str, 
        values: Optional[List[str]] = None,
        min_value: Optional[int] = None,
        max_value: Optional[int] = None
    ):
        self.name = name
        self.values = values
        self.min_value = min_value
        self.max_value = max_value

def aggregate_attributes(ads: List[Ad]) -> List[AggregatedAttribute]:
    
    # aking ads as input
    # iterate each ads
    # find name of ad
    # try to put into list for agg attr, and its type
    # if type is string, then try to agg to list
    # if type is number, then get min and max
    
    # dict
    # name -> [values]
  	
  	attrs = set() # (attr_name, type)
  	name_dict = dict()
    for ad in ads:
      # put attr
    	for attr in ad.attributes:
      	if attr.name not in name_dict:
          name_dict[attr.name] = set()
        name_dict[attr.name].add(attr.value)
      	# check if attr is in attrs
        if attr.name not in attrs:
        	attrs.add(attr.name)
  	# now we are having attrs
    res = []
  	# iterate each attr, and try to append accordingly
    for attr in attrs:
    	# grab values from name_dict
    	values = name_dict[attr]
    	# check the first element
      first_elem = values[0]
    	# check if attr is string or number
      if type(first_elem) == str:
      	# temp = set()
      	# for ad in ads:
      	# # put attr
      	# for ad_attr in ad.attributes:
      	# if ad_attr.name == attr[0]:
      	# # if matching, then we try to find if value is in temp
      	# # if not in temp, then append
      	# # if in temp, then skip,
      	# if ad_attr.value not in temp:
      	# temp.add(ad_attr.value)
        # after ad ends
      	# we have to append to agg object
        res.append(AggregatedAttribute(name=attr,values=list(values)))
      elif type(first_elem) == int:
        min_value = sys.maxsize
        max_value = -sys.maxsize
        # for ad in ads:
        # # put attr
        #   for ad_attr in ad.attributes:
        #     if ad_attr.name == attr[0]:
        #       # if matching, then try to do comparison of number
        #       min_value = min(min_value, ad_attr.value)
        #       max_value = min(max_value, ad_attr.value)
        # # do final
      	
      	# iterate values
        for value in values:
          min_value = min(min_value, value)
          max_value = min(max_value, value)
        res.append(AggregatedAttribute(name=attr,min_value=min_value,max_value=max_value))
    return res    

    
    
    
    
    
    


