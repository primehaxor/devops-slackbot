import dataset

def check_entries(link):
    db = dataset.connect('sqlite:///feed.db')
    table = db['news']
    q = table.find_one(link=link)
    if q:
        return True
    else:
        return False

def add_entries(title, link, timestamp):
   db = dataset.connect('sqlite:///feed.db')
   table = db['news']
   table.insert(dict(name=title, link=link, date=timestamp))
