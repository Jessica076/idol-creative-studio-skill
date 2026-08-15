import unittest

from core.agent import build_prompt, run_agent, select_workflow


class AgentTests(unittest.TestCase):
    def test_select_workflow_multilingual(self):
        cases = {
            "Create a wallpaper": "wallpaper",
            "做一张手机壁纸": "wallpaper",
            "Create a sticker": "sticker",
            "帮我做透明贴纸": "sticker",
            "把这张照片拆解成贴纸页": "sticker-sheet",
            "Create a photo-to-sticker sheet": "sticker-sheet",
            "Create a photocard": "photocard",
            "做一张生日小卡": "photocard",
        }
        for request, expected in cases.items():
            with self.subTest(request=request):
                self.assertEqual(select_workflow(request), expected)

    def test_prompt_contains_identity_output_and_safety_constraints(self):
        prompt = build_prompt("photocard", "black silver luxury", "HAPPY DAY")
        self.assertIn("recognizable identity", prompt)
        self.assertIn("750x1050", prompt)
        self.assertIn("HAPPY DAY", prompt)
        self.assertIn("official endorsement", prompt)

    def test_unknown_request_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "sticker sheet"):
            run_agent("make something", "cute")

    def test_sticker_sheet_prompt_has_hybrid_treatment_and_opaque_background(self):
        prompt = build_prompt("sticker-sheet", "warm cream paper with colors sampled from the photo")
        self.assertIn("Keep people photorealistic", prompt)
        self.assertIn("broad color blocks", prompt)
        self.assertIn("opaque", prompt)
        self.assertIn("Do not use\ntransparency", prompt)
        self.assertIn("exact 16:25", prompt)
        self.assertIn("1600x2500", prompt)


if __name__ == "__main__":
    unittest.main()
