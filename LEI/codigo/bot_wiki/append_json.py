import json

# f = open("wiki_all.json", "a")

# prettyJSON = json.dumps(wiki2,sort_keys=True, indent=2,ensure_ascii=True)
# f.write(prettyJSON)

# wiki_first = json.loads(open("wiki_first.json").read())
# prettyJSON = json.dumps(wiki_first,sort_keys=True, indent=2,ensure_ascii=True)
# f.write(prettyJSON)

# wiki_second = json.loads(open("wiki_second.json").read())
# prettyJSON = json.dumps(wiki_second,sort_keys=True, indent=2,ensure_ascii=True)
# f.write(prettyJSON)

# wiki_third = json.loads(open("wiki_third.json").read())
# prettyJSON = json.dumps(wiki_third,sort_keys=True, indent=2,ensure_ascii=True)
# f.write(prettyJSON)


# wiki_fourth = json.loads(open("wiki_fourth.json").read())
# prettyJSON = json.dumps(wiki_fourth,sort_keys=True, indent=2,ensure_ascii=True)
# f.write(prettyJSON)

# wiki_fifth = json.loads(open("wiki_fifth.json").read())
# prettyJSON = json.dumps(wiki_fifth,sort_keys=True, indent=2,ensure_ascii=True)
# f.write(prettyJSON)

# wiki2 = json.loads(open("wiki2.json").read())

wiki = json.loads(open("wiki_all.json").read())
prettyJSON = json.dumps(wiki,sort_keys=True, indent=2,ensure_ascii=False)

f = open("wiki_all_direito.json", "w")
f.write(prettyJSON)

