import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from colors import best_contrast_color, is_valid_hex, luminance, normalize_hex, random_hex_color


class LuminanceTests(unittest.TestCase):
    def test_black_is_zero(self):
        self.assertAlmostEqual(luminance("#000000"), 0.0)

    def test_white_is_one(self):
        self.assertAlmostEqual(luminance("#ffffff"), 1.0)

    def test_red_luminance(self):
        self.assertAlmostEqual(luminance("#ff0000"), 0.299)


class BestContrastColorTests(unittest.TestCase):
    def test_dark_background_uses_white_text(self):
        self.assertEqual(best_contrast_color("#000000"), "white")

    def test_light_background_uses_black_text(self):
        self.assertEqual(best_contrast_color("#ffffff"), "black")


class IsValidHexTests(unittest.TestCase):
    def test_six_char_with_hash(self):
        self.assertTrue(is_valid_hex("#a1b2c3"))

    def test_six_char_uppercase(self):
        self.assertTrue(is_valid_hex("A1B2C3"))

    def test_three_char_shorthand(self):
        self.assertTrue(is_valid_hex("#fff"))

    def test_three_char_without_hash(self):
        self.assertTrue(is_valid_hex("abc"))

    def test_invalid_characters(self):
        self.assertFalse(is_valid_hex("#gggggg"))

    def test_invalid_length(self):
        self.assertFalse(is_valid_hex("#ff"))

    def test_empty(self):
        self.assertFalse(is_valid_hex(""))

    def test_with_whitespace(self):
        self.assertTrue(is_valid_hex("  #fff  "))


class NormalizeHexTests(unittest.TestCase):
    def test_uppercases_are_lowercased_and_shorthand_expanded(self):
        self.assertEqual(normalize_hex("#FFF"), "#ffffff")

    def test_shorthand_expanded(self):
        self.assertEqual(normalize_hex("abc"), "#aabbcc")

    def test_already_normalized_passthrough(self):
        self.assertEqual(normalize_hex("#a1b2c3"), "#a1b2c3")

    def test_strips_whitespace_and_normalizes(self):
        self.assertEqual(normalize_hex("  #FfF  "), "#ffffff")


class RandomHexColorTests(unittest.TestCase):
    def test_format(self):
        for _ in range(100):
            color = random_hex_color()
            self.assertTrue(color.startswith("#"))
            self.assertEqual(len(color), 7)
            self.assertTrue(all(c in "0123456789abcdef" for c in color[1:]))

    def test_variety(self):
        colors = {random_hex_color() for _ in range(50)}
        self.assertGreater(len(colors), 1)


if __name__ == "__main__":
    unittest.main()
