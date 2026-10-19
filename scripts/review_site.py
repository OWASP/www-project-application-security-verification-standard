"""Browser smoke test and desktop/mobile captures for the built website."""
import base64
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
import json
from pathlib import Path
import shutil
from threading import Thread

from playwright.sync_api import sync_playwright

site = Path('/tmp/asvs-site-root')
server = ThreadingHTTPServer(('127.0.0.1', 8765), partial(SimpleHTTPRequestHandler, directory=str(site)))
Thread(target=server.serve_forever, daemon=True).start()
captures = Path('/tmp/asvs-review')
captures.mkdir(exist_ok=True)


def capture(page, name):
    data = page.screenshot(path=str(captures / (name + '.jpg')), type='jpeg', quality=65)
    print('ASVS_SCREENSHOT ' + json.dumps({'name': name, 'base64': base64.b64encode(data).decode()}), flush=True)


with sync_playwright() as p:
    browser = p.chromium.launch(executable_path=shutil.which('google-chrome') or shutil.which('chromium'), args=['--no-sandbox'])
    page = browser.new_page(viewport={'width': 1365, 'height': 900}, device_scale_factor=1)
    errors = []
    page.on('pageerror', lambda error: errors.append(str(error)))
    page.goto('http://127.0.0.1:8765/', wait_until='networkidle')
    page.evaluate('document.fonts.ready')
    capture(page, 'desktop-overview')
    print('ASVS_REVIEW ' + json.dumps({'sidebar_background': page.locator('.side-bar').evaluate('(e) => getComputedStyle(e).backgroundColor'), 'navigation_links': page.locator('.site-nav .nav-list-link').all_text_contents(), 'broken_images': page.locator('img').evaluate_all('(imgs) => imgs.filter(i => !i.complete || i.naturalWidth === 0).map(i => i.src)')}), flush=True)
    assert 'placeholder' not in page.locator('.site-nav .nav-list-link').all_text_contents()
    assert page.locator('img[src$="LinkedIn_Logo.svg"]').first.evaluate('(i) => i.getBoundingClientRect().height') <= 21
    assert page.locator('.btn-primary').first.evaluate('(e) => getComputedStyle(e).backgroundColor') == 'rgb(0, 53, 148)'
    search = page.locator('#search-input')
    search.fill('downloads')
    page.wait_for_timeout(1500)
    capture(page, 'desktop-search')
    print('ASVS_SEARCH ' + json.dumps({'results_text': page.locator('#search-results').inner_text()}), flush=True)
    search.fill('')
    page.goto('http://127.0.0.1:8765/supporters/', wait_until='networkidle')
    capture(page, 'desktop-supporters')
    mobile = browser.new_page(viewport={'width': 390, 'height': 844}, device_scale_factor=1, is_mobile=True, has_touch=True)
    mobile.goto('http://127.0.0.1:8765/', wait_until='networkidle')
    capture(mobile, 'mobile-overview')
    overflow = mobile.evaluate('document.documentElement.scrollWidth > innerWidth')
    mobile.locator('#menu-button').click()
    capture(mobile, 'mobile-navigation')
    print('ASVS_BROWSER_RESULT ' + json.dumps({'javascript_errors': errors, 'mobile_horizontal_overflow': overflow, 'mobile_navigation_visible': mobile.locator('.site-nav').is_visible()}), flush=True)
    assert not errors, errors
    assert not overflow, 'Horizontal overflow on mobile'
    assert mobile.locator('.site-nav').is_visible(), 'Mobile menu did not open'
    browser.close()
server.shutdown()
