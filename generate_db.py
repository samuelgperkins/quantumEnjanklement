import json


def main():
    cnt = 0
    fi = open('default-cards.json', 'r', encoding='utf-8')
    fo = open('birthday.json', 'w')

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

        name = line_json.get('name').replace('"', '\\"')
        card_set = line_json.get('set').replace('"', '\\"')
        date = line_json.get('released_at').replace('"', '\\"')

        image_uris = line_json.get('image_uris')
        if image_uris is None:
            card_faces = line_json.get('card_faces')
            if card_faces is None:
                image = ''
            else:
                image = card_faces[0].get('image_uris').get('large')
        else:
            image = image_uris.get('large')
            if image is None:
                image = ''

        image = image.replace('"', '\\"')

        # only vintage legal - skips restricted cards
        # 7/30/2020, we want to include restricted cards though, just not
        #   cards not legal in vintage, like ante or conspiracy or silver border
        #   We also want to spare Lurrus, since his vintage banning is very
        #   specific to how companion works in constructed
        if ((line_json.get('legalities').get('vintage') == 'not_legal' or \
                line_json.get('legalities').get('vintage') == 'banned') \
                and name != 'Lurrus of the Dream-Den'):
            continue

        # no promos
        if line_json.get('set_type') == 'promo':
            continue

        # no normal basics
        if name == 'Swamp' or name == 'Island' or name == 'Mountain' or \
                name == 'Forest' or name == 'Plains':
            continue

        if line_json.get('lang') != 'en':
            continue

        if line_json.get('reserved') is True:
            continue

        # if name == 'Badlands':
        #     print(json.dumps(line_json, indent=2))
        #     input()

        fo.write('["{}","{}","{}","{}"],\n'.format(
            name,
            card_set,
            date,
            image
        ))

        cnt += 1
        if cnt % 1000 == 0:
            print('Read {} cards'.format(cnt))

    print('Read {} cards'.format(cnt))
    fi.close()
    fo.close()


if __name__ == '__main__':
    main()
