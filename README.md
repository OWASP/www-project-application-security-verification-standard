# ASVS website

This repository publishes the OWASP Application Security Verification Standard project website. The standard itself remains in [OWASP/ASVS](https://github.com/OWASP/ASVS).

The website uses the same Jekyll / Just the Docs mechanism and pinned theme revision as [OWASP Secure Headers](https://github.com/OWASP/secure-headers-project), including its OWASP blue sidebar, cyan accents, fonts, search and responsive navigation. The custom styling derives from that project's Apache-2.0-licensed stylesheet. ASVS content retains its [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.

## Content

Edit `index.md` for the overview and `mainsite/*.md` for the other pages. Existing tab, sidebar and migration files are retained as migration references and excluded from publication. Images, branding and the release ZIP remain at their original paths. The new pages preserve the existing editorial content; dated events and links have not been refreshed.

Use Liquid's `relative_url` filter for local links so both GitHub project paths and custom domains work. For example: `{{ '/downloads/' | relative_url }}`.

## Local preview

Install Ruby 3.3 and Bundler, then run:

```sh
bundle install
bundle exec jekyll serve
```

Open http://localhost:4000/www-project-application-security-verification-standard/.

## Build and deployment

```sh
JEKYLL_ENV=production bundle exec jekyll build
python3 scripts/check_site.py _site
```

In repository Settings → Pages, select **GitHub Actions** as the source. The site workflow builds and checks pull requests, and deploys pushes to `master`. This is intended to replace the old OWASP theme build. Repository Pages configuration must be enabled by a maintainer.

The default address is https://owasp.github.io/www-project-application-security-verification-standard/. For a custom domain, set `url` and `baseurl` in `_config.yml`, add the appropriate `CNAME`, and remove the workflow's `--baseurl` override. No custom domain is assumed by this migration.

## Migration provenance

Source content was read from the upstream master branch through GitHub's connector. The patch changes text files only and preserves the existing binary assets in the target repository. The migration branch is based on the current OWASP commit and retains all binary assets through its original Git tree.
