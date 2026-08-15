import unittest

from core.agent import build_prompt, run_agent, select_workflow


class AgentTests(unittest.TestCase):
    def test_select_workflow_multilingual(self):
        cases = {
            "Create a wallpaper": "wallpaper",
            "做一张手机壁纸": "wallpaper",
            "Create a sticker": "sticker",
            "帮我做透明贴纸": "sticker",
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
        with self.assertRaisesRegex(ValueError, "wallpaper, sticker, or photocard"):
            run_agent("make something", "cute")


if __name__ == "__main__":
    unittest.main()
