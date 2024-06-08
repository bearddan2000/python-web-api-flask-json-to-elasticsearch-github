class Repo():
    
    def __init__(self, name, desc, topics: list) -> None:
        self.name = name
        self.compose_desc(desc)
        self.compose_topics(topics)

    def compose_desc(self, desc):
        self.desc = '-'
        if desc is not None:
            self.desc = desc

    def compose_topics(self, topics):
        tmp_lst = topics
        for item in self.name.split("-"):
            tmp_lst.append(item)
        condensed_lst = list(set(tmp_lst))
        self.topics = "::".join(condensed_lst)

    def __str__(self) -> str:
        return f"{self.name}, {self.desc}, {self.topics}"

    def __iter__(self):
        return iter([self.name, self.desc, self.topics])