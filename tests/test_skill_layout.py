import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read(path: str) -> str:
    return (ROOT / path).read_text()


class SkillLayoutTests(unittest.TestCase):
    def test_root_skill_routes_to_intake_and_testing_guidance(self):
        content = read('skills/SKILL.md')
        self.assertIn('intake/SKILL.md', content)
        self.assertIn('testing-guidance/SKILL.md', content)
        self.assertIn('wiki repository pages first', content)

    def test_architecture_recommends_same_repo_strategy(self):
        content = read('queries/agora-skill-architecture.md')
        self.assertIn('same `agora-wiki` repository', content)
        self.assertIn('skills/', content)
        self.assertIn('wiki-first but not wiki-only', content)

    def test_product_skill_files_exist_and_define_live_doc_boundary(self):
        product_files = [
            'skills/products/rtc.md',
            'skills/products/rtm.md',
            'skills/products/conversational-ai.md',
            'skills/products/cloud-recording.md',
            'skills/products/server.md',
            'skills/products/server-gateway.md',
        ]
        for rel in product_files:
            p = ROOT / rel
            self.assertTrue(p.exists(), f'missing {rel}')
            content = p.read_text()
            self.assertIn('Live-doc escalation', content)
            self.assertIn('Wiki-first lookup', content)

    def test_testing_guidance_skill_requires_tests(self):
        content = read('skills/testing-guidance/SKILL.md')
        self.assertIn('tests or explicit test stubs', content)
        self.assertIn('token renewal behavior', content)

    def test_shared_policy_docs_exist(self):
        for rel in [
            'skills/shared/live-doc-policy.md',
            'skills/shared/repo-strategy.md',
        ]:
            self.assertTrue((ROOT / rel).exists(), f'missing {rel}')
        self.assertIn('Escalate to live docs', read('skills/shared/live-doc-policy.md'))
        self.assertIn('same `agora-wiki` repository', read('skills/shared/repo-strategy.md'))

    def test_acceptance_test_docs_exist(self):
        for rel in [
            'docs/tests/acceptance-test-matrix.md',
            'docs/tests/execution-template.md',
            'docs/tests/final-acceptance-plan.md',
        ]:
            self.assertTrue((ROOT / rel).exists(), f'missing {rel}')
        self.assertIn('Routing cases', read('docs/tests/acceptance-test-matrix.md'))
        self.assertIn('PASS / FAIL', read('docs/tests/execution-template.md'))

    def test_testing_concept_pages_exist(self):
        concept_files = [
            'concepts/testing/agora-testing-completeness-gate.md',
            'concepts/testing/agora-token-renewal-testing.md',
            'concepts/testing/agora-rtc-web-testing.md',
            'concepts/testing/agora-convoai-rest-testing.md',
        ]
        for rel in concept_files:
            self.assertTrue((ROOT / rel).exists(), f'missing {rel}')

    def test_platform_entity_pages_exist(self):
        platform_files = [
            'entities/platforms/agora-rtc-web-sdk.md',
            'entities/platforms/agora-rtc-ios-sdk.md',
            'entities/platforms/agora-rtc-android-sdk.md',
            'entities/platforms/agora-rtm-web-sdk.md',
            'entities/platforms/agora-rtm-ios-sdk.md',
            'entities/platforms/agora-rtm-android-sdk.md',
        ]
        for rel in platform_files:
            self.assertTrue((ROOT / rel).exists(), f'missing {rel}')

    def test_platform_patterns_and_gotchas_exist(self):
        self.assertTrue((ROOT / 'patterns/rtc-platform-implementation-patterns.md').exists())
        self.assertTrue((ROOT / 'patterns/rtm-platform-implementation-patterns.md').exists())
        self.assertTrue((ROOT / 'gotchas/agora-platform-identity-and-lifecycle-gotchas.md').exists())
        self.assertIn('RTC commonly uses numeric UIDs while RTM uses string identities', read('gotchas/agora-platform-identity-and-lifecycle-gotchas.md'))


if __name__ == '__main__':
    unittest.main()
