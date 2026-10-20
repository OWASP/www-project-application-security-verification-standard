# ASVS website

This repository publishes the OWASP Application Security Verification Standard project website. The standard itself remains in [OWASP/ASVS](https://github.com/OWASP/ASVS).

The website uses the same Jekyll / Just the Docs mechanism and pinned theme revision as [OWASP Secure Headers](https://github.com/OWASP/secure-headers-project), including its OWASP blue sidebar, cyan accents, fonts, search and responsive navigation. The custom styling derives from that project's Apache-2.0-licensed stylesheet. ASVS content retains its [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.

## Content

Edit `index.md` for the overview and `mainsite/*.md` for the other pages. Existing tab, sidebar and migration files are retained as migration references and excluded from publication. Images, branding and the release ZIP remain at their original paths. The new pages preserve the existing editorial content; dated events and links have not been refreshed.

Use Liquid's `relative_url` filter for local links so both GitHub project paths and custom domains work. For example: `{{ '/downloads/' | relative_url }}`.

## Local preview

### Windows

Install [Ruby 4.0.7 with Devkit](https://rubyinstaller.org/downloads/) and complete its MSYS2 development toolchain setup (`ridk install`). Ruby must be on your PATH; reopen your terminal after installation.

Double-click `start-site.bat`, or run it from Command Prompt. It installs Bundler if needed, installs missing gems into `vendor/bundle`, and starts the site at **http://127.0.0.1:4000/**. The first run needs internet access; Jekyll also downloads the remote theme when it starts. Wait for the server to start before opening the URL. Keep the window open while testing and press **Ctrl+C** to stop. Changes to `_config.yml` require restarting the script.

### Other platforms

Install Ruby 4.0.7 and Bundler, then run:

```sh
bundle install
bundle exec jekyll serve
```

Open http://localhost:4000/.

The project uses Jekyll 4 directly so it can run on Ruby 4.0.7, rather than the older `github-pages` gem bundle. CI builds on Ruby 4.0.7 and checks the Windows launcher.

## Build and deployment

```sh
JEKYLL_ENV=production bundle exec jekyll build
python3 scripts/check_site.py _site --baseurl ""
```

In repository Settings → Pages, select **GitHub Actions** as the source. The site workflow builds and checks pull requests, and deploys pushes to `master`. This is intended to replace the old OWASP theme build. Repository Pages configuration must be enabled by a maintainer.

The production address is https://asvs.owasp.org/. `_config.yml` sets that origin with an empty `baseurl`, and `CNAME` records the domain. The published build uses this configuration without a repository-path override. The browser review checks this exact deployment directory. A separate build checks that repository-prefixed URLs still work for project-path previews.

The Pages source must be **GitHub Actions**, not **Deploy from a branch**. The built-in branch publisher uses an older Ruby/Jekyll/Sass toolchain that cannot compile this site's Sass modules. After merging configuration changes, the `Build and deploy website` workflow publishes the validated artifact.

## Migration provenance

Source content was read from the upstream master branch through GitHub's connector. The patch changes text files only and preserves the existing binary assets in the target repository. The migration branch is based on the current OWASP commit and retains all binary assets through its original Git tree.

## Windows installation troubleshooting

If dependency installation reports `failed to load encoding (UTF-16BE)`, first check Ruby independently of the site:

```powershell
ruby -e "p 'test'.encode('UTF-16BE').bytes"
```

If this fails, repair or reinstall Ruby 4.0.7 with Devkit and reopen your terminal. The launcher checks this before installing dependencies.

If the encoding check passes but RubyGems crashes verifying a downloaded gem, update its tooling (`gem update --system`) and remove only the specific cached `.gem` named in the error, then rerun `start-site.bat`. Do not disable gem verification.

## Theme stylesheet maintenance

The theme templates remain pinned to the Secure Headers theme revision. The styles in `_sass/asvs/` are local MIT-licensed derivatives of that revision, migrated from Sass imports and deprecated global functions to modules. This removes the deprecations without changing the palette or suppressing compiler warnings.

To regenerate after reviewing a theme update, check out the revision recorded in `scripts/migrate_theme_styles.py`, then run `python scripts/migrate_theme_styles.py /path/to/just-the-docs`. Commit the generated light and dark styles and license. The shared Liquid stylesheet include loads these modules for the default, light and dark stylesheets. No extra tooling is needed for a normal Jekyll build.
