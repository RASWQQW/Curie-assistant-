import asyncio
import json
from choice.bot.apps.ownProjects.BookFinder.FinderWithGoogle import GetOurs

def Finder(authorName: str = None, BookName: str = None):
    a = GetOurs()
    elem = asyncio.run(a.Waiter(authorName, BookName, user_id=43452242, get_last=True, link=True))
    # del a.contentList; print("Yes Compiled")
    print(json.dumps(elem, indent=4, separators=(',', ': '), ensure_ascii=False))
    return elem

# Finder("Atomic Habits", "James Clear")