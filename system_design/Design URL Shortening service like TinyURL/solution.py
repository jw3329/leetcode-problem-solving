class TinyURL:
    
    char_map = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

    def __init__(self):
        self.count = 0
        self.id_map = {}
        self.long_id_map = {}

    def insert_long_url(self,long_url):
        # check if long url is in the database
        if long_url in self.long_id_map: return self.long_id_map[long_url]
        self.count += 1
        self.id_map[self.count] = {
            'short_url': self.id_to_short_url(self.count),
            'long_url': long_url
        }
        self.long_id_map[long_url] = self.count
        return self.count

    def id_to_short_url(self,id):
        short_url = ''
        while id:
            short_url += self.char_map[id % 62]
            id //= 62
        return short_url[::-1]

    def short_url_to_id(self,short_url):
        id = 0
        for c in short_url:
            sub_val, add_val = 0, 0
            if 'a' <= c <= 'z':
                sub_val = ord('a')
                add_val = 0
            elif 'A' <= c <= 'Z':
                sub_val = ord('A')
                add_val = 26
            elif '0' <= c <= '9':
                sub_val = ord('0')
                add_val = 52
            id = id * 62 + ord(c) - sub_val + add_val
        return id 

def generate_urls(num):
    res = []
    char_list = 'abcdefghizklmnopqrstuvwxyz'
    import random
    for i in range(num):
        url = ''
        for j in range(10):
            index = random.randint(0,25)
            url += char_list[index]
        res.append(url)
    return res

s = TinyURL()

urls = generate_urls(100)

for url in urls:
    s.insert_long_url(url)

print(s.id_map)
print(s.long_id_map)