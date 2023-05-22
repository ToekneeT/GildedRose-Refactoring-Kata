# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if item.name != "Sulfuras, Hand of Ragnaros":
                item.sell_in -= 1
            if item.name == "Aged Brie":
                if (item.quality < 50 and item.sell_in >= 0) or (item.quality == 49 and item.sell_in < 0):
                    item.quality += 1
                elif item.quality < 50 and item.sell_in < 0:
                    item.quality += 2
            elif item.name == "Backstage passes to a TAFKAL80ETC concert":
                if item.sell_in < 0:
                    item.quality = 0
                else:
                    if item.quality < 50:
                        item.quality += 1
                    if item.sell_in < 10 and item.quality < 50:
                        item.quality += 1
                    if item.sell_in < 5 and item.quality < 50:
                        item.quality += 1
            elif item.name.split()[0] == "Conjured":
                if item.sell_in >= 0:
                    item.quality -= 2
                else:
                    item.quality -= 4
            elif item.name != "Sulfuras, Hand of Ragnaros":
                if (item.sell_in >= 0 and item.quality > 0) or (item.sell_in >= 0 and item.quality == 1):
                    item.quality -= 1
                elif item.sell_in < 0 and item.quality > 0:
                    item.quality -= 2


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
