import pandas

GRAY = "Gray"
BLACK = "Black"
CINNAMON = "Cinnamon"

data = pandas.read_csv("2018_Central_Park_Squirrel_Data.csv")
grey_squirrels = data[data["Primary Fur Color"] == GRAY]
cinnamon_squirrels = data[data["Primary Fur Color"] == CINNAMON]
black_squirrels = data[data["Primary Fur Color"] == BLACK]

squirrels_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [len(grey_squirrels), len(cinnamon_squirrels), len(black_squirrels)]
}

squirrels_data = pandas.DataFrame(squirrels_dict)
squirrels_data.to_csv("squirrel_count.csv")