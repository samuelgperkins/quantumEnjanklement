import json
from os import defpath


def main():
    cnt = 0
    fi = open('default-cards.json', 'r', encoding='utf-8')
    fo = open('jank.json', 'w')

    fi.readline()
    fo.write('{\n"cards": [\n')

    while True:
        # each card is a JSON object, strip off the trailing ','
        line = fi.readline().strip()

        # end of the list
        if line[0] == ']':
            break

        if line[-1] == ',':
            line = line[:-1]

        try:
            line_json = json.loads(line)
        except json.decoder.JSONDecodeError as e:
            print('Bad JSON: {}'.format(line))
            print(e)
            continue

        #name = line_json.get('name')
        #rarity = line_json.get('rarity')
        name = line_json.get('name').replace('"', '\\"')
        rarity = line_json.get('rarity').replace('"', '\\"')
        #prices = line_json.get('prices').get('usd').replace('"', '\\"')
        prices = line_json.get('prices').get('usd')
        pricesFoil = line_json.get('prices').get('usd_foil')

        # image_uris = line_json.get('image_uris')
        # if image_uris is None:
            # card_faces = line_json.get('card_faces')
            # if card_faces is None:
                # image = ''
            # else:
                # image = card_faces[0].get('image_uris').get('large')
        # else:
            # image = image_uris.get('large')
            # if image is None:
                # image = ''

        # image = image.replace('"', '\\"')

        # only vintage legal - skips restricted cards
        # 7/30/2020, we want to include restricted cards though, just not
        #   cards not legal in vintage, like ante or conspiracy or silver border
        #   We also want to spare Lurrus, since his vintage banning is very
        #   specific to how companion works in constructed
        if ((line_json.get('legalities').get('vintage') == 'not_legal' or \
                line_json.get('legalities').get('vintage') == 'banned' or\
                line_json.get('legalities').get('vintage') == 'restricted' or\
                line_json.get('legalities').get('legacy') == 'banned' or\
                line_json.get('legalities').get('modern') == 'banned' or\
                line_json.get('legalities').get('pioneer') == 'banned' or\
                line_json.get('legalities').get('pauper') == 'banned' or\
                line_json.get('border_color') == 'gold') \
                and name != 'Lurrus of the Dream-Den'):
            continue

        # no memorabilia
        #if line_json.get('set_type') == 'memorabilia':
            #continue

        # no none price
        if prices == None:
            if(pricesFoil != None):
                prices = pricesFoil
            else:
                continue

        #price caps by rarity
        # match rarity:
        #     case 'rare':
        #         if float(prices) > 1.75:
        #             continue
        #     case 'uncommon':
        #         if float(prices) > 0.75:
        #             continue
        #     case 'common':
        #         if float(prices) > 0.25:
        #             continue
        #     case _:
        #         if float(prices) > 2.25:
        #             continue

        #price caps by rarity
        match rarity:
            case 'rare':
                rarity = 2
            case 'uncommon':
                rarity = 1
            case 'common':
                rarity = 0
            case _:
                rarity = 3


        # no normal basics
        #if name == 'Swamp' or name == 'Island' or name == 'Mountain' or \
        #        name == 'Forest' or name == 'Plains':
        #    continue

        # no basics
        if name == 'Swamp' or name == 'Island' or name == 'Mountain' or \
                name == 'Forest' or name == 'Plains' or name == 'Snow-Covered Swamp' \
                or name == 'Snow-Covered Island' or name == 'Snow-Covered Mountain' \
                or name == 'Snow-Covered Forest' or name == 'Snow-Covered Plains' or name == 'Wastes':
            continue

        if line_json.get('lang') != 'en':
            continue

        if line_json.get('reserved') is True:
            continue
            
        if line_json.get('digital') is True:
            continue

        # if name == 'Badlands':
        #     print(json.dumps(line_json, indent=2))
        #     input()

        # fo.write('["{}","{}","{}"],\n'.format(
        #     name,
        #     rarity,
        #     prices
        # ))

        fo.write('["{}","{}","{}"],\n'.format(
            name,
            rarity,
            prices
        ))

        #fo.write('[\"name\":"{}",\"rarity\":"{}",\"prices\":"{}"],\n'.format(
        #    #"name",
        #    name,
        #    #"rarity",
        #    rarity,
        #    #"prices",
        #    prices
        #))

        cnt += 1
        if cnt % 1000 == 0:
            print('Read {} cards'.format(cnt))

    print('Read {} cards'.format(cnt))
    fi.close()
    fo.close()


if __name__ == '__main__':
    main()
