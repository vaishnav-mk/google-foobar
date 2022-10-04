def solution(area):
    final = []
    while area > 0:
        squareSide = int(area ** 0.5)
        squareArea = squareSide ** 2
        area -= squareArea
        res.append(squareArea)

    return final
