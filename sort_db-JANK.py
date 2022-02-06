from calendar import c
import json


def main():
    cnt = 0
    deletedList = list()
    db = open('jank.json')
    db_json = json.load(db)
    cards = db_json.get('cards')
    outputCards = {}

    for card in cards:
        if outputCards.get(card[0]) is None:
            outputCards[card[0]] = [card[0],int(card[1]),float(card[2])]
            continue
        if int(card[1]) < outputCards[card[0]][1]:
            outputCards[card[0]][1] = int(card[1])
        if float(card[2]) < outputCards[card[0]][2]:
            outputCards[card[0]][2] = float(card[2])
    
    keys = sorted(list(outputCards.keys()))
    cards_sorted = []
    for key in keys:
        if outputCards[key][1] == 0 and outputCards[key][2] > 0.25:
            continue
        elif outputCards[key][1] == 1 and outputCards[key][2] > 0.75:
            continue
        elif outputCards[key][1] == 2 and outputCards[key][2] > 1.50:
            continue
        elif outputCards[key][1] == 3 and outputCards[key][2] > 2.25:
            continue
        cards_sorted.append([key,outputCards[key][1],outputCards[key][2]])

    db_sorted = dict()
    db_sorted['cards'] = cards_sorted
    out = open('jank_sorted.json', 'w')
    json.dump(db_sorted, out)

    out.close()
    db.close()

    output = open('jank_sorted.json').read()
    output = output.replace('], ', '],\n')
    out = open('jank_sorted.json', 'w')
    out.write(output)
    out.close()


    #cards_sorted = sorted(cards, key=lambda c: (c[0], c[1], c[2]))

    # #THIS NESTED FOR LOOP UGH identifies a unique card and finds its lowest rarity
    # #and price
    # for idx, val in enumerate(cards_sorted):
    #     if idx < len(cards_sorted):
    #         if idx > 0 and cards_sorted[idx][0] == cards_sorted[idx-1][0]:
    #             if int(cards_sorted[idx-1][1]) < int(cards_sorted[idx][1]):
    #                 cards_sorted[idx][1] = cards_sorted[idx-1][1]
    #             if float(cards_sorted[idx-1][2]) < float(cards_sorted[idx][2]):
    #                 cards_sorted[idx][2] = cards_sorted[idx-1][2]
            
    # for idx, val in enumerate(cards_sorted):
    #     #price caps by rarity, ugly implementatin
    #     match int(cards_sorted[idx][1]):
    #         case 3:
    #             if float(cards_sorted[idx][2]) > 2.25:
    #                 if float(cards_sorted[idx][2]) <= 2.70:
    #                     deletedList.append(cards_sorted[idx].pop())
    #                     deletedList.append(cards_sorted[idx].pop())
    #                     deletedList.append(cards_sorted[idx].pop())
    #                 else:
    #                     deletedList.append(cards_sorted[idx].pop())
    #                     deletedList.append(cards_sorted[idx].pop())
    #                     deletedList.append(cards_sorted[idx].pop())
    #         case 2:
    #             if float(cards_sorted[idx][2]) > 1.50:
    #                 if float(cards_sorted[idx][2]) <= 1.80:
    #                     deletedList.append(cards_sorted[idx].pop())
    #                     deletedList.append(cards_sorted[idx].pop())
    #                     deletedList.append(cards_sorted[idx].pop())
    #                 else:
    #                     deletedList.append(cards_sorted[idx].pop())
    #                     deletedList.append(cards_sorted[idx].pop())
    #                     deletedList.append(cards_sorted[idx].pop())
    #         case 1:
    #             if float(cards_sorted[idx][2]) > 0.75:
    #                 if float(cards_sorted[idx][2]) <= 0.90:
    #                     deletedList.append(cards_sorted[idx].pop())
    #                     deletedList.append(cards_sorted[idx].pop())
    #                     deletedList.append(cards_sorted[idx].pop())
    #                 else:
    #                     deletedList.append(cards_sorted[idx].pop())
    #                     deletedList.append(cards_sorted[idx].pop())
    #                     deletedList.append(cards_sorted[idx].pop())
    #         case 0:
    #             if float(cards_sorted[idx][2]) > 0.25:
    #                 if float(cards_sorted[idx][2]) <= 0.30:
    #                     deletedList.append(cards_sorted[idx].pop())
    #                     deletedList.append(cards_sorted[idx].pop())
    #                     deletedList.append(cards_sorted[idx].pop())
    #                 else:
    #                     deletedList.append(cards_sorted[idx].pop())
    #                     deletedList.append(cards_sorted[idx].pop())
    #                     deletedList.append(cards_sorted[idx].pop())
    #         case _: continue

    # for idx, val in enumerate(cards_sorted):
    #     if idx < len(cards_sorted):
    #         if idx > 0 and cards_sorted[idx] != [] and cards_sorted[idx-1] != []:
    #             if idx > 0 and cards_sorted[idx][0] == cards_sorted[idx-1][0]:
    #                 deletedList.append(cards_sorted[idx-1].pop())
    #                 deletedList.append(cards_sorted[idx-1].pop())
    #                 deletedList.append(cards_sorted[idx-1].pop())




if __name__ == '__main__':
    main()
