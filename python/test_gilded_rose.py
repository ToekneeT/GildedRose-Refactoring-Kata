# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_item_name(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("foo", items[0].name)

    def test_sell_in(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(-1, items[0].sell_in)

    # SHould be 0, quality never goes under 0.
    def test_quality_zero(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)

    # Should be 3 as quality drops by double once sell in date is past due.
    def test_quality_past_sell_in(self):
        items = [Item("foo", 0, 5)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(3, items[0].quality)

    def test_array_count(self):
        items = [Item("foo", 0, 5)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("foo", items[0].name)
        self.assertEqual(3, items[0].quality)
        self.assertEqual(1, len(items))

    # Aged Brie should go up in quality while the sell in should go down.
    def test_aged_brie(self):
        items = [Item("Aged Brie", 1, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].sell_in)
        self.assertEqual(1, items[0].quality)
        gilded_rose.update_quality()
        self.assertEqual(-1, items[0].sell_in)
        self.assertEqual(3, items[0].quality)

    def test_quality_fifty(self):
        items = [Item("Aged Brie", 1, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].sell_in)
        self.assertEqual(50, items[0].quality)
        items = [Item("Aged Brie", 0, 49)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(50, items[0].quality)

    # Sulfuras shouldn't go down in quality or sell in.
    def test_sulfuras(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 10, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(10, items[0].sell_in)
        self.assertEqual(80, items[0].quality)

    # Checks quality of the backstage passes when over 10. Also makes sure that
    # it doesn't go over the 50 quality mark.
    def test_backstage_ten_more(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 11, 48)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(10, items[0].sell_in)
        self.assertEqual(49, items[0].quality)
        gilded_rose.update_quality()
        self.assertEqual(9, items[0].sell_in)
        self.assertEqual(50, items[0].quality)
        gilded_rose.update_quality()
        self.assertEqual(8, items[0].sell_in)
        self.assertEqual(50, items[0].quality)

    def test_backstage_ten_less(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 10, 2)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(9, items[0].sell_in)
        self.assertEqual(4, items[0].quality)

    # Increases by 3 when less than 5 days.
    def test_backstage_five_less(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 6, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(5, items[0].sell_in)
        self.assertEqual(2, items[0].quality)
        gilded_rose.update_quality()
        self.assertEqual(4, items[0].sell_in)
        self.assertEqual(5, items[0].quality)

    # 0 after concert is over.
    def test_backstage_zero(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 0, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(-1, items[0].sell_in)
        self.assertEqual(0, items[0].quality)
    
    # Tests conjured quality. Makes sure it drops by 2, then past sell in by 4.
    def test_conjured(self):
        items = [Item("Conjured Mana Cake", 2, 8)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(1, items[0].sell_in)
        self.assertEqual(6, items[0].quality)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].sell_in)
        self.assertEqual(4, items[0].quality)
        gilded_rose.update_quality()
        self.assertEqual(-1, items[0].sell_in)
        self.assertEqual(0, items[0].quality)


if __name__ == '__main__':
    unittest.main()
