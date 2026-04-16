import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read(path: str) -> str:
    return (ROOT / path).read_text()


class SkillLayoutTests(unittest.TestCase):
    def test_root_skill_routes_to_standard_subskills(self):
        content = read('skills/agora/SKILL.md')
        self.assertIn('../agora-intake/SKILL.md', content)
        self.assertIn('../agora-testing-guidance/SKILL.md', content)
        self.assertIn('../agora-rtc/SKILL.md', content)
        self.assertIn('knowledge pages first', content)

    def test_skills_readme_lists_standard_entrypoints(self):
        content = read('skills/README.md')
        self.assertIn('agora/SKILL.md', content)
        self.assertIn('agora-intake/SKILL.md', content)
        self.assertIn('agora-server-gateway/SKILL.md', content)
        self.assertIn('only runtime entry layer', content)

    def test_architecture_recommends_same_repo_split_layers(self):
        content = read('knowledge/queries/agora-skill-architecture.md')
        self.assertIn('same `agora-wiki` repository', content)
        self.assertIn('skills-first, knowledge-backed, live-doc-aware', content)
        self.assertIn('knowledge/', content)

    def test_standard_product_skills_exist_and_define_live_doc_boundary(self):
        product_files = [
            'skills/agora-rtc/SKILL.md',
            'skills/agora-rtm/SKILL.md',
            'skills/agora-conversational-ai/SKILL.md',
            'skills/agora-cloud-recording/SKILL.md',
            'skills/agora-server/SKILL.md',
            'skills/agora-server-gateway/SKILL.md',
        ]
        for rel in product_files:
            p = ROOT / rel
            self.assertTrue(p.exists(), f'missing {rel}')
            content = p.read_text()
            self.assertIn('Live-doc escalation', content)
            self.assertIn('Knowledge-first lookup', content)

    def test_intake_skill_exists(self):
        content = read('skills/agora-intake/SKILL.md')
        self.assertIn('multi-product', content)
        self.assertIn('next Agora sub-skills to load', content)

    def test_testing_guidance_skill_requires_tests(self):
        content = read('skills/agora-testing-guidance/SKILL.md')
        self.assertIn('tests or explicit test stubs', content)
        self.assertIn('token renewal behavior', content)

    def test_root_skill_reference_docs_exist(self):
        for rel in [
            'skills/agora/references/knowledge-map.md',
            'skills/agora/references/shared-live-doc-policy.md',
            'skills/agora/references/shared-knowledge-architecture.md',
        ]:
            self.assertTrue((ROOT / rel).exists(), f'missing {rel}')
        self.assertIn('Escalate to live docs', read('skills/agora/references/shared-live-doc-policy.md'))
        self.assertIn('only runtime entry layer', read('skills/agora/references/shared-knowledge-architecture.md'))

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
            'knowledge/concepts/testing/agora-testing-completeness-gate.md',
            'knowledge/concepts/testing/agora-token-renewal-testing.md',
            'knowledge/concepts/testing/agora-rtc-web-testing.md',
            'knowledge/concepts/testing/agora-convoai-rest-testing.md',
        ]
        for rel in concept_files:
            self.assertTrue((ROOT / rel).exists(), f'missing {rel}')

    def test_platform_entity_pages_exist(self):
        platform_files = [
            'knowledge/entities/platforms/agora-rtc-web-sdk.md',
            'knowledge/entities/platforms/agora-rtc-ios-sdk.md',
            'knowledge/entities/platforms/agora-rtc-android-sdk.md',
            'knowledge/entities/platforms/agora-rtm-web-sdk.md',
            'knowledge/entities/platforms/agora-rtm-ios-sdk.md',
            'knowledge/entities/platforms/agora-rtm-android-sdk.md',
        ]
        for rel in platform_files:
            self.assertTrue((ROOT / rel).exists(), f'missing {rel}')

    def test_platform_patterns_and_gotchas_exist(self):
        self.assertTrue((ROOT / 'knowledge/patterns/rtc-platform-implementation-patterns.md').exists())
        self.assertTrue((ROOT / 'knowledge/patterns/rtm-platform-implementation-patterns.md').exists())
        self.assertTrue((ROOT / 'knowledge/gotchas/agora-platform-identity-and-lifecycle-gotchas.md').exists())
        self.assertIn(
            'RTC commonly uses numeric UIDs while RTM uses string identities',
            read('knowledge/gotchas/agora-platform-identity-and-lifecycle-gotchas.md'),
        )

    def test_reference_files_are_small_control_docs(self):
        refs = [
            'skills/agora/references/knowledge-map.md',
            'skills/agora/references/shared-live-doc-policy.md',
            'skills/agora/references/shared-knowledge-architecture.md',
        ]
        for rel in refs:
            p = ROOT / rel
            self.assertTrue(p.exists(), f'missing {rel}')
            line_count = len(p.read_text().splitlines())
            self.assertLess(line_count, 80, f'{rel} is too large for a reference control doc')

    def test_root_level_knowledge_dirs_were_moved_under_knowledge(self):
        for name in ['entities', 'concepts', 'patterns', 'gotchas', 'queries', 'comparisons']:
            self.assertFalse((ROOT / name).exists(), f'legacy top-level dir still exists: {name}')
        self.assertTrue((ROOT / 'knowledge').exists())

    def test_readme_and_schema_define_three_layer_model(self):
        readme = read('README.md')
        schema = read('SCHEMA.md')
        self.assertIn('skills/` — routing, intake, testing guardrails', readme)
        self.assertIn('knowledge/` — stable product knowledge', readme)
        self.assertIn('This repository has three layers', schema)
        self.assertIn('Skill layer', schema)
        self.assertIn('Knowledge layer', schema)
        self.assertIn('Source layer', schema)

    def test_no_legacy_flat_skill_files_exist(self):
        banned_paths = [
            'skills/agora-router-skill.md',
            'skills/agora-intake-skill.md',
            'skills/agora-testing-guidance-skill.md',
        ]
        for rel in banned_paths:
            self.assertFalse((ROOT / rel).exists(), f'legacy file still exists: {rel}')


if __name__ == '__main__':
    unittest.main()
