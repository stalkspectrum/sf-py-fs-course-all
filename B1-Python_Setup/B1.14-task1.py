flowers = {
    "iris_setosa": {
        "sepal_length": [3.6, 4.9, 4.8, 4.7],
        "sepal_width": [2.9, 3.3, 3.2, 3.1],
        "petal_length": [1.3, 1.2, 1.5, 1.4]
    },
    "iris_virginica": {
        "sepal_length": [7.2, 7.0, 7.9],
        "sepal_width": [3.1, 2.7, 2.8],
        "petal_length": [5.5, 5.5, 6.5]

    },
    "iris_versicolor": {
        "sepal_length": [6.5, 6.0, 6.1, 6.2, 6.3],
        "sepal_width": [2.8, 2.9, 2.4, 2.7, 2.7],
        "petal_length": [4.8, 4.7, 5.0, 4.9, 4.8]
    }
}

TotalSepalLength = 0
TotalSepalWidth = 0
TotalPetalLength = 0
CountSepalLength = 0
CountSepalWidth = 0
CountPetalLength = 0

for IrisesKeys, IrisesValues in flowers.items():
    TotalSepalLength = TotalSepalLength + sum(IrisesValues["sepal_length"])
    CountSepalLength = CountSepalLength + len(IrisesValues["sepal_length"])
    TotalSepalWidth = TotalSepalWidth + sum(IrisesValues["sepal_width"])
    CountSepalWidth = CountSepalWidth + len(IrisesValues["sepal_width"])
    TotalPetalLength = TotalPetalLength + sum(IrisesValues["petal_length"])
    CountPetalLength = CountPetalLength + len(IrisesValues["petal_length"])

print(TotalSepalLength / CountSepalLength)
print(TotalSepalWidth / CountSepalWidth)
print(TotalPetalLength / CountPetalLength)

#####=====----- ETHALON -----=====#####
sepal_lengths = []
sepal_widths = []
petal_lengths = []
for flower, data in flowers.items():
    for length in data['sepal_length']:
        sepal_lengths.append(length)
    for width in data['sepal_width']:
        sepal_widths.append(width)
    for length in data['petal_length']:
        petal_lengths.append(length)
mean_sepal_length = sum(sepal_lengths) / len(sepal_lengths)
print(mean_sepal_length)
mean_sepal_width = sum(sepal_widths) / len(sepal_widths)
print(mean_sepal_width)
mean_petal_length = sum(petal_lengths) / len(petal_lengths)
print(mean_petal_length)

#####=====----- Refactored 2021 -----=====#####
sum_ = 0.
values_ = 0
for k_ in (list(flowers)):
    sum_ += sum(flowers[k_]['sepal_length'])
    values_ += len(flowers[k_]['sepal_length'])
mean_sepal_length = int(sum_ / values_ * 100) / 100
print('mean_sepal_length = ', mean_sepal_length)

sum_ = 0.
values_ = 0
for k_ in (list(flowers)):
    sum_ += sum(flowers[k_]['sepal_width'])
    values_ += len(flowers[k_]['sepal_width'])
mean_sepal_width = int(sum_ / values_ * 100) / 100
print('mean_sepal_width = ', mean_sepal_width)

sum_ = 0.
values_ = 0
for k_ in (list(flowers)):
    sum_ += sum(flowers[k_]['petal_length'])
    values_ += len(flowers[k_]['petal_length'])
mean_petal_length = int(sum_ / values_ * 100) / 100
print('mean_petal_length = ', mean_petal_length)

##### Дополнительно размышления об алгоритме округления до одного десятичного знака
sm = 2.8733333333333333
sss = int(sm * 100)
print(sss)
ssss = sss % 10
if ssss >= 5:
    sss = (sss - ssss + 10) / 100
print(ssss)
print(sss)

##########################################################################