import pandas as pd
import codecs
class Redditor:
    def __init__(self, name):
        self.name = name

def get_comments(row):
    comments = row["comments"]
    lst = eval(comments)
    return lst

def add_tag(value, tag):
    return f"<{tag}> {value} </{tag}> \n"
def add_tag_comments(comment):
    return add_tag(comment[5], "comment")
def post_to_string(row):
    result = ""
    post = str(row["title"]) + "\n" + str(row["selftext"])
    result += add_tag(post, "post")
    for comment in get_comments(row):
        result += add_tag_comments(comment)
    return add_tag(result, "Submission")+"\n"
df = pd.read_csv("new_results.csv")
data = df[["author", 'selftext', 'num_comments', 'title', 'id', 'comments']]
print(data.columns)
data = data[df.num_comments > 0]
with codecs.open("new_results.txt", "w", "utf-8") as file:
    for i in range(len(data["comments"])):
        row = data.iloc[i, :]
        file.write(post_to_string(row))