"""Regression checks for the custom-domain/repository-prefix deployment mixup."""
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

from check_site import check


class DeploymentPaths(unittest.TestCase):
    def setUp(self):
        self.temporary = TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        files = ['index.html', '404.html', 'assets/css/just-the-docs-default.css',
                 'assets/js/search-data.json']
        files += [f'{page}/index.html' for page in (
            'downloads', 'meetup', 'supporters', 'news', 'acknowledgements',
            'get-involved', 'users', 'team')]
        for name in files:
            path = self.root / name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text('')

    def homepage(self, prefix):
        (self.root / 'index.html').write_text(
            f'<link rel="stylesheet" href="{prefix}/assets/css/just-the-docs-default.css">'
            f'<a href="{prefix}/downloads/">Downloads</a>')

    def test_custom_domain_uses_root_paths(self):
        self.homepage('')
        self.assertEqual(check(self.root, ''), [])

    def test_versioned_stylesheet_urls_are_supported(self):
        for prefix in ('', '/project'):
            with self.subTest(prefix=prefix):
                self.homepage(prefix)
                home = self.root / 'index.html'
                home.write_text(home.read_text().replace('.css"', '.css?v=1234567890"'))
                self.assertEqual(check(self.root, prefix), [])

    def test_project_prefix_is_not_valid_for_custom_domain(self):
        # All files exist: inferring the prefix alone used to pass this build,
        # even though the stylesheet URL would return 404 on the custom domain.
        self.homepage('/www-project-application-security-verification-standard')
        self.assertTrue(any('Wrong deployed baseurl' in error
                            for error in check(self.root, '')))

    def test_explicit_project_path_preview_is_supported(self):
        self.homepage('/project')
        self.assertEqual(check(self.root, '/project'), [])


if __name__ == '__main__':
    unittest.main()
